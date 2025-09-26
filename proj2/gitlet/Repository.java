package gitlet;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.*;

import static gitlet.Utils.*;
import static gitlet.ErrorHandling.*;

// TODO: any imports you need here

/**
 * Represents a gitlet repository.
 *  TODO: It's a good idea to give a description here of what else this Class
 *  does at a high level.
 *
 * @author azbnbNotFound
 */
public class Repository {
    /**
     * TODO: add instance variables here.
     * List all instance variables of the Repository class here with a useful
     * comment above them describing what that variable represents and how that
     * variable is used. We've provided two examples for you.
     */

    /**
     * The current working directory.
     */
    public static final File CWD = new File(System.getProperty("user.dir"));
    /**
     * The .gitlet directory.
     */
    public static final File GITLET_DIR = join(CWD, ".gitlet");

    /**
     * Storage for Commit and Blob objects.
     */
    public static final File OBJECTS_DIR = join(GITLET_DIR, "objects");
    /**
     * Storage for references (like branches).
     */
    public static final File REFS_DIR = join(GITLET_DIR, "refs");
    /**
     * Storage for branch heads.
     */
    public static final File HEADS_DIR = join(REFS_DIR, "heads");
    /**
     * The staging area file.
     */
    public static final File STAGING_FILE = join(GITLET_DIR, "index");
    /**
     * The HEAD file, pointing to the current branch.
     */
    public static final File HEAD_FILE = join(GITLET_DIR, "HEAD");

    public static String getHeadCommitId() {
        String headContent = Utils.readContentsAsString(HEAD_FILE);
        String branchPath = headContent.split(": ")[1];
        File branchFile = Utils.join(GITLET_DIR, branchPath);
        return Utils.readContentsAsString(branchFile);
    }

    public static Commit getCommitById(String id) {
        if (id == null) {
            return null;
        }
        File commitFile = Utils.join(OBJECTS_DIR, id);
        if (!commitFile.exists()) {
            return null;
            //throw new GitletException("Commit with id " + id + " does not exist.");
        }
        return Utils.readObject(commitFile, Commit.class);
    }

    public static Commit getCurrentCommit() {
        String headCommitId = getHeadCommitId();
        return getCommitById(headCommitId);
    }

    public static boolean doesBranchExist(String branch) {
        File branchFile = Utils.join(HEADS_DIR, branch);
        return branchFile.exists();
    }

    public static String getCurrentBranch() {
        String headContent = Utils.readContentsAsString(HEAD_FILE);
        return headContent.split(": ")[1].substring("refs/heads/".length());
    }

    public static Commit getCommitByBranch(String branch) {
        if (!doesBranchExist(branch)) {
            messageAndExit("No such branch exists.");
        }
        File branchFile = Utils.join(HEADS_DIR, branch);
        String commitId = Utils.readContentsAsString(branchFile);
        return getCommitById(commitId);
    }

    public static void initRepository() {
        checkGitletEmpty(GITLET_DIR);

        boolean dirCreated = true;
        dirCreated &= GITLET_DIR.mkdir();
        dirCreated &= OBJECTS_DIR.mkdir();
        dirCreated &= REFS_DIR.mkdir();
        dirCreated &= HEADS_DIR.mkdir();
        checkCreatingDirectory(dirCreated);

        Commit initialCommit = new Commit("initial commit", null, new Date(0L), new TreeMap<>());
        String commitId = Utils.sha1(serialize(initialCommit));
        File commitFile = new File(OBJECTS_DIR, commitId);
        Utils.writeObject(commitFile, initialCommit);

        File masterBranchFile = new File(HEADS_DIR, "master");
        Utils.writeContents(masterBranchFile, commitId);

        String headContent = "ref: refs/heads/master";
        Utils.writeContents(HEAD_FILE, headContent);
    }

