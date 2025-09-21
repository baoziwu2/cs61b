package gitlet;

import java.io.File;

// handle the command check and error throw
public class CommandValidator {
    public static final File GITLET_DIR = new File(".gitlet");

    private static void messageAndExit(String message) {
        System.out.println(message);
        System.exit(0);
    }

    private static boolean validateForCheckOut(String[] args) {
        return false; // TODO
    }

    public static void validateArgs(StandardCommand command, String[] args) {
        int actualArgsLength = args.length - 1;
        if (command == StandardCommand.CHECKOUT) {
           if(validateForCheckOut(args)) {
               messageAndExit("Incorrect operands.");
           }
        }

        if (actualArgsLength != command.getStandardArgs()) {
            messageAndExit("Incorrect operands.");
        }
    }

    public static void validateInputEmpty(String[] args) {
        if(args.length == 0) {
            messageAndExit("Please enter a command.");
        }
    }

    public static StandardCommand validateCommandExists(String commandStr) { // after check argument
        try {
            String formattedCommandStr = commandStr.replace('-', '_').toUpperCase();
            return StandardCommand.valueOf(formattedCommandStr);
        } catch (IllegalArgumentException e) {
            messageAndExit("No command with that name exists.");
            return null;
        }
    }

    public static void validateRepoInitialized(StandardCommand command) {
        if(command == StandardCommand.INIT) {
            if (!GITLET_DIR.exists()) {
                messageAndExit("Not in an initialized Gitlet directory.");
            }
        }
    }
}
