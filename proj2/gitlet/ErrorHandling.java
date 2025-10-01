package gitlet;

import java.io.File;

import static gitlet.Repository.CWD;
import static gitlet.Repository.doesBranchExist;

public class ErrorHandling {
    public static void messageAndExit(String message) {
        System.out.println(message);
        System.exit(0);
    }

    public static void checkGitletEmpty(File repository) {
        if (repository.exists()) {
            messageAndExit("A Gitlet version-control system already"
                    + " exists in the current directory.");
        }
    }

    public static void checkCreatingDirectory(boolean flag) {
        if (!flag) {
            messageAndExit("Creating directory fail.");
        }
    }

    public static void checkFileExists(String fileName) {
        File file = new File(CWD, fileName);
        if (!file.exists()) {
            messageAndExit("File does not exist.");
        }
    }

    public static void checkStageEmpty(StagingArea stagingArea) {
        if (stagingArea.isEmpty()) {
            messageAndExit("No changes added to the commit.");
        }
    }

    public static void checkCommitMessage(String message) {
        if (message == null || message.isEmpty()) {
            messageAndExit("Please enter a commit message.");
        }
    }

    public static void checkBranchExist(String branch) {
        if (doesBranchExist(branch)) {
            messageAndExit("A branch with that name already exists.");
        }
    }

    public static void checkBranchNotExist(String branch) {
        if (!doesBranchExist(branch)) {
            messageAndExit("A branch with that name does not exist.");
        }
    }

    public static void checkForSameBranch(String branch) {
        String currentBranch = Repository.getCurrentBranch();
        if (branch.equals(currentBranch)) {
            messageAndExit("Cannot remove the current branch.");
        }
    }

    public static void checkRemoteDirectoryCanBeFound(File remoteFile) {
        if (!remoteFile.exists()) {
            messageAndExit("Remote directory not found.");
        }
    }
}
