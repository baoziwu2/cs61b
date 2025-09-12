package deque;

public interface Deque<T> {
    void addFirst(T item);
    void addLast(T item);
    T removeFirst();
    T removeLast();
    void printDeque();
    int size();
    T get(int index);
    default boolean isEmpty() {
        return size() == 0;
    }
}
