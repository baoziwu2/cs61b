package byow.Core;

import byow.TileEngine.TETile;

import java.util.Vector;

public class WorldGenerator {
    private final int worldWidth;
    private final int worldHeight;
    private final long seed;

    TETile[][] worldFrame;
    Vector<Room> rooms;

    public WorldGenerator(int width, int height, long seed) {
        this.worldWidth = width;
        this.worldHeight = height;
        this.seed = seed;
        this.worldFrame = new TETile[worldWidth][worldHeight];
    }

    public TETile[][] generateWorld() {
        for (int x = 0; x < worldWidth; ++x) {
            for (int y = 0; y < worldHeight; ++y) {
                worldFrame[x][y] = byow.TileEngine.Tileset.NOTHING;
            }
        }

        RoomGenerator roomGenerator = new RoomGenerator(worldWidth, worldHeight, seed);
        RoadConnector roadConnector = new RoadConnector();
        WallFiller wallFiller = new WallFiller();

        roomGenerator.roomInit(seed, worldWidth, worldHeight, worldFrame);
        int tryTimes = 200;
        rooms = roomGenerator.roomGenerate(tryTimes);
        roadConnector.connectRooms(worldFrame, rooms);
        wallFiller.wallFiller(worldFrame);
        return worldFrame;
    }
}
