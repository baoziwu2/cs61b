package byow.Core;

import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

public class WallFiller {
    private boolean checkForAdjacentFloor(TETile[][] world, int x, int y) {
        return world[x][y] == Tileset.FLOOR;
    }

    public void wallFiller(TETile[][] world) {
        int width = world.length;
        int height = world[0].length;

        for (int x = 1; x < width - 1; ++x) {
            for (int y = 1; y < height - 1; ++y) {
                if (world[x][y] == Tileset.NOTHING) {
                    boolean adjacentToFloor = false;

                    // Check adjacent tiles
                    adjacentToFloor |= checkForAdjacentFloor(world, x + 1, y);
                    adjacentToFloor |= checkForAdjacentFloor(world, x - 1, y);
                    adjacentToFloor |= checkForAdjacentFloor(world, x, y + 1);
                    adjacentToFloor |= checkForAdjacentFloor(world, x, y - 1);

                    if (adjacentToFloor) {
                        world[x][y] = Tileset.WALL;
                    }
                }
            }
        }
    }
}
