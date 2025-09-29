package gitlet;

import java.io.File;

import static gitlet.Repository.CWD;

public class ErrorHandling {
    public static void messageAndExit(String message) {
        System.out.println(message);
        System.exit(0);
    }

    public static void checkGitletEmpty(File repository) {
        if (repository.exists()) {
            messageAndExit("A Gitlet version-control system already exists in the current directory.");
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
}
