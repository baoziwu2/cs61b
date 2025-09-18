package bstmap;

import edu.princeton.cs.algs4.BST;
import org.w3c.dom.Node;

import java.util.*;

public class BSTMap<K extends Comparable<K>, V> implements Map61B<K, V> {
    private BSTNode root;
    private HashSet<K> keySet = new HashSet<>();

    private class BSTNode {
        K key;
        V value;
        BSTNode leftSon, rightSon;
        int subTreeSize;

        public BSTNode(K key, V value) {
            this.key = key;
            this.value = value;
            subTreeSize = 1;
            leftSon = null; rightSon = null;
        }
    }

    public void clear() {
        root = null;
    }

    public boolean containsKey(K key) {
        if(key == null) throw new IllegalArgumentException("key cannot be null");
        return containsKey(key, root) != null;
    }

    private K containsKey(K key, BSTNode node) {
        if(node == null) return null;
        int cmp = key.compareTo(node.key);
        if(cmp < 0) return containsKey(key, node.leftSon);
        if(cmp > 0) return containsKey(key, node.rightSon);
        return node.key;
    }

    public V get(K key) {
        if(key == null) throw new IllegalArgumentException("key cannot be null");
        return get(key, root);
    }

    private V get(K key, BSTNode node) {
        if(node == null) return null;
        int cmp = key.compareTo(node.key);
        if(cmp < 0) return get(key, node.leftSon);
        if(cmp > 0) return get(key, node.rightSon);
        return node.value;
    }

    public int size() {
        if(root == null) return 0;
        return root.subTreeSize;
    }

    private int size(BSTNode node) {
        return node == null ? 0 : node.subTreeSize;
    }

    public void put(K key, V value) {
        if(key == null) throw new IllegalArgumentException("key cannot be null");
        root = put(key, value, root);
        keySet.add(key);
    }

    private BSTNode put(K key, V value, BSTNode node) {
        if(node == null) return new BSTNode(key, value);
        int cmp = key.compareTo(node.key);
        if(cmp < 0) node.leftSon = put(key, value, node.leftSon);
        else if(cmp > 0) node.rightSon = put(key, value, node.rightSon);
        else node.value = value;
        sizeUpate(node);
        return node;
    }

    private void sizeUpate(BSTNode node) {
        node.subTreeSize = size(node.leftSon) + size(node.rightSon) + 1;
    }

    @Override
    public Set<K> keySet() {
       return keySet;
    }

    public V remove(K key) {
        if(key == null) throw new IllegalArgumentException("key cannot be null");
        V value = get(key);
        if(value == null) return null;
        keySet.remove(key);
        root = remove(key, root);
        return value;
    }

    public V remove(K key, V value){
        if (key == null) throw new IllegalArgumentException("key cannot be null");
        V valueInMap = get(key);
        if (valueInMap == null || !valueInMap.equals(value)) {
            return null;
        }
        return remove(key);
    }

    private BSTNode remove(K key, BSTNode node) {
        if(node == null) return null;
        int cmp = key.compareTo(node.key);
        if(cmp  < 0) node.leftSon = remove(key, node.leftSon);
        else if(cmp > 0) node.rightSon = remove(key, node.rightSon);
        else {
            if(node.leftSon == null) return node.rightSon;
            if(node.rightSon == null) return node.leftSon;

            BSTNode tempNode = node;
            node = searchMinNode(tempNode.rightSon);
            node.rightSon = removeMin(tempNode.rightSon);
            node.leftSon = tempNode.leftSon;
        }
        sizeUpate(node);
        return node;
    }

    private BSTNode searchMinNode(BSTNode node) {
        if(node.leftSon == null) return node;
        return searchMinNode(node.leftSon);
    }

    private BSTNode removeMin(BSTNode node) {
        if(node.leftSon == null) return node.rightSon;
        node.leftSon = removeMin(node.leftSon);
        sizeUpate(node);
        return node;
    }

    @Override
    public Iterator<K> iterator() {
        return new IteratorOfKey(root);
    }

    private class IteratorOfKey implements Iterator<K> {
        private Stack<BSTNode> stack;

        public IteratorOfKey(BSTNode root) {
            stack = new Stack<>();
            pushLeft(root);
        }

        private void pushLeft(BSTNode node) {
            while (node != null) {
                stack.push(node);
                node = node.leftSon;
            }
        }

        @Override
        public boolean hasNext() {
            return !stack.isEmpty();
        }

        @Override
        public K next() {
            if (!hasNext()) {
                throw new NoSuchElementException("The map has no more elements.");
            }
            BSTNode nextNode = stack.pop();
            K keyToReturn = nextNode.key;

            if (nextNode.rightSon != null) {
                pushLeft(nextNode.rightSon);
            }

            return keyToReturn;
        }
    }

    public void printInOrder() {
        System.out.println("Printing BSTMap in order:");
        for (K key : this) {
            System.out.println("key: " + key + ", value: " + get(key));
        }
    }
}
