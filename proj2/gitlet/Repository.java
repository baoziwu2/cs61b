package gitlet;

import java.io.File;
import java.util.*;

import static gitlet.CheckOutCommand.validateNoUntrackedFilesWouldBeOverwritten;
import static gitlet.ErrorHandling.*;
import static gitlet.Utils.*;


/**
 * Represents a gitlet repository.
 * does at a high level.
 *
 * @author azbnbNotFound
 */
public class Repository {
    /**
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
        File commitFile = Utils.join(OBJECTS_DIR, commitId);
        Utils.writeObject(commitFile, initialCommit);

        File masterBranchFile = Utils.join(HEADS_DIR, "master");
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

        for (String fileName : stagingArea.getFilesForRemoval()) {
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

    public static void log() {
        Display.log();
    }

    public static void globalLog() {
        Display.globalLog();
    }

    public static void find(String commitMessage) {
        List<String> objectFiles = Utils.plainFilenamesIn(OBJECTS_DIR);
        boolean matchFound = false;
        for (String fileName : objectFiles) {
            try {
                Commit commit = getCommitById(fileName);
                if (commitMessage.equals(commit.getMessage())) {
                    matchFound = true;
                    System.out.println(fileName);
                }

            } catch (Exception e) {
                // This object is not a commit, so we ignore it.
            }
        }

        if (!matchFound) {
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

    public static void checkOut(String... args) {
        CheckOutCommand.execute(args);
    }

    public static void status() {
        Display.status();
    }

    public static void createBranch(String branchName) {
        checkBranchExist(branchName);
        String headCommitId = getHeadCommitId();
        File newBranchFile = Utils.join(HEADS_DIR, branchName);
        Utils.writeContents(newBranchFile, headCommitId);
    }

    public static void removeBranch(String branchName) {
        checkBranchNotExist(branchName);
        checkForSameBranch(branchName);
        File branchFile = Utils.join(HEADS_DIR, branchName);
        branchFile.delete();
    }

    public static void resetWorkspaceToCommit(Commit targetCommit) {
        Commit currentCommit = getCurrentCommit();

        Map<String, String> targetFiles = targetCommit.getTrackedFiles();
        Map<String, String> currentFiles = currentCommit.getTrackedFiles();

        for (Map.Entry<String, String> entry : targetFiles.entrySet()) {
            String fileName = entry.getKey();
            String blobId = entry.getValue();

            File blobFile = Utils.join(Repository.OBJECTS_DIR, blobId);
            byte[] fileContent = Utils.readContents(blobFile);
            File fileInCWD = Utils.join(Repository.CWD, fileName);
            Utils.writeContents(fileInCWD, fileContent);
        }

        for (String fileName : currentFiles.keySet()) {
            if (!targetFiles.containsKey(fileName)) {
                Utils.restrictedDelete(fileName);
            }
        }
    }

    public static void validateNoUntrackedFilesWouldBeOverwritten(Commit targetCommit) {
        Commit currentCommit = Repository.getCurrentCommit();

        List<String> untrackedFiles = new ArrayList<>();
        for (String fileName : Utils.plainFilenamesIn(Repository.CWD)) {
            boolean isTracked = currentCommit.getTrackedFiles().containsKey(fileName);
            boolean isStaged = StagingArea.load().getFileForAddition().containsKey(fileName);
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

    public static void reset(String commitId) {
        Commit targetCommit = getCommitById(commitId);
        if (targetCommit == null) {
            messageAndExit("No commit with that id exists.");
        }

        validateNoUntrackedFilesWouldBeOverwritten(targetCommit);

        resetWorkspaceToCommit(targetCommit);

        String headContent = Utils.readContentsAsString(HEAD_FILE);
        String branchPath = headContent.split(": ")[1];
        File branchFile = Utils.join(GITLET_DIR, branchPath);
        Utils.writeContents(branchFile, commitId);

        StagingArea.clear();
    }
}


