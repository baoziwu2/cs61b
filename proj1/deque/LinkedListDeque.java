package deque;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class LinkedListDeque<T> implements Deque<T>, Iterable<T> {
    private class Node {
        T data;
        Node next;
        Node prev;

        Node(T data, Node prev, Node next) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }

        Node(T data) {
            this.data = data;
            prev = null;
            next = null;
        }
    }

    Node headSentinel; // complete loop linked list:
    int size;

    public LinkedListDeque() {
        headSentinel = new Node(null, null, null);
        headSentinel.next = headSentinel;
        headSentinel.prev = headSentinel;
        size = 0;
    }

    public void addFirst(T item) {
        Node temp = new Node(item, headSentinel, headSentinel.next);
        headSentinel.next.prev = temp;
        headSentinel.next = temp;
        size += 1;
    }

    public void addLast(T item) {
        Node temp = new Node(item, headSentinel.prev, headSentinel);
        headSentinel.prev.next = temp;
        headSentinel.prev = temp;
        size += 1;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void printDeque() {
        Node temp = headSentinel.next;
        while (temp != headSentinel) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public T removeFirst() {
        if (size == 0) {
            return null;
        }
        Node temp = headSentinel.next;
        headSentinel.next = temp.next;
        temp.next.prev = headSentinel;
        size -= 1;
        return temp.data;
    }

    public T removeLast() {
        if (size == 0) {
            return null;
        }
        Node temp = headSentinel.prev;
        headSentinel.prev = temp.prev;
        temp.prev.next = headSentinel;
        size -= 1;
        return temp.data;
    }

    public T get(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        Node p = headSentinel.next;
        for (int i = 0; i < index; ++i) {
            p = p.next;
        }
        return p.data;
    }

    public T getRecursive(int index) {
        class HelperFunction {
            public T get(Node currentNode, int index) {
                if (index == 0) {
                    return currentNode.data;
                }
                if (currentNode.next == headSentinel) {
                    return null;
                }
                return get(currentNode.next, index - 1);
            }
        }
        HelperFunction helper = new HelperFunction();
        return helper.get(headSentinel.next, index);
    }

    @Override
    public Iterator<T> iterator() {
        return new LinkedListDequeIterator();
    }

    public class LinkedListDequeIterator implements Iterator<T> {
        private Node currentNode;

        public LinkedListDequeIterator() {
            currentNode = headSentinel.next;
        }

        @Override
        public boolean hasNext() {
            return currentNode != headSentinel;
        }

        @Override
        public T next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            T item = currentNode.data;
            currentNode = currentNode.next;
            return item;
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

