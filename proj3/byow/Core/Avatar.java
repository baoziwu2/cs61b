package byow.Core;

import byow.TileEngine.TETile;
import byow.TileEngine.Tileset;

import java.io.Serializable;

public class Avatar implements Serializable {
    private final TETile appearance;
    private int x;
    private int y;

    public Avatar(int startX, int startY) {
        this.x = startX;
        this.y = startY;
        this.appearance = Tileset.AVATAR;
    }

    public void initializeAvatar(TETile[][] world) {
        world[x][y] = this.appearance;
    }

    boolean isValidMove(TETile[][] world, int nextX, int nextY) {
        if (nextX < 0 || nextX >= world.length || nextY < 0 || nextY >= world[0].length) {
            return false;
        }
        if (world[nextX][nextY].description().equals(Tileset.WALL.description())) {
            return false;
        }
        return true;
    }

    public void move(TETile[][] world, char cmd) {
        int dx = 0;
        int dy = 0;

        switch (cmd) {
            case 'W':
                dy = 1;
                break;
            case 'S':
                dy = -1;
                break;
            case 'A':
                dx = -1;
                break;
            case 'D':
                dx = 1;
                break;
            default:
                return;
        }

        int nextX = x + dx;
        int nextY = y + dy;

        if (!isValidMove(world, nextX, nextY)) {
            return;
        }


        world[x][y] = Tileset.FLOOR;
        x = nextX;
        y = nextY;
        world[x][y] = this.appearance;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
}
