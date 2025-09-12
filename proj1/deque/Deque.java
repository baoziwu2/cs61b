package deque;

public interface Deque<typeName> {
    void addFirst(typeName item);
    void addLast(typeName item);
    typeName removeFirst();
    typeName removeLast();
    void printDeque();
    int size();
    boolean isEmpty();
    typeName get(int index);
}