    public static void addFile(String fileName) {
        StagingArea stagingArea = StagingArea.load();
        Commit currentCommit = getCurrentCommit();

        File fileForAddition = join(CWD, fileName);
        checkFileExists(fileName);

        byte[] fileContent = readContents(fileForAddition);
        String blobId = sha1(fileContent);

        String trackedBlobId = currentCommit.getTrackedFiles().get(fileName);
        if (blobId.equals(trackedBlobId)) {
            stagingArea.clearRemoval(fileName);
            stagingArea.save();
            return;
        }

        File blobFile = join(OBJECTS_DIR, blobId);
        if (!blobFile.exists()) {
            Utils.writeContents(blobFile, fileContent);
        }

        stagingArea.add(fileName, blobId);
        stagingArea.save();
    }

    public static void commit(String message) {
        StagingArea stagingArea = StagingArea.load();
        checkStageEmpty(stagingArea);
        checkCommitMessage(message);

        Commit currentCommit = getCurrentCommit();
        TreeMap<String, String> newTrackFiles = new TreeMap<>(currentCommit.getTrackedFiles());

        for (String fileName : stagingArea.getFileForAddition().keySet()) {
            String blobId = stagingArea.getFileForAddition().get(fileName);
            newTrackFiles.put(fileName, blobId);
        }

        for (String fileName : stagingArea.getFileForRemoval()) {
            newTrackFiles.remove(fileName);
        }

        Commit newCommit = new Commit(message, getHeadCommitId(), new Date(), newTrackFiles);
        String newCommitId = Utils.sha1(serialize(newCommit));
        File newCommitFile = Utils.join(OBJECTS_DIR, newCommitId);
        Utils.writeObject(newCommitFile, newCommit);

        String headContent = Utils.readContentsAsString(HEAD_FILE);
        String branchPath = headContent.split(": ")[1];
        File branchFile = Utils.join(GITLET_DIR, branchPath);
        Utils.writeContents(branchFile, newCommitId);

        StagingArea.clear();
    }

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
            System.out.println("Merge: " + currentCommit.getParentId().substring(0, 7) + " " +
                    currentCommit.secondParentId.substring(0, 7));
        }
        System.out.println("Date: " + formatDate(currentCommit.getDate()));
        System.out.println(currentCommit.getMessage());
        System.out.println();
    }

    public static void globalLog() {
        List<String> objectFiles = Utils.plainFilenamesIn(OBJECTS_DIR);
        for (String fileName : objectFiles) {
            try {
                Commit commit = getCommitById(fileName);
                if (commit.getMessage() == null) { // Simple check if it's a valid commit
                    continue;
                }
                printLogMessage(fileName, commit);
            } catch (Exception e) {
                // This object is not a commit, so we ignore it.
            }
        }
    }

    public static void find(String commitMessage) {
        List<String> objectFiles = Utils.plainFilenamesIn(OBJECTS_DIR);
        boolean matchFound = false;
        for (String fileName : objectFiles) {
            try {
                Commit commit = getCommitById(fileName);
                if (commitMessage.equals(commit.getMessage())) { // Simple check for matching message
                    continue;
                }
                matchFound = true;
                System.out.println(fileName);
            } catch (Exception e) {
                // This object is not a commit, so we ignore it.
            }
        }

        if(!matchFound) {
            System.out.println("Found no commit with that message.");
        }
    }

    public static void remove(String fileName) {
        StagingArea stagingArea = StagingArea.load();
        Commit currentCommit = getCurrentCommit();

        boolean isTracked = currentCommit.getTrackedFiles().containsKey(fileName);
        boolean isStaged = stagingArea.getFileForAddition().containsKey(fileName);

        if (!isTracked && !isStaged) {
            messageAndExit("No reason to remove the file.");
        }

        if (isStaged) {
            stagingArea.unstage(fileName);
        }

        if (isTracked) {
            stagingArea.remove(fileName);
            File fileInCWD = join(CWD, fileName);
            if (fileInCWD.exists()) {
                Utils.restrictedDelete(fileName);
            }
        }

        stagingArea.save();
    }

    public static void checkOut(String ...args) {
        CheckOutCommand.execute(args);
    }
}


