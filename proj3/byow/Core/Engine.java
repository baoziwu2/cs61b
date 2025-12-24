package byow.Core;

import byow.TileEngine.TERenderer;
import byow.TileEngine.TETile;
import edu.princeton.cs.introcs.StdDraw;

import java.awt.*;
import java.io.*;

public class Engine {
    /* Feel free to change the width and height. */
    public static final int WIDTH = 80;
    public static final int HEIGHT = 30;
    private static final String SAVE_FILE_NAME = "game_save.txt";
    TERenderer ter = new TERenderer();
    WorldGenerator worldGenerator;
    TETile[][] worldFrame;
    private Avatar avatar;

    private void saveGame() {
        try {
            FileOutputStream fos = new FileOutputStream(SAVE_FILE_NAME);
            ObjectOutputStream oos = new ObjectOutputStream(fos);

            oos.writeObject(worldFrame);
            oos.writeObject(avatar);

            oos.close();
            fos.close();
        } catch (IOException e) {
            System.out.println("Error saving game: " + e.getMessage());
        }
    }

    private void loadGame() {
        File file = new File(SAVE_FILE_NAME);
        if (!file.exists()) {
            return;
        }

        try {
            FileInputStream fis = new FileInputStream(SAVE_FILE_NAME);
            ObjectInputStream ois = new ObjectInputStream(fis);

            worldFrame = (TETile[][]) ois.readObject();
            avatar = (Avatar) ois.readObject();

            ois.close();
            fis.close();
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error loading game: " + e.getMessage());
        }
    }

    /**
     * Method used for exploring a fresh world. This method should handle all inputs,
     * including inputs from the main menu.
     */
    public void interactWithKeyboard() {
        ter.initialize(WIDTH, HEIGHT);

        processMenu();

        if (worldFrame != null) {
            gameLoop();
        }
    }

    private void processMenu() {
        boolean selected = false;
        while (!selected) {
            drawMenuFrame("CS61B: THE GAME", "New Game (N)", "Load Game (L)", "Quit (Q)");

            if (StdDraw.hasNextKeyTyped()) {
                char c = Character.toUpperCase(StdDraw.nextKeyTyped());
                switch (c) {
                    case 'N':
                        long seed = handleSeedInput();
                        WorldGenerator wg = new WorldGenerator(WIDTH, HEIGHT, seed);
                        worldFrame = wg.generateWorld();
                        initializeAvatar(worldFrame, wg);
                        selected = true;
                        break;
                    case 'L':
                        loadGame();
                        if (worldFrame != null && avatar != null) {
                            selected = true;
                        }
                        break;
                    case 'Q':
                        // saveGame();
                        selected = true;
                        // System.exit(0);
                        break;
                }
            }
        }
    }

    private long handleSeedInput() {
        String input = "";
        drawMenuFrame("Enter Seed (Press S to start):", input, "", ""); // 初始显示

        while (true) {
            if (StdDraw.hasNextKeyTyped()) {
                char c = Character.toUpperCase(StdDraw.nextKeyTyped());

                if (c == 'S') {
                    if (!input.isEmpty()) {
                        return Long.parseLong(input);
                    }
                } else if (Character.isDigit(c)) {
                    input += c;
                    drawMenuFrame("Enter Seed (Press S to start):", input, "", "");
                } else if (c == '\b') {
                    if (!input.isEmpty()) {
                        input = input.substring(0, input.length() - 1);
                        drawMenuFrame("Enter Seed (Press S to start):", input, "", "");
                    }
                }
            }
        }
    }

    private void gameLoop() {
        boolean gameOver = false;
        ter.renderFrame(worldFrame);

        while (!gameOver) {
            int mouseX = (int) StdDraw.mouseX();
            int mouseY = (int) StdDraw.mouseY();

            String hudText = "";
            if (mouseX < WIDTH && mouseY < HEIGHT && mouseX >= 0 && mouseY >= 0) {
                hudText = worldFrame[mouseX][mouseY].description();
            }
            ter.renderFrame(worldFrame);
            StdDraw.textLeft(1, HEIGHT - 1, hudText);
            StdDraw.show();

            if (StdDraw.hasNextKeyTyped()) {
                char c = Character.toUpperCase(StdDraw.nextKeyTyped());

                if (c == ':') {
                    while (!StdDraw.hasNextKeyTyped()) ;
                    if (Character.toUpperCase(StdDraw.nextKeyTyped()) == 'Q') {
                        saveGame();
                        return;
//                        System.exit(0);
                    }
                } else {
                    avatar.move(worldFrame, c);
                    ter.renderFrame(worldFrame);
                }
            }
        }
    }

    private void drawMenuFrame(String s1, String s2, String s3, String s4) {
        StdDraw.clear(Color.BLACK);
        StdDraw.setFont(new Font("Monaco", Font.BOLD, 30));
        StdDraw.setPenColor(Color.WHITE);
        StdDraw.text(WIDTH / 2.0, HEIGHT / 1.5, s1);
        StdDraw.text(WIDTH / 2.0, HEIGHT / 2.0, s2);
        StdDraw.text(WIDTH / 2.0, HEIGHT / 2.5, s3);
        StdDraw.text(WIDTH / 2.0, HEIGHT / 3.0, s4);
        StdDraw.show();
    }

    /**
     * Method used for autograding and testing your code. The input string will be a series
     * of characters (for example, "n123sswwdasdassadwas", "n123sss:q", "lwww". The engine should
     * behave exactly as if the user typed these characters into the engine using
     * interactWithKeyboard.
     * <p>
     * Recall that strings ending in ":q" should cause the game to quite save. For example,
     * if we do interactWithInputString("n123sss:q"), we expect the game to run the first
     * 7 commands (n123sss) and then quit and save. If we then do
     * interactWithInputString("l"), we should be back in the exact same state.
     * <p>
     * In other words, both of these calls:
     * - interactWithInputString("n123sss:q")
     * - interactWithInputString("lww")
     * <p>
     * should yield the exact same world state as:
     * - interactWithInputString("n123sssww")
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
                    initializeAvatar(worldFrame, worldGenerator);
                }
            } else {
                switch (c) {
                    case 'N':
                        gatheringSeed = true;
                        seedString.setLength(0);
                        break;
                    case 'L':
                        loadGame();
                        break;
                    case ':':
                        if (i + 1 < input.length() && input.charAt(i + 1) == 'Q') {
                            saveGame();
                            return worldFrame;
                        }
                        break;
                    case 'W':
                    case 'A':
                    case 'S':
                    case 'D':
                        if (worldFrame != null) {
                            move(worldFrame, c);
                        }
                        break;
                }
            }
        }

        return worldFrame;

    }

    private void initializeAvatar(TETile[][] worldFrame, WorldGenerator worldGenerator) {
        Room firstRoom = worldGenerator.rooms.get(0);
        int avatarX = firstRoom.x + firstRoom.width / 2;
        int avatarY = firstRoom.y + firstRoom.height / 2;

        avatar = new Avatar(avatarX, avatarY);
        worldFrame[avatarX][avatarY] = byow.TileEngine.Tileset.AVATAR;
    }

    private void move(TETile[][] worldFrame, char cmd) {
        if (avatar != null) {
            avatar.move(worldFrame, cmd);
        }
    }
}
