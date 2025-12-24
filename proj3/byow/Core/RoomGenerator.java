package byow.Core;

import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

import java.util.Random;
import java.util.Vector;

import static byow.Core.RandomUtils.uniform;

public class RoomGenerator {
    TETile[][] worldFrame;
    private int worldWidth;
    private int worldHeight;
    private Random random;

    public RoomGenerator(int worldWidth, int worldHeight, long seed) {
        this.worldWidth = worldWidth;
        this.worldHeight = worldHeight;
        this.worldFrame = new TETile[worldWidth][worldHeight];
        initialize(seed);
    }

    private void initialize(long seed) {
        random = new Random(seed);
    }

    private boolean checkRoomOverlap(Room roomA) {
        for (int i = roomA.x; i < roomA.x + roomA.width; ++i) {
            for (int j = roomA.y; j < roomA.y + roomA.height; ++j) {
                if (worldFrame[i][j] != Tileset.NOTHING) {
                    return true;
                }
            }
        }
        return false;
    }

    public Room generateRoom() {
        int width = uniform(random, worldWidth / 20, worldWidth / 5);
        int height = uniform(random, worldHeight / 20, worldHeight / 5);
        int x = uniform(random, 0, worldWidth - width);
        int y = uniform(random, 0, worldHeight - height);
        Room newRoom = new Room(x, y, width, height);

        if (checkRoomOverlap(newRoom)) {
            return null;
        }

        for (int i = x; i < x + width; ++i) {
            for (int j = y; j < y + height; ++j) {
                if (i == x || i == x + width - 1 || j == y || j == y + height - 1) {
                    continue;
                } else {
                    worldFrame[i][j] = Tileset.FLOOR;
                }
            }
        }

        return newRoom;
    }

    public void roomInit(long seed, int worldWidth, int worldHeight, TETile[][] worldFrame) {
        initialize(seed);
        this.worldWidth = worldWidth;
        this.worldHeight = worldHeight;
        this.worldFrame = worldFrame;
    }

    public Vector<Room> roomGenerate(int tryTimes) {
        Vector<Room> rooms = new Vector<>();
        while (tryTimes-- > 0) {
            Room newRoom = generateRoom();
            if (newRoom != null) {
                rooms.add(newRoom);
            }
        }
        return rooms;
    }
}
