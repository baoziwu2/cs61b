class BreakContinue {
    public static void windowPosSum(int[] a, int n) {
        int[] prefixSum = new int[a.length + n];
        prefixSum[0] = a[0];
        for(int i = 1; i < a.length; ++ i)
            prefixSum[i] = prefixSum[i - 1] + a[i];
        for(int i = a.length; i < prefixSum.length; ++ i)
            prefixSum[i] = prefixSum[i - 1];

        a[0] = prefixSum[n];
        for(int i = 1; i < a.length; ++ i)
           if(a[i] >= 0)
               a[i] = prefixSum[i + n] - prefixSum[i - 1];
    }

    public static void main(String[] args){
        int[] a = {1, 2, -3, 4, 5, 4};
        int n = 3;
        windowPosSum(a, n);

        // Should print 4, 8, -3, 13, 9, 4
        System.out.println(java.util.Arrays.toString(a));
    }
}