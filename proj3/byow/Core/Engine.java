package byow.Core;

import byow.TileEngine.TERenderer;
import byow.TileEngine.TETile;

public class Engine {
    TERenderer ter = new TERenderer();
    /* Feel free to change the width and height. */
    public static final int WIDTH = 80;
    public static final int HEIGHT = 30;



    /**
     * Method used for exploring a fresh world. This method should handle all inputs,
     * including inputs from the main menu.
     */
    public void interactWithKeyboard() {
    }

    /**
     * Method used for autograding and testing your code. The input string will be a series
     * of characters (for example, "n123sswwdasdassadwas", "n123sss:q", "lwww". The engine should
     * behave exactly as if the user typed these characters into the engine using
     * interactWithKeyboard.
     *
     * Recall that strings ending in ":q" should cause the game to quite save. For example,
     * if we do interactWithInputString("n123sss:q"), we expect the game to run the first
     * 7 commands (n123sss) and then quit and save. If we then do
     * interactWithInputString("l"), we should be back in the exact same state.
     *
     * In other words, both of these calls:
     *   - interactWithInputString("n123sss:q")
     *   - interactWithInputString("lww")
     *
     * should yield the exact same world state as:
     *   - interactWithInputString("n123sssww")
     *
     * @param input the input string to feed to your program
     * @return the 2D TETile[][] representing the state of the world
     */
    public TETile[][] interactWithInputString(String input) {
        // TODO: Fill out this method so that it run the engine using the input
        // passed in as an argument, and return a 2D tile representation of the
        // world that would have been drawn if the same inputs had been given
        // to interactWithKeyboard().
        //
        // See proj3.byow.InputDemo for a demo of how you can make a nice clean interface
        // that works for many different input types.
        // input will be like: N123253S, extract the number part for seed
        input = input.toUpperCase();
        long seed = 0;
        StringBuilder seedString = new StringBuilder();
        boolean gatheringSeed = false;

        WorldGenerator worldGenerator = null;
        TETile[][] worldFrame = null;

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (gatheringSeed) {
                if (Character.isDigit(c)) {
                    seedString.append(c);
                } else if (c == 'S') {
                    gatheringSeed = false;
                    seed = Long.parseLong(seedString.toString());
                    worldGenerator = new WorldGenerator(WIDTH, HEIGHT, seed);
                    worldFrame = worldGenerator.generateWorld();
                }
            } else {
                switch (c) {
                    case 'N':
                        gatheringSeed = true;
                        seedString.setLength(0);
                        break;
                    case 'L':
                        break;
                    case ':':
                        if (i + 1 < input.length() && input.charAt(i + 1) == 'Q') {
                            return worldFrame;
                        }
                        break;
                    case 'W':
                    case 'A':
                    case 'S':
                    case 'D':
                        if (worldFrame != null) {
                        }
                        break;
                }
            }
        }

        return worldFrame;

    }
}
