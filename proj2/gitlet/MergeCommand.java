package gitlet;

import java.io.File;
import java.util.*;

import static gitlet.ErrorHandling.messageAndExit;

public class MergeCommand {
    private static void previousChecker(String branchName, StagingArea stagingArea) {
        if (!stagingArea.isEmpty()) {
            messageAndExit("You have uncommitted changes.");
        }
        if (!Repository.doesBranchExist(branchName)) {
            messageAndExit("A branch with that name does not exist.");
        }
        String currentBranch = Repository.getCurrentBranch();
        if (currentBranch.equals(branchName)) {
            messageAndExit("Cannot merge a branch with itself.");
        }
        Commit targetCommit = Repository.getCommitByBranch(branchName);
        Repository.validateNoUntrackedFilesWouldBeOverwritten(targetCommit);
    }

    private static String findSplitPoint(String targetCommitId, String currentCommitId) {
        Map<String, Integer> currentAncestors = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(currentCommitId);
        currentAncestors.put(currentCommitId, 0);
        while (!queue.isEmpty()) {
            String commitId = queue.poll();
            Commit commit = Repository.getCommitById(commitId);
            if (commit == null) {
                continue;
            }

            if (commit.getParentId() != null
                    && !currentAncestors.containsKey(commit.getParentId())) {
                currentAncestors.put(commit.getParentId(), currentAncestors.get(commitId) + 1);
                queue.add(commit.getParentId());
            }
            if (commit.isMergeCommit()
                    && !currentAncestors.containsKey(commit.getSecondParentId())) {
                currentAncestors.put(commit.getSecondParentId(),
                        currentAncestors.get(commitId) + 1);
                queue.add(commit.getSecondParentId());
            }
        }

        Set<String> visitedInTarget = new HashSet<>();
        queue.add(targetCommitId); // already empty
        visitedInTarget.add(targetCommitId);
        while (!queue.isEmpty()) {
            String commitId = queue.poll();
            if (currentAncestors.containsKey(commitId)) {
                return commitId; // find lca
            }
            Commit commit = Repository.getCommitById(commitId);
            if (commit == null) {
                continue;
            }

            if (commit.getParentId() != null && !visitedInTarget.contains(commit.getParentId())) {
                visitedInTarget.add(commit.getParentId());
                queue.add(commit.getParentId());
            }
            if (commit.isMergeCommit() && !visitedInTarget.contains(commit.getSecondParentId())) {
                visitedInTarget.add(commit.getSecondParentId());
                queue.add(commit.getSecondParentId());
            }
        }
        return null; // should never reach here
    }

    private static void lcaSpecialChecker(String splitPointId,
                                          String givenCommitId,
                                          String currentCommitId,
                                          String branchName) {
        if (splitPointId.equals(givenCommitId)) {
            ErrorHandling.messageAndExit("Given branch is an ancestor of the current branch.");
        }

        if (splitPointId.equals(currentCommitId)) {
            CheckOutCommand.checkOutBranch(branchName);
            ErrorHandling.messageAndExit("Current branch fast-forwarded.");
        }
    }

    private static void handleConflict(String fileName, String currentBlobId, String givenBlobId) {
        String headContent = "";
        if (currentBlobId != null) {
            File blobFile = Utils.join(Repository.BLOBS_DIR, currentBlobId);
            headContent = Utils.readContentsAsString(blobFile);
        }

        String givenContent = "";
        if (givenBlobId != null) {
            File blobFile = Utils.join(Repository.BLOBS_DIR, givenBlobId);
            givenContent = Utils.readContentsAsString(blobFile);
        }

        String conflictContent = "<<<<<<< HEAD\n"
                + headContent
                + "=======\n"
                + givenContent
                + ">>>>>>>\n";

        File fileInCWD = Utils.join(Repository.CWD, fileName);
        Utils.writeContents(fileInCWD, conflictContent);

        Repository.addFile(fileName);
    }

    private static void merge(String branchName, Commit splitPointCommit,
                              Commit currentCommit, Commit givenCommit,
                              String givenCommitId) {
        Map<String, String> currentFiles = currentCommit.getTrackedFiles();
        Map<String, String> givenFiles = givenCommit.getTrackedFiles();
        Map<String, String> splitFiles = splitPointCommit.getTrackedFiles();

        Set<String> allFileNames = new TreeSet<>();
        allFileNames.addAll(currentFiles.keySet());
        allFileNames.addAll(givenFiles.keySet());
        allFileNames.addAll(splitFiles.keySet());

        boolean conflictOccurred = false;

        for (String fileName : allFileNames) {
            String splitBlobId = splitFiles.get(fileName);
            String currentBlobId = currentFiles.get(fileName);
            String givenBlobId = givenFiles.get(fileName);

            boolean modifiedInCurrent = !Objects.equals(splitBlobId, currentBlobId);
            boolean modifiedInGiven = !Objects.equals(splitBlobId, givenBlobId);

            if (modifiedInGiven && !modifiedInCurrent) {
                // rule 1 and 5
                if (givenBlobId != null) {
                    CheckOutCommand.restoreFileFromCommit(givenCommit, fileName);
                    Repository.addFile(fileName);
                } else {
                    // rule 6
                    Repository.remove(fileName);
                }
            } else if (modifiedInCurrent && !modifiedInGiven) {
                // rule 2 and 4 and 7
                continue;
            } else if (!modifiedInCurrent && !modifiedInGiven) {
                continue;
            } else {
                if (Objects.equals(currentBlobId, givenBlobId)) {
                    // rule 3
                    continue;
                } else {
                    // rule 8
                    conflictOccurred = true;
                    handleConflict(fileName, currentBlobId, givenBlobId);
                }
            }
        }

        String currentBranch = Repository.getCurrentBranch();
        String givenBranchName = branchName;
        String mergeMessage = "Merged " + givenBranchName + " into " + currentBranch + ".";

        Repository.commit(mergeMessage, givenCommitId);

        if (conflictOccurred) {
            System.out.println("Encountered a merge conflict.");
        }
    }

    public static void execute(String branchName) {
        StagingArea stagingArea = StagingArea.load();
        previousChecker(branchName, stagingArea);

        File givenBranchFile = Utils.join(Repository.HEADS_DIR, branchName);
        String givenCommitId = Utils.readContentsAsString(givenBranchFile);

        Commit givenCommit = Repository.getCommitById(givenCommitId);

        Commit currentCommit = Repository.getCurrentCommit();
        String currentCommitId = Repository.getHeadCommitId();

        String splitPointId = findSplitPoint(givenCommitId, currentCommitId);
        Commit splitPointCommit = Repository.getCommitById(splitPointId);

        lcaSpecialChecker(splitPointId, givenCommitId, currentCommitId, branchName);
        merge(branchName, splitPointCommit, currentCommit, givenCommit, givenCommitId);
    }
}

