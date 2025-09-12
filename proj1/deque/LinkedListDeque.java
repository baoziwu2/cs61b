package deque;

public class LinkedListDeque<typeName> implements Deque<typeName> {
    private class Node {
        typeName data;
        Node next;
        Node prev;

        Node(typeName data, Node prev, Node next) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }

        Node(typeName data) {
            this.data = data;
            this.next = this.prev = null;
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

    public void addFirst(typeName item) {
        Node temp = new Node(item, headSentinel, headSentinel.next);
        headSentinel.next.prev = temp;
        headSentinel.next = temp;
        size += 1;
    }

    public void addLast(typeName item) {
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
        while(temp != headSentinel) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public typeName removeFirst() {
        if(size == 0) return null;
        Node temp = headSentinel.next;
        headSentinel.next = temp.next;
        temp.next.prev = headSentinel;
        size -= 1;
        return temp.data;
    }

    public typeName removeLast() {
        if(size == 0) return null;
        Node temp = headSentinel.prev;
        headSentinel.prev = temp.prev;
        temp.prev.next = headSentinel;
        size -= 1;
        return temp.data;
    }

    public typeName get(int index) {
        if (index < 0 || index >= size) return null;
        Node p = headSentinel.next;
        for (int i = 0; i < index; i++) p = p.next;
        return p.data;
    }

    public typeName getRecursive(int index) {
        class HelperFunction {
            public typeName get(Node currentNode, int index) {
                if(index == 0) return currentNode.data;
                if(currentNode.next == headSentinel) return null;
                return get(currentNode.next, index - 1);
            }
        }
        HelperFunction helper = new  HelperFunction();
        return helper.get(headSentinel.next, index);
    }
}

