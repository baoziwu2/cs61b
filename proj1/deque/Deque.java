package deque;

public interface Deque<T> extends Iterable<T> {
    void addFirst(T item);
    void addLast(T item);
    T removeFirst();
    T removeLast();
    void printDeque();
    int size();
    boolean isEmpty();
    T get(int index);

    @Override
    boolean equals(Object o);
}
