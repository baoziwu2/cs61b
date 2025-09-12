package deque;

import java.util.Comparator;

public class MaxArrayDeque<T> extends ArrayDeque<T> {

    private Comparator<T> comparator;

    public MaxArrayDeque(Comparator<T> c) {
        super();
        this.comparator = c;
    }

    public T max(Comparator<T> cmp) {
        if (isEmpty()) {
            return null;
        }

        T maxSoFar = get(0);
        for (int i = 1; i < size(); i++) {
            T currentItem = get(i);
            if (cmp.compare(currentItem, maxSoFar) > 0) {
                maxSoFar = currentItem;
            }
        }
        return maxSoFar;
    }

    public T max() {
        return max(comparator);
    }
}
