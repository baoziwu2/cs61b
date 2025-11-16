package byow.Core;

import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

import java.util.Arrays;
import java.util.Vector;

public class RoadConnector {
    // use prim for MST
    private static int distance(Room a, Room b) {
        int ax = a.x + a.width / 2;
        int ay = a.y + a.height / 2;
        int bx = b.x + b.width / 2;
        int by = b.y + b.height / 2;
        return Math.abs(ax - bx) + Math.abs(ay - by);
    }

    private void createCorridor(TETile[][] worldFrame, Room a, Room b) {
        // there should be walls around corridors
        int ax = a.x + a.width / 2;
        int ay = a.y + a.height / 2;
        int bx = b.x + b.width / 2;
        int by = b.y + b.height / 2;

        for (int x = Math.min(ax, bx); x <= Math.max(ax, bx); ++x) {
            worldFrame[x][ay] = Tileset.FLOOR;
        }
        for (int y = Math.min(ay, by); y <= Math.max(ay, by); ++y) {
            worldFrame[bx][y] = Tileset.FLOOR;
        }
    }

    public void connectRooms(TETile[][] worldFrame, Vector<Room> rooms) {
        int n = rooms.size();
        boolean[] inMST = new boolean[n];
        int[] minDist = new int[n];
        int[] parent = new int[n];

        Arrays.fill(minDist, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
        minDist[0] = 0;

        for (int count = 0; count < n - 1; count++) {
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (!inMST[i] && (u == -1 || minDist[i] < minDist[u])) {
                    u = i;
                }
            }

            inMST[u] = true;

            for (int v = 0; v < n; v++) {
                if (!inMST[v]) {
                    int dist = distance(rooms.get(u), rooms.get(v));
                    if (dist < minDist[v]) {
                        minDist[v] = dist;
                        parent[v] = u;
                    }
                }
            }
        }

        for (int i = 1; i < n; i++) {
            createCorridor(worldFrame, rooms.get(i), rooms.get(parent[i]));
        }

    }
}
