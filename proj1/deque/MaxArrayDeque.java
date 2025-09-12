package deque;
import java.util.Comparator;

public class MaxArrayDeque<typeName> extends ArrayDeque<typeName> {

    private Comparator<typeName> comparator;

    public MaxArrayDeque(Comparator<typeName> c) {
        super();
        this.comparator = c;
    }

    public typeName max(Comparator<typeName> cmp) {
        if(isEmpty()) {
            return null;
        }

        typeName maxSoFar = get(0);
        for (int i = 1; i < size(); i++) {
            typeName currentItem = get(i);
            if (cmp.compare(currentItem, maxSoFar) > 0) {
                maxSoFar = currentItem;
            }
        }
        return maxSoFar;
    }

    public typeName max() {
        return max(comparator);
    }
}
