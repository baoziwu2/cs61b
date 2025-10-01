package gitlet;

import java.io.File;
import java.util.*;

import static gitlet.ErrorHandling.messageAndExit;
import static gitlet.Repository.*;

public class RemoteCommand {
    public static void remoteAdd(String remoteName, String remotePath) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        ErrorHandling.checkRemoteExist(remoteFile);
        Utils.writeContents(remoteFile, remotePath);
    }

    public static void remoteRemove(String remoteName) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        ErrorHandling.checkRemoteExist(remoteFile);
        remoteFile.delete();
    }

    public static void push(String remoteName, String remoteBranchName) {
        File remoteFile = Utils.join(REMOTES_DIR, remoteName);
        ErrorHandling.checkRemoteDirectoryCanBeFound(remoteFile);
        String remotePath = Utils.readContentsAsString(remoteFile);
        File remoteGitletDir = new File(remotePath);
        ErrorHandling.checkRemoteDirectoryCanBeFound(remoteGitletDir);

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
        String currentId = localHeadId;
        while (currentId != null && !currentId.equals(remoteHeadId)) {
            commitsToPush.add(currentId);
            Commit c = getCommitById(currentId);
            blobsToPush.addAll(c.getTrackedFiles().values());
            currentId = c.getParentId();
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
            if (!remoteBlob.exists()) { // 優化：不存在才複製
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
}
