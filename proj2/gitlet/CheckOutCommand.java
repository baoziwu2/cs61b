package gitlet;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CheckOutCommand {
    public static void execute(String... args) { // args exclude "checkout"
        int len = args.length;
        if (len == 1) { // checkout branch name
            checkOutBranch(args[0]);
        } else if (len == 2) { // checkout -- [file name]
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

    public static void validateNoUntrackedFilesWouldBeOverwritten(String branchName) {
        Commit targetCommit = Repository.getCommitByBranch(branchName);
        Repository.validateNoUntrackedFilesWouldBeOverwritten(targetCommit);
    }

    static void checkOutBranch(String branchName) {
        validateBranchExists(branchName);
        validateIsNotCurrentBranch(branchName);
        validateNoUntrackedFilesWouldBeOverwritten(branchName);

        Commit targetCommit = Repository.getCommitByBranch(branchName);
        Commit currentCommit = Repository.getCurrentCommit();

        Map<String, String> targetFiles = targetCommit.getTrackedFiles();

        Repository.resetWorkspaceToCommit(targetCommit);

        String headContent = "ref: refs/heads/" + branchName;
        Utils.writeContents(Repository.HEAD_FILE, headContent);

        StagingArea.clear();
    }

    static void restoreFileFromCommit(Commit targetCommit, String fileName) {
        Map<String, String> trackedFiles = targetCommit.getTrackedFiles();
        if (!trackedFiles.containsKey(fileName)) {
            ErrorHandling.messageAndExit("File does not exist in that commit."); //
        }

        String blobId = trackedFiles.get(fileName);
        File blobFile = Utils.join(Repository.BLOBS_DIR, blobId);
        byte[] fileContent = Utils.readContents(blobFile);

        File fileInCWD = Utils.join(Repository.CWD, fileName);
        Utils.writeContents(fileInCWD, fileContent);
    }

    private static void checkOutFileInHead(String fileName) {
        Commit headCommit = Repository.getCurrentCommit();
        restoreFileFromCommit(headCommit, fileName);
    }

    static String findFullCommitId(String abbreviatedId) {
        final int fullCommitLength = 40;
        if (abbreviatedId.length() == fullCommitLength) {
            File commitFile = Utils.join(Repository.COMMITS_DIR, abbreviatedId);
            return commitFile.exists() ? abbreviatedId : null;
        }

        List<String> matchingIds = new ArrayList<>();
        List<String> allCommitIds = Utils.plainFilenamesIn(Repository.COMMITS_DIR);
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

    static void checkOutFileInCommit(String commitId,
                                     String fileName) {
        String fullCommitId = findFullCommitId(commitId);
        if (fullCommitId == null) {
            ErrorHandling.messageAndExit("No commit with that id exists.");
        }
        Commit targetCommit = Repository.getCommitById(fullCommitId);
        restoreFileFromCommit(targetCommit, fileName);
    }
}
