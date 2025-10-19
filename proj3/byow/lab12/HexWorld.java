package byow.lab12;
import org.junit.Test;

import static byow.lab12.RandomWorldDemo.randomTile;
import static org.junit.Assert.*;

import byow.TileEngine.TERenderer;
import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

import java.util.Random;

/**
 * Draws a world consisting of hexagonal regions.
 */
public class HexWorld {
    static Random RANDOM = new Random(42);

    public static void drawHexagon(TETile[][] world, Hexagon hex, TETile tile) {
        Point p = hex.getPoint();
        int s = hex.sizeLength;
        drawHexagon(world, p, s, tile);
    }

    public static void drawHexagon(TETile[][] world, Point p, int s, TETile tile) {
        int x = p.x();
        int y = p.y();
        drawHexagon(world, x, y, s, tile);
    }

    public static void drawHexagon(TETile[][] world, int x, int y, int s, TETile tile) {
        int height = 2 * s;
        for (int i = 0; i < height; ++i) {
            int rowY = y + i;
            int rowWidth = s + 2 * Math.min(i, height - i - 1);
            int rowXStart = x - Math.min(i, height - i - 1);
            for (int j = 0; j < rowWidth; ++j) {
                world[rowXStart + j][rowY] = tile;
            }
        }
    }

    private static TETile randomTile() {
        int tileNum = RANDOM.nextInt(7);
        switch (tileNum) {
            case 0: return Tileset.WALL;
            case 1: return Tileset.FLOWER;
            case 2: return Tileset.GRASS;
            case 3: return Tileset.WATER;
            case 4: return Tileset.SAND;
            case 5: return Tileset.MOUNTAIN;
            case 6: return Tileset.TREE;
            default: return Tileset.NOTHING;
        }
    }

    public static void main(String[] args) {
        final int WIDTH = 100;
        final int HEIGHT = 100;

        TERenderer ter = new TERenderer();
        ter.initialize(WIDTH, HEIGHT);

        TETile[][] world = new TETile[WIDTH][HEIGHT];
        for (int x = 0; x < WIDTH; ++ x) {
            for (int y = 0; y < HEIGHT; ++ y) {
                world[x][y] = Tileset.NOTHING;
            }
        }

        Hexagon headHex = new Hexagon(30, 30, 3); // starting hexagon
        for(int i = 0; i < 5; ++ i) {
            Hexagon pointerHex = headHex;
            for(int j = 0; j < 3 + Math.min(i, 4 - i); ++ j) { // 3 4 5 4 3 hexagons in each column
                pointerHex = new Hexagon(pointerHex.getTop(3), 3);
                drawHexagon(world, pointerHex, randomTile());
            }
            if(i < 2) headHex = new Hexagon(headHex.getDownRight(3), 3);
            else headHex = new Hexagon(headHex.getUpRight(3), 3);
        }

        ter.renderFrame(world);
    }
}
