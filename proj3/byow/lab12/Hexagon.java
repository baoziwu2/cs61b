package byow.lab12;


public class Hexagon {
    Point point;
    int sizeLength;

    public Hexagon(int x, int y, int sizeLength) {
        point = new Point(x, y);
        this.sizeLength = sizeLength;
    }

    public Hexagon(Point point, int sizeLength) {
        this.point = point;
        this.sizeLength = sizeLength;
    }

    public Point getPoint() {
        return point;
    }

    public Point getUpRight(int s) {
        int newX = point.x() + 2 * s - 1;
        int newY = point.y() + s;
        return new Point(newX, newY);
    }

    public Point getDownRight(int s) {
        int newX = point.x() + 2 * s - 1;
        int newY = point.y() - s;
        return new Point(newX, newY);
    }

    public Point getLeftRight(int s) {
        int newX = point.x() - 2 * s + 1;
        int newY = point.y() + s;
        return new Point(newX, newY);
    }

    public Point getDownLeft(int s) {
        int newX = point.x() - 2 * s + 1;
        int newY = point.y() - s;
        return new Point(newX, newY);
    }

    public Point getTop(int s) {
        int newX = point.x();
        int newY = point.y() + 2 * s;
        return new Point(newX, newY);
    }

    public Point getBottom(int s) {
        int newX = point.x();
        int newY = point.y() - 2 * s;
        return new Point(newX, newY);
    }
}
