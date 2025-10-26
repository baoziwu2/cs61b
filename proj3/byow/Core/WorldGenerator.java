package byow.Core;

import byow.TileEngine.TETile;

import java.util.Vector;

public class WorldGenerator {
    private final static int WorldWidth = 400;
    private final static int WorldHeight = 400;
    private final static int tryTimes = 200;

    static TETile[][] worldFrame = new TETile[WorldWidth][WorldHeight];
    static Vector<Room> rooms;

    public static TETile[][] generateWorld(long seed) {
        for (int x = 0; x < WorldWidth; ++ x) {
            for (int y = 0; y < WorldHeight; ++ y) {
                worldFrame[x][y] = byow.TileEngine.Tileset.NOTHING;
            }
        }

        RoomGenerator.roomInit(seed, WorldWidth, WorldHeight, worldFrame);

        rooms = RoomGenerator.roomGenerate(tryTimes);

        RoadConector.connectRooms(worldFrame, rooms);
        WallFiller.wallFiller(worldFrame);
        return worldFrame;
    }
}
