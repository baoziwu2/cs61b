package gitlet;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.*;

import static gitlet.Repository.*;

public class Display {
    private static String formatDate(Date date) {
        // Match the expected format: EEE MMM d HH:mm:ss yyyy Z, in US locale
        SimpleDateFormat sdf = new SimpleDateFormat("EEE MMM d HH:mm:ss yyyy Z", Locale.US);
        return sdf.format(date);
    }

    public static void log() {
        String currentId = getHeadCommitId();
        while (currentId != null) {
            Commit currentCommit = getCommitById(currentId);
            printLogMessage(currentId, currentCommit);

            currentId = currentCommit.getParentId();
        }
    }

    private static void printLogMessage(String currentId, Commit currentCommit) {
        System.out.println("===");
        System.out.println("commit " + currentId);
        if (currentCommit.isMergeCommit()) {
            System.out.println("Merge: " + currentCommit.getParentId().substring(0, 7) + " "
                    + currentCommit.secondParentId.substring(0, 7));
        }
        System.out.println("Date: " + formatDate(currentCommit.getDate()));
        System.out.println(currentCommit.getMessage());
        System.out.println();
    }

    public static void globalLog() {
        List<String> commitFiles = Utils.plainFilenamesIn(COMMITS_DIR);

        if (commitFiles != null) {
            for (String fileName : commitFiles) {
                Commit commit = getCommitById(fileName);
            }
        }
    }

    private static void printBranches() {
        System.out.println("=== Branches ===");
        String currentBranch = getCurrentBranch();
        List<String> allBranches = Utils.plainFilenamesIn(HEADS_DIR);
        if (allBranches != null) {
            Collections.sort(allBranches);
            for (String branch : allBranches) {
                if (branch.equals(currentBranch)) {
                    System.out.println("*" + branch);
                } else {
                    System.out.println(branch);
                }
            }
        }
        System.out.println();
    }

    private static void printStagedFiles(StagingArea stagingArea) {
        System.out.println("=== Staged Files ===");
        Set<String> stagedFiles = stagingArea.getFileForAddition().keySet();
        for (String file : stagedFiles) {
            System.out.println(file);
        }
        System.out.println();
    }

    private static void printRemovedFiles(StagingArea stagingArea) {
        System.out.println("=== Removed Files ===");
        Set<String> removedFiles = stagingArea.getFilesForRemoval();
        for (String file : removedFiles) {
            System.out.println(file);
        }
        System.out.println();
    }

    private static void printModifiedButUnstagedFiles(StagingArea stagingArea) {
        System.out.println("=== Modifications Not Staged For Commit ===");

        Commit currentCommit = getCurrentCommit();
        Map<String, String> trackedFiles = currentCommit.getTrackedFiles();
        Map<String, String> stagedFiles = stagingArea.getFileForAddition();
        Set<String> removedFiles = stagingArea.getFilesForRemoval();

        Set<String> filesToPrint = new TreeSet<>();

        for (String fileName : trackedFiles.keySet()) {
            File fileInCWD = new File(CWD, fileName);
            boolean exists = fileInCWD.exists();

            if (exists) {
                String commitBlobId = trackedFiles.get(fileName);
                String cwdBlobId = Utils.sha1(Utils.readContents(fileInCWD));
                // 情况1: 文件被跟踪，内容被修改，且未被暂存(add)
                if (!commitBlobId.equals(cwdBlobId) && !stagedFiles.containsKey(fileName)) {
                    filesToPrint.add(fileName + " (modified)");
                }
            } else {
                // 情况2: 文件被跟踪，但在工作区被删除，且未被暂存(rm)
                if (!removedFiles.contains(fileName)) {
                    filesToPrint.add(fileName + " (deleted)");
                }
            }
        }

        // 检查已暂存的文件
        for (String fileName : stagedFiles.keySet()) {
            File fileInCWD = Utils.join(CWD, fileName);
            boolean exists = fileInCWD.exists();

            if (exists) {
                String stagedBlobId = stagedFiles.get(fileName);
                String cwdBlobId = Utils.sha1(Utils.readContents(fileInCWD));
                // 情况3: 文件已暂存，但工作区内容又被修改
                if (!stagedBlobId.equals(cwdBlobId)) {
                    filesToPrint.add(fileName + " (modified)");
                }
            } else {
                // 情况4: 文件已暂存，但又被从工作区删除
                filesToPrint.add(fileName + " (deleted)");
            }
        }

        for (String line : filesToPrint) {
            System.out.println(line);
        }
        System.out.println();
    }

    private static void printUntrackedFiles(StagingArea stagingArea) {
        System.out.println("=== Untracked Files ===");

        Commit currentCommit = getCurrentCommit();
        Map<String, String> trackedFiles = currentCommit.getTrackedFiles();
        Map<String, String> stagedFiles = stagingArea.getFileForAddition();
        List<String> cwdFiles = Utils.plainFilenamesIn(CWD);

        if (cwdFiles != null) {
            Set<String> untrackedFiles = new TreeSet<>();
            for (String fileName : cwdFiles) {
                if (!trackedFiles.containsKey(fileName) && !stagedFiles.containsKey(fileName)) {
                    untrackedFiles.add(fileName);
                }
            }

            for (String fileName : untrackedFiles) {
                System.out.println(fileName);
            }
        }

        System.out.println();
    }

    public static void status() {
        StagingArea stagingArea = StagingArea.load();
        printBranches();
        printStagedFiles(stagingArea);
        printRemovedFiles(stagingArea);
        printModifiedButUnstagedFiles(stagingArea);
        printUntrackedFiles(stagingArea);
    }
}
