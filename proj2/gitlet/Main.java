package gitlet;

/** Driver class for Gitlet, a subset of the Git version-control system.
 *  @author TODO
 */
public class Main {
    /** Usage: java gitlet.Main ARGS, where ARGS contains
     *  <COMMAND> <OPERAND1> <OPERAND2> ... 
     */
    public static void main(String[] args) {
        CommandValidator.validateInputEmpty(args);
        StandardCommand command = CommandValidator.validateCommandExists(args[0]);
        CommandValidator.validateRepoInitialized(command);
        CommandValidator.validateArgs(command, args);

        switch(command) {
            case INIT:
                // TODO: handle the `init` command
                break;
            case ADD:
                // TODO: handle the `add [filename]` command
                break;
            // TODO: FILL THE REST IN
        }
    }
}
