package gitlet;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CheckOutCommand {
    public static void execute(String... args) { // args exclude "checkout"
        int len = args.length;
        if(len == 1) { // checkout branch name
            checkOutBranch(args[0]);
        } else if(len == 2) { // checkout -- [file name]
            checkOutFileInHead(args[1]);
        } else { // len == 3, checkout [commit id] -- [file name]
            checkOutFileInCommit(args[0], args[2]);
        }
    }

    private static void validateBranchExists(String branch) {
        if (!Repository.doesBranchExist(branch)) {
            ErrorHandling.messageAndExit("No such branch exists.");
        }
    }

    private static void validateIsNotCurrentBranch(String branch) {
        if (branch.equals(Repository.getCurrentBranch())) {
            ErrorHandling.messageAndExit("No need to checkout the current branch.");
        }
    }

    private static void validateNoUntrackedFilesWouldBeOverwritten(String branchName) {
        Commit currentCommit = Repository.getCurrentCommit();
        Commit targetCommit = Repository.getCommitByBranch(branchName);

        List<String> untrackedFiles = new ArrayList<>();
        for (String fileName : Utils.plainFilenamesIn(Repository.CWD)) {
            boolean isTracked = currentCommit.getTrackedFiles().containsKey(fileName);
            boolean isStaged = StagingArea.load().getFileForAddition().containsKey(fileName); // 重新加载以获取最新状态
            if (!isTracked && !isStaged) {
                untrackedFiles.add(fileName);
            }
        }

        for (String untrackedFile : untrackedFiles) {
            if (targetCommit.getTrackedFiles().containsKey(untrackedFile)) {
                ErrorHandling.messageAndExit("There is an untracked file in the way; "
                        + "delete it, or add and commit it first.");
            }
        }
    }

    private static void checkOutBranch(String branchName) {
        validateBranchExists(branchName);
        validateIsNotCurrentBranch(branchName);
        validateNoUntrackedFilesWouldBeOverwritten(branchName);

        Commit targetCommit = Repository.getCommitByBranch(branchName);
        Commit currentCommit = Repository.getCurrentCommit();

        Map<String, String> targetFiles = targetCommit.getTrackedFiles();
        Map<String, String> currentFiles = currentCommit.getTrackedFiles();

        for(Map.Entry<String, String> entry : targetFiles.entrySet()) {
            String fileName = entry.getKey();
            String blobId = entry.getValue();

            File blobFile = Utils.join(Repository.OBJECTS_DIR, blobId);
            byte[] fileContent = Utils.readContents(blobFile);
            File fileInCWD = Utils.join(Repository.CWD, fileName);
            Utils.writeContents(fileInCWD, fileContent);
        }

        for(String fileName : currentFiles.keySet()) {
            if(!targetFiles.containsKey(fileName)) {
                Utils.restrictedDelete(fileName);
            }
        }

        String headContent = "ref: refs/heads/" + branchName;
        Utils.writeContents(Repository.HEAD_FILE, headContent);

        StagingArea.clear();
    }

    private static void restoreFileFromCommit(Commit targetCommit, String fileName) {
        Map<String, String> trackedFiles = targetCommit.getTrackedFiles();
        if (!trackedFiles.containsKey(fileName)) {
            ErrorHandling.messageAndExit("File does not exist in that commit."); //
        }

        String blobId = trackedFiles.get(fileName);
        File blobFile = Utils.join(Repository.OBJECTS_DIR, blobId);
        byte[] fileContent = Utils.readContents(blobFile);

        File fileInCWD = Utils.join(Repository.CWD, fileName);
        Utils.writeContents(fileInCWD, fileContent);
    }

    private static void checkOutFileInHead(String fileName) {
        Commit headCommit = Repository.getCurrentCommit();
        restoreFileFromCommit(headCommit, fileName);
    }

    private static String findFullCommitId(String abbreviatedId) {
        if (abbreviatedId.length() == 40) {
            File commitFile = Utils.join(Repository.OBJECTS_DIR, abbreviatedId);
            return commitFile.exists() ? abbreviatedId : null;
        }

        List<String> matchingIds = new ArrayList<>();
        List<String> allCommitIds = Utils.plainFilenamesIn(Repository.OBJECTS_DIR);
        if (allCommitIds != null) {
            for (String id : allCommitIds) {
                if (id.startsWith(abbreviatedId)) {
                    matchingIds.add(id);
                }
            }
        }

        if (matchingIds.size() == 1) {
            return matchingIds.get(0);
        }
        return null;
    }

    private static void checkOutFileInCommit(String commitId, String fileName) {
        String fullCommitId = findFullCommitId(commitId);
        if (fullCommitId == null) {
            ErrorHandling.messageAndExit("No commit with that id exists.");
        }
        Commit targetCommit = Repository.getCommitById(fullCommitId);
        restoreFileFromCommit(targetCommit, fileName);
    }
}
