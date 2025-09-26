package gitlet;

import java.io.Serializable;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

import static gitlet.Repository.STAGING_FILE;

public class StagingArea implements Serializable {
    Map<String, String> fileForAddition; // filename -> blobId
    Set<String> fileForRemove; // filename

    public StagingArea() {
        fileForAddition = new HashMap<>();
        fileForRemove = new HashSet<>();
    }

    public void clear() {
        fileForAddition.clear();
        fileForRemove.clear();
    }

    public void add(String fileName, String blobId) {
        fileForAddition.put(fileName, blobId);
        fileForRemove.remove(fileName);
    }

    public void clearRemoval(String fileName) {
        fileForRemove.remove(fileName); // cancel removal
    }

    public boolean isEmpty() {
        return fileForAddition.isEmpty() && fileForRemove.isEmpty();
    }

    public void unstage(String fileName) {
        fileForAddition.remove(fileName); // cancel addition
    }

    public void remove(String fileName) {
        fileForRemove.add(fileName); // update the removal set
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

    public Set<String> getFileForRemove() {
        return fileForRemove;
    }
}