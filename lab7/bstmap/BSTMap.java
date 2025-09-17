package bstmap;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Set;

public class BSTMap<K extends Comparable<K>, V> implements Map61B<K, V> {
    private BSTNode root;
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

    public int size(BSTNode node) {
        return node == null ? 0 : node.subTreeSize;
    }

    public void put(K key, V value) {
        if(key == null) throw new IllegalArgumentException("key cannot be null");
        root = put(key, value, root);
    }

    public BSTNode put(K key, V value, BSTNode node) {
        if(node == null) return new BSTNode(key, value);
        int cmp = key.compareTo(node.key);
        if(cmp < 0) node.leftSon = put(key, value, node.leftSon);
        else if(cmp > 0) node.rightSon = put(key, value, node.rightSon);
        else node.value = value;
        node.subTreeSize = size(node.leftSon) + size(node.rightSon) + 1;
        return node;
    }

    @Override
    public Set<K> keySet() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public V remove(K key) { // TODO
        throw new UnsupportedOperationException();
    }

    public V remove(K key, V value) { // TODO
        throw new UnsupportedOperationException();
    }

    @Override
    public Iterator<K> iterator() {
        return new IteratorOfKey(root);
    }

    private class IteratorOfKey implements Iterator<K> {
        private BSTNode node;
        public IteratorOfKey(BSTNode node) {
            this.node = node;
        }

        @Override
        public boolean hasNext() {
            return node != null;
        }

        public K next() {
            if(!hasNext()) throw new NoSuchElementException();
            throw new UnsupportedOperationException("Not supported yet."); // TODO
        }
    }
}
