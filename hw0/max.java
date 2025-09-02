public class max {
    public static int max(int[] a) {
        int maxNum = Integer.MIN_VALUE;
        for (int i = 0; i < a.length; ++ i)
            if (a[i] > maxNum)
                maxNum = a[i];
        return maxNum;
    }

    public static void main(String[] args) {
        int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6};
    }
}