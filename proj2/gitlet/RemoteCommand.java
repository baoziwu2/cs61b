package gitlet;

import java.io.File;
import java.util.*;

import static gitlet.ErrorHandling.messageAndExit;
import static gitlet.Repository.*;

public class RemoteCommand {
    public static void remoteAdd(String remoteName, String remotePath) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        if (remoteFile.exists()) {
            messageAndExit("A remote with that name already exists.");
        }
        Utils.writeContents(remoteFile, remotePath);
    }

    public static void remoteRemove(String remoteName) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        if (!remoteFile.exists()) {
            messageAndExit("A remote with that name does not exist.");
        }
        remoteFile.delete();
    }

    private static File getRemoteGitletDir(String remoteName) {
        File remoteConfigFile = Utils.join(REMOTES_DIR, remoteName);

        if (!remoteConfigFile.exists()) {
            messageAndExit("Remote directory not found.");
        }

        String remotePath = Utils.readContentsAsString(remoteConfigFile);
        File remoteGitletDir = new File(remotePath);

        if (!remoteGitletDir.exists() || !remoteGitletDir.isDirectory()) {
            messageAndExit("Remote directory not found.");
        }

        return remoteGitletDir;
    }

    public static void push(String remoteName, String remoteBranchName) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        ErrorHandling.checkRemoteDirectoryCanBeFound(remoteFile);
        File remoteGitletDir = getRemoteGitletDir(remoteName);

        String localHeadId = getHeadCommitId();
        File remoteBranchFile = Utils.join(remoteGitletDir, "refs", "heads", remoteBranchName);
        String remoteHeadId = null;
        if (remoteBranchFile.exists()) {
            remoteHeadId = Utils.readContentsAsString(remoteBranchFile);
        }

        if (remoteHeadId != null && !isAncestor(localHeadId, remoteHeadId)) {
            messageAndExit("Please pull down remote changes before pushing.");
        }

        List<String> commitsToPush = new ArrayList<>();
        Set<String> blobsToPush = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(localHeadId);
        visited.add(localHeadId);

        while (!queue.isEmpty()) {
            String currentId = queue.poll();
            if (currentId.equals(remoteHeadId)) {
                continue;
            }
            commitsToPush.add(currentId);
            Commit c = getCommitById(currentId);
            if (c == null) continue;

            blobsToPush.addAll(c.getTrackedFiles().values());

            if (c.getParentId() != null && !visited.contains(c.getParentId())) {
                queue.add(c.getParentId());
                visited.add(c.getParentId());
            }
            if (c.isMergeCommit() && !visited.contains(c.getSecondParentId())) {
                queue.add(c.getSecondParentId());
                visited.add(c.getSecondParentId());
            }
        }

        File remoteCommitsDir = Utils.join(remoteGitletDir, "objects", "commits");
        File remoteBlobsDir = Utils.join(remoteGitletDir, "objects", "blobs");

        for (String commitId : commitsToPush) {
            File localCommit = Utils.join(COMMITS_DIR, commitId);
            File remoteCommit = Utils.join(remoteCommitsDir, commitId);
            Utils.writeContents(remoteCommit, Utils.readContents(localCommit));
        }
        for (String blobId : blobsToPush) {
            File localBlob = Utils.join(BLOBS_DIR, blobId);
            File remoteBlob = Utils.join(remoteBlobsDir, blobId);
            if (!remoteBlob.exists()) {
                Utils.writeContents(remoteBlob, Utils.readContents(localBlob));
            }
        }

        Utils.writeContents(remoteBranchFile, localHeadId);
    }

    private static boolean isAncestor(String commitId, String ancestorId) {
        Queue<String> queue = new LinkedList<>();
        queue.add(commitId);
        while (!queue.isEmpty()) {
            String current = queue.poll();
            if (current.equals(ancestorId)) {
                return true;
            }
            Commit c = getCommitById(current);
            if (c != null && c.getParentId() != null) {
                queue.add(c.getParentId());
            }
            if (c != null && c.isMergeCommit()) {
                queue.add(c.getSecondParentId());
            }
        }
        return false;
    }

    public static void fetch(String remoteName, String remoteBranchName) {
        File remoteGitletDir = getRemoteGitletDir(remoteName); // 假設這是一個輔助函數
        File remoteBranchFile = Utils.join(remoteGitletDir, "refs", "heads", remoteBranchName);
        if (!remoteBranchFile.exists()) {
            messageAndExit("That remote does not have that branch.");
        }

        String remoteHeadId = Utils.readContentsAsString(remoteBranchFile);

        Queue<String> commitsToFetch = new LinkedList<>();
        commitsToFetch.add(remoteHeadId);
        Set<String> visited = new HashSet<>();
        visited.add(remoteHeadId);

        while (!commitsToFetch.isEmpty()) {
            String commitId = commitsToFetch.poll();
            File localCommitFile = Utils.join(COMMITS_DIR, commitId);

            if (!localCommitFile.exists()) {
                File remoteCommitFile = Utils.join(remoteGitletDir, "objects", "commits", commitId);
                Utils.writeContents(localCommitFile, Utils.readContents(remoteCommitFile));
            }

            Commit commit = getCommitById(commitId);
            if (commit == null) continue;

            for (String blobId : commit.getTrackedFiles().values()) {
                File localBlobFile = Utils.join(BLOBS_DIR, blobId);
                if (!localBlobFile.exists()) {
                    File remoteBlobFile = Utils.join(remoteGitletDir, "objects", "blobs", blobId);
                    Utils.writeContents(localBlobFile, Utils.readContents(remoteBlobFile));
                }
            }

            if (commit.getParentId() != null && !visited.contains(commit.getParentId())) {
                commitsToFetch.add(commit.getParentId());
                visited.add(commit.getParentId());
            }
            if (commit.isMergeCommit() && !visited.contains(commit.getSecondParentId())) {
                commitsToFetch.add(commit.getSecondParentId());
                visited.add(commit.getSecondParentId());
            }
        }

        File localRemoteRefDir = Utils.join(GITLET_DIR, "refs", "remotes", remoteName);
        if (!localRemoteRefDir.exists()) {
            localRemoteRefDir.mkdirs(); // 創建多級目錄
        }
        File localRefFile = Utils.join(localRemoteRefDir, remoteBranchName);
        Utils.writeContents(localRefFile, remoteHeadId);
    }

    public static void pull(String remoteName, String remoteBranchName) {
        fetch(remoteName, remoteBranchName);
        MergeCommand.executeForPull(remoteName, remoteBranchName);
    }
}
