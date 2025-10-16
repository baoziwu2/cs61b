package hashmap;

import java.util.Collection;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
/**
 *  A hash table-backed Map implementation. Provides amortized constant time
 *  access to elements via get(), remove(), and put() in the best case.
 *
 *  Assumes null keys will never be inserted, and does not resize down upon remove().
 *  @author YOUR NAME HERE
 */
public class MyHashMap<K, V> implements Map61B<K, V> {
    public double getLoadFactor() {
        return loadFactor;
    }

    /**
     * Protected helper class to store key/value pairs
     * The protected qualifier allows subclass access
     */
    protected class Node {
        K key;
        V value;

        Node(K k, V v) {
            key = k;
            value = v;
        }
    }

    private static final int INITIAL_MAX_CAPACITY = 16;
    private static final double INITIAL_LOAD_FACTOR = 0.75;
    /* Instance Variables */
    private Collection<Node>[] buckets;
    private int maxCapacity;
    private double loadFactor;
    private int size;
    // You should probably define some more!

    /** Constructors */
    public MyHashMap() {
        this(INITIAL_MAX_CAPACITY, INITIAL_LOAD_FACTOR);
    }

    public MyHashMap(int initialSize) {
        this(initialSize, INITIAL_LOAD_FACTOR);
    }

    /**
     * MyHashMap constructor that creates a backing array of initialSize.
     * The load factor (# items / # buckets) should always be <= loadFactor
     *
     * @param initialSize initial size of backing array
     * @param maxLoad maximum load factor
     */
    public MyHashMap(int initialSize, double maxLoad) {
        this.maxCapacity = initialSize;
        this.loadFactor = maxLoad;
        this.size = 0;
        this.buckets = createTable(initialSize);
    }

    /**
     * Returns a new node to be placed in a hash table bucket
     */
    private Node createNode(K key, V value) {
        return new Node(key, value);
    }

    /**
     * Returns a data structure to be a hash table bucket
     *
     * The only requirements of a hash table bucket are that we can:
     *  1. Insert items (`add` method)
     *  2. Remove items (`remove` method)
     *  3. Iterate through items (`iterator` method)
     *
     * Each of these methods is supported by java.util.Collection,
     * Most data structures in Java inherit from Collection, so we
     * can use almost any data structure as our buckets.
     *
     * Override this method to use different data structures as
     * the underlying bucket type
     *
     * BE SURE TO CALL THIS FACTORY METHOD INSTEAD OF CREATING YOUR
     * OWN BUCKET DATA STRUCTURES WITH THE NEW OPERATOR!
     */
    protected Collection<Node> createBucket() {
        return new java.util.LinkedList<Node>();
    }

    /**
     * Returns a table to back our hash table. As per the comment
     * above, this table can be an array of Collection objects
     *
     * BE SURE TO CALL THIS FACTORY METHOD WHEN CREATING A TABLE SO
     * THAT ALL BUCKET TYPES ARE OF JAVA.UTIL.COLLECTION
     *
     * @param tableSize the size of the table to create
     */
    private Collection<Node>[] createTable(int tableSize) {
        Collection<Node>[] table = new Collection[tableSize];
        for(int i = 0; i < tableSize; i++) {
            table[i] = createBucket();
        }
        return table;
    }

    private void resize(int capacity) {
        Collection<Node>[] newBuckets = createTable(capacity);
        for(Collection<Node> bucket : buckets) {
            if(bucket == null) continue;
            for(Node node : bucket) {
                int hashCode = node.key.hashCode();
                int bucketIndex = Math.floorMod(hashCode, newBuckets.length);
                if (newBuckets[bucketIndex] == null) {
                    newBuckets[bucketIndex] = createBucket();
                }
                newBuckets[bucketIndex].add(createNode(node.key, node.value));
            }
        }
        this.buckets = newBuckets;
        this.maxCapacity = capacity;
    }

    private void checkLoadFactorAndResize() {
        if ((double) size / buckets.length > loadFactor) {
            resize(buckets.length * 2);
        }
    }
    // TODO: Implement the methods of the Map61B Interface below
    // Your code won't compile until you do so!
    public void clear() {
        buckets = createTable(maxCapacity);
        size = 0;
    }

    public boolean containsKey(K key) {
        int hashCode = key.hashCode();
        int bucketIndex = Math.floorMod(hashCode, buckets.length);
        for(Node node : buckets[bucketIndex]) {
            if(node.key.equals(key)) {
                return true;
            }
        }
        return false;
    }

    public V get(K key) {
        int hashCode = key.hashCode();
        int bucketIndex = Math.floorMod(hashCode, buckets.length);
        if (buckets[bucketIndex] == null) {
            return null;
        }
        for (Node node : buckets[bucketIndex]) {
            if (node.key.equals(key)) {
                return node.value;
            }
        }
        return null;
    }

    public int size() {
        return size;
    }

    public void put(K key, V value) {
        checkLoadFactorAndResize();
        int hashCode = key.hashCode();
        int bucketIndex = Math.floorMod(hashCode, buckets.length);
        Collection<Node> bucket = buckets[bucketIndex];

        for (Node node : bucket) {
            if (node.key.equals(key)) {
                node.value = value;
                return ;
            }
        }
        bucket.add(createNode(key, value));
        size ++;
    }

    public Set<K> keySet() {
        Set<K> keys = new HashSet<>();
        for(Collection<Node> bucket : buckets) {
            if(bucket == null) continue;
            for(Node node : bucket) {
                keys.add(node.key);
            }
        }
        return keys;
    }

    public V remove(K key) {
        int hashCode = key.hashCode();
        int bucketIndex = Math.floorMod(hashCode, buckets.length);
        Collection<Node> bucket = buckets[bucketIndex];
        Iterator<Node> iterator = bucket.iterator();
        while(iterator.hasNext()) {
            Node node = iterator.next();
            if(node.key.equals(key)) {
                V val = node.value;
                iterator.remove();
                size --;
                return val;
            }
        }
        return null;
    }

    public V remove(K key, V value) {
        int hashCode = key.hashCode();
        int bucketIndex = Math.floorMod(hashCode, buckets.length);
        Collection<Node> bucket = buckets[bucketIndex];
        Iterator<Node> iterator = bucket.iterator();
        while(iterator.hasNext()) {
            Node node = iterator.next();
            if(node.key.equals(key) && node.value.equals(value)) {
                V val = node.value;
                iterator.remove();
                size --;
                return val;
            }
        }
        return null;
    }

    public Iterator<K> iterator() {
        Set<K> keys = new HashSet<>();
        for(Collection<Node> bucket : buckets) {
            if(bucket == null) continue;
            for(Node node : bucket) {
                keys.add(node.key);
            }
        }
        return keys.iterator();
    }
}
