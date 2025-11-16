package byow.Core;

import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

import java.util.Random;
import java.util.Vector;

import static byow.Core.RandomUtils.*;

public class RoomGenerator {
    private int WorldWidth;
    private int WorldHeight;
    TETile[][] worldFrame;

    private Random random;

    public RoomGenerator(int WorldWidth, int WorldHeight, long seed) {
        this.WorldWidth = WorldWidth;
        this.WorldHeight = WorldHeight;
        this.worldFrame = new TETile[WorldWidth][WorldHeight];
        initialize(seed);
    }

    private void initialize(long seed) {
        random = new Random(seed);
    }

    private boolean checkRoomOverlap(Room roomA) {
        for(int i = roomA.x; i < roomA.x + roomA.width; ++ i) {
            for(int j = roomA.y; j < roomA.y + roomA.height; ++ j) {
                if(worldFrame[i][j] != Tileset.NOTHING) {
                    return true;
                }
            }
        }
        return false;
    }

    public Room generateRoom() {
        int width = uniform(random, WorldWidth / 20, WorldWidth / 5);
        int height = uniform(random, WorldHeight / 20, WorldHeight / 5);
        int x = uniform(random, 0, WorldWidth - width);
        int y = uniform(random, 0, WorldHeight - height);
        Room newRoom = new Room(x, y, width, height);

        if(checkRoomOverlap(newRoom)) {
            return null;
        }

        for(int i = x; i < x + width; ++ i) {
            for (int j = y; j < y + height; ++ j) {
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
        WorldWidth = worldWidth;
        WorldHeight = worldHeight;
        this.worldFrame = worldFrame;
    }

    public Vector<Room> roomGenerate(int tryTimes) {
         Vector<Room> rooms = new Vector<>();
         while(tryTimes --> 0) {
             Room newRoom = generateRoom();
             if(newRoom != null) {
                rooms.add(newRoom);
             }
         }
         return rooms;
    }
}
