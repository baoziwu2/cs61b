package gitlet;

// TODO: any imports you need here

import java.io.Serializable;
import java.util.Date; // TODO: You'll likely use this in this class
import java.util.Map;
import java.util.TreeMap;

/** Represents a gitlet commit object.
 *  TODO: It's a good idea to give a description here of what else this Class
 *  does at a high level.
 *
 *  @author TODO
 */
public class Commit implements Serializable {
    /**
     *
     * List all instance variables of the Commit class here with a useful
     * comment above them describing what that variable represents and how that
     * variable is used. We've provided one example for `message`.
     */

    /** The message of this Commit. */
    private String message;
    private Date date;
    String parentId;
    String secondParentId; // for merge commit
    TreeMap<String, String> trackedFiles = new TreeMap<>(); // Key "FileName". Value "SHA-1 ID"

    public Commit(String message, String parentId, Date date, TreeMap<String, String> trackedFiles) {
        this.message = message;
        this.date = date;
        this.parentId = parentId;
        this.secondParentId = null;
        this.trackedFiles = trackedFiles;
    }

    // getters
    public String getMessage() {
        return message;
    }

    public Date getDate() {
        return date;
    }

    public boolean isMergeCommit() {
        return secondParentId != null;
    }

    public String getParentId() {
        return parentId;
    }

    public Map<String, String> getTrackedFiles() {
        return trackedFiles;
    }
}
