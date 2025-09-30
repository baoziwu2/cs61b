package gitlet;

import java.util.Arrays;

import static gitlet.ErrorHandling.messageAndExit;

/**
 * Driver class for Gitlet, a subset of the Git version-control system.
 *
 * @author azbnbnotfound
 */
public class Main {
    /**
     * Usage: java gitlet.Main ARGS, where ARGS contains
     * <COMMAND> <OPERAND1> <OPERAND2> ...
     */
    public static void main(String[] args) {
        CommandValidator.validateInputEmpty(args);
        StandardCommand command = CommandValidator.validateCommandExists(args[0]);
        CommandValidator.validateRepoInitialized(command);
        CommandValidator.validateArgs(command, args);

        switch (command) {
            case INIT:
                Repository.initRepository();
                break;
            case ADD:
                String fileNameToAdd = args[1];
                Repository.addFile(fileNameToAdd);
                break;
            case COMMIT:
                String commitMessage = args[1];
                Repository.commit(commitMessage);
                break;
            case LOG:
                Repository.log();
                break;
            case GLOBAL_LOG:
                Repository.globalLog();
                break;
            case FIND:
                Repository.find(args[1]);
                break;
            case CHECKOUT:
                String[] cmdArgs = Arrays.copyOfRange(args, 1, args.length);
                Repository.checkOut(cmdArgs);
                break;
            case BRANCH:
                Repository.createBranch(args[1]);
                break;
            case RM_BRANCH:
                Repository.removeBranch(args[1]);
                break;
            case STATUS:
                Repository.status();
                break;
            case RM:
                Repository.remove(args[1]);
                break;
            case RESET:
                Repository.reset(args[1]);
                break;
            case MERGE:
                messageAndExit("Not yet implemented.");
                break;
            default:
                messageAndExit("No command with that name exists.");
        }
    }
}
