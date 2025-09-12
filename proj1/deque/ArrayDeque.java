package deque;

public class ArrayDeque<typeName> implements Deque<typeName> {
    public static final int INIT_LENGTH = 8;

    private int size;
    private int indexFront, indexLast; // 指针指向下一个元素放置的位置
    private typeName[] item;

    ArrayDeque() {
        size = 0;
        item = (typeName[]) new Object[INIT_LENGTH];
        indexFront = INIT_LENGTH / 2;
        indexLast = indexFront + 1;
    }

    public int addInCircular(int pointer, int var) {
        if(pointer + var >= item.length) pointer -= item.length;
        return pointer + var;
    }

    public int subInCircular(int pointer, int var) {
        if(pointer - var < 0) pointer += item.length;
        return pointer - var;
    }

    public void addFirst(typeName var) {
        if(size == item.length) resize(item.length << 1);
        item[indexFront] = var;
        indexFront = subInCircular(indexFront, 1);
        size += 1;
    }

    public void addLast(typeName var) {
        if(size == item.length) resize(item.length << 1);
        item[indexLast] = var;
        indexLast = addInCircular(indexLast, 1);
        size += 1;
    }

    public typeName removeFirst() {
        size -= 1;
        indexFront = addInCircular(indexFront, 1);
        return item[indexFront];
    }

    public typeName removeLast() {
        size -= 1;
        indexLast = subInCircular(indexLast, 1);
        return item[indexLast];
    }

    public typeName get(int index) {
        if(index > size) return null;
        return item[addInCircular(indexFront, index + 1)];
    }

    public typeName front() {
        return item[addInCircular(indexFront, 1)];
    }

    public typeName back() {
        return item[subInCircular(indexLast, 1)];
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void printDeque() {
        for(int i = addInCircular(indexFront, 1); i != indexLast; i = addInCircular(i, 1)) {
            System.out.println(item[i]);
        }
        System.out.println();
    }

    public void resize(int newSize) {
        typeName[] temp = (typeName[]) new Object[newSize];
        int current = addInCircular(indexFront, 1);

        for (int i = 0; i < size; ++ i) {
            temp[i] = item[current];
            current = addInCircular(current, 1);
        }

        item = temp;

        indexFront = newSize - 1;
        indexLast = size;
    }
}
