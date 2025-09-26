package gitlet;

import java.io.Serializable;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static gitlet.Repository.STAGING_FILE;

public class StagingArea implements Serializable {
    Map<String, String> fileForAddition; // filename -> blobId
    Set<String> fileForRemoval; // filename

    public StagingArea() {
        fileForAddition = new HashMap<>();
        fileForRemoval = new HashSet<>();
    }

    public static void clear() {
        StagingArea emptyArea = new StagingArea();
        emptyArea.save();
    }

    public void add(String fileName, String blobId) {
        fileForAddition.put(fileName, blobId);
        fileForRemoval.remove(fileName);
    }

    public void clearRemoval(String fileName) {
        fileForRemoval.remove(fileName); // cancel removal
    }

    public boolean isEmpty() {
        return fileForAddition.isEmpty() && fileForRemoval.isEmpty();
    }

    public void unstage(String fileName) {
        fileForAddition.remove(fileName); // cancel addition
    }

    public void remove(String fileName) {
        fileForRemoval.add(fileName); // update the removal set
    }

    public static StagingArea load() {
        try {
            if (STAGING_FILE.exists() && STAGING_FILE.isFile()) {
                StagingArea sa = Utils.readObject(STAGING_FILE, StagingArea.class);
                return sa != null ? sa : new StagingArea();
            }
        } catch (RuntimeException e) {

        }
        return new StagingArea();
    }

    public void save() {
        Utils.writeObject(STAGING_FILE, this);
    }

    public Map<String, String> getFileForAddition() {
        return fileForAddition;
    }

    public Set<String> getFileForRemoval() {
        return fileForRemoval;
    }
}