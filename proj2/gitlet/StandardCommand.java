package gitlet;

public enum StandardCommand {
    INIT(1),
    ADD(2),
    COMMIT(2),
    RM(2),
    LOG(1),
    GLOBAL_LOG(1),
    FIND(2),
    STATUS(1),
    CHECKOUT(-1), // multi-able arguments
    BRANCH(2),
    RM_BRANCH(2),
    RESET(2),
    MERGE(2);

    private final int requiredArgs;

    StandardCommand(int numArgs) {
        this.requiredArgs = numArgs;
    }

    public int getStandardArgs() {
        return requiredArgs;
    }
}
