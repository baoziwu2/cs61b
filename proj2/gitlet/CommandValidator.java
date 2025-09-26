package gitlet;

import java.io.File;
import static gitlet.ErrorHandling.*;

// handle the command check and error throw
public class CommandValidator {
    public static final File GITLET_DIR = new File(".gitlet");

    private static boolean validateForCheckOut(String[] args) {
        boolean valid = false;
        if(args.length == 2) {
            valid = true;
        } else if(args.length == 3) {
            valid = args[1].equals("--");
        } else if(args.length == 4) {
            valid = args[2].equals("--");
        }
        return valid;
    }

    public static void validateArgs(StandardCommand command, String[] args) {
        if (command == StandardCommand.CHECKOUT) {
           if(!validateForCheckOut(args)) {
               messageAndExit("Incorrect operands.");
           }
           return ;
        }

        if (args.length != command.getStandardArgs()) {
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
        if(command != StandardCommand.INIT && !GITLET_DIR.exists()) {
            messageAndExit("Not in an initialized Gitlet directory.");
        }
    }
}
