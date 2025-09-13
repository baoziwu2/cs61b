package deque;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class ArrayDeque<T> implements Deque<T>, Iterable<T> {
    private static final int INIT_LENGTH = 8;

    private int size;
    private int indexFront, indexLast; // 指针指向下一个元素放置的位置
    private T[] item;

    public ArrayDeque() {
        size = 0;
        item = (T[]) new Object[INIT_LENGTH];
        indexFront = INIT_LENGTH / 2;
        indexLast = indexFront + 1;
    }

    private int addInCircular(int pointer, int var) {
        if (pointer + var >= item.length) {
            pointer -= item.length;
        }
        return pointer + var;
    }

    private int subInCircular(int pointer, int var) {
        if (pointer - var < 0) {
            pointer += item.length;
        }
        return pointer - var;
    }

    public void addFirst(T var) {
        if (size == item.length) {
            resize(item.length << 1);
        }
        item[indexFront] = var;
        indexFront = subInCircular(indexFront, 1);
        size += 1;
    }

    public void addLast(T var) {
        if (size == item.length) {
            resize(item.length << 1);
        }
        item[indexLast] = var;
        indexLast = addInCircular(indexLast, 1);
        size += 1;
    }

    public T removeFirst() {
        if (size == 0) {
            return null;
        }
        size -= 1;
        indexFront = addInCircular(indexFront, 1);
        T temp = item[indexFront];
        if (size < item.length >> 2 && item.length > INIT_LENGTH) {
            resize(item.length >> 1);
        }
        return temp;
    }

    public T removeLast() {
        if (size == 0) {
            return null;
        }
        size -= 1;
        indexLast = subInCircular(indexLast, 1);
        T temp = item[indexLast];
        if (size < item.length >> 2 && item.length > INIT_LENGTH) {
            resize(item.length >> 1);
        }
        return temp;
    }

    public T get(int index) {
        if (index > size) {
            return null;
        }
        return item[addInCircular(indexFront, index + 1)];
    }

    public int size() {
        return size;
    }

    public void printDeque() {
        for (int i = addInCircular(indexFront, 1); i != indexLast; i = addInCircular(i, 1)) {
            System.out.println(item[i]);
        }
        System.out.println();
    }

    private void resize(int newSize) {
        T[] temp = (T[]) new Object[newSize];
        int current = addInCircular(indexFront, 1);

        for (int i = 0; i < size; ++i) {
            temp[i] = item[current];
            current = addInCircular(current, 1);
        }

        item = temp;

        indexFront = newSize - 1;
        indexLast = size;
    }

    @Override
    public Iterator<T> iterator() {
        return new ArrayDequeIterator();
    }

    private class ArrayDequeIterator implements Iterator<T> {
        private int currentPosition;

        ArrayDequeIterator() {
            currentPosition = addInCircular(indexFront, 1);
        }

        @Override
        public boolean hasNext() {
            return addInCircular(currentPosition, 1) != indexLast;
        }

        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T var = item[currentPosition];
            currentPosition = addInCircular(currentPosition, 1);
            return var;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Deque)) {
            return false;
        }
        if (size() != ((Deque<?>) o).size()) {
            return false;
        }
        for (int i = 0; i < size(); i++) { // Time Complexity high
            T left = (T) ((Deque<?>) o).get(i);
            T right = get(i);
            if (left == null && right == null) {
                continue;
            }
            if (left == null || right == null) {
                return false;
            }
            if (!(left.equals(right))) {
                return false;
            }
        }
        return true;
    }
}
