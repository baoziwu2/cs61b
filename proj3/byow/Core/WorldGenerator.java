package byow.Core;

import byow.TileEngine.TETile;

import java.util.Vector;

public class WorldGenerator {
    private final int WorldWidth;
    private final int WorldHeight;
    private final long Seed;

    TETile[][] worldFrame;
    Vector<Room> rooms;

    public WorldGenerator(int width, int height, long seed) {
        this.WorldWidth = width;
        this.WorldHeight = height;
        this.Seed = seed;
        this.worldFrame = new TETile[WorldWidth][WorldHeight];
    }

    public TETile[][] generateWorld() {
        for (int x = 0; x < WorldWidth; ++ x) {
            for (int y = 0; y < WorldHeight; ++ y) {
                worldFrame[x][y] = byow.TileEngine.Tileset.NOTHING;
            }
        }

        RoomGenerator roomGenerator = new RoomGenerator(WorldWidth, WorldHeight, Seed);
        RoadConnector roadConnector = new RoadConnector();
        WallFiller wallFiller = new WallFiller();

        roomGenerator.roomInit(Seed, WorldWidth, WorldHeight, worldFrame);
        int tryTimes = 200;
        rooms = roomGenerator.roomGenerate(tryTimes);
        roadConnector.connectRooms(worldFrame, rooms);
        wallFiller.wallFiller(worldFrame);
        return worldFrame;
    }
}
