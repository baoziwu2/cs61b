package timingtest;

/** An SLList is a list of integers, which hides the terrible truth
 * of the nakedness within. */
public class SLList<Item> {
	private class IntNode {
		public Item item;
		public IntNode next;

		public IntNode(Item i, IntNode n) {
			item = i;
			next = n;
		}
	}

	/* The first item (if it exists) is at sentinel.next. */
	private IntNode sentinelHead;
    private IntNode tailElement;
	private int size;

	/** Creates an empty timingtest.SLList. */
	public SLList() {
		sentinelHead = new IntNode(null, null);
        tailElement = sentinelHead;
		size = 0;
	}

	public SLList(Item x) {
		sentinelHead = new IntNode(null, null);
		sentinelHead.next = new IntNode(x, null);
        tailElement = sentinelHead.next;
		size = 1;
	}

	/** Adds x to the front of the list. */
	public void addFirst(Item x) {
		sentinelHead.next = new IntNode(x, sentinelHead.next);
		size = size + 1;
	}

	/** Returns the first item in the list. */
	public Item getFirst() {
		return sentinelHead.next.item;
	}

	/** Adds x to the end of the list. */
	public void addLast(Item x) {
		IntNode p = tailElement;
        p.next = new IntNode(x, null);
        tailElement = tailElement.next;
        if(size ++ == 0) sentinelHead.next = tailElement;
	}

	/** returns last item in the list */
	public Item getLast() {
        return tailElement.item;
	}


	/** Returns the size of the list. */
	public int size() {
		return size;
	}

	public static void main(String[] args) {
		/* Creates a list of one integer, namely 10 */
		SLList L = new SLList();
		L.addLast(20);
		System.out.println(L.size());
	}
}
