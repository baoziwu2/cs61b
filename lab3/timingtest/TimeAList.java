package timingtest;
import edu.princeton.cs.algs4.Stopwatch;

import java.util.function.Predicate;

/**
 * Created by hug.
 */
public class TimeAList {
    private static final int MAX_OP_NUMBER = 128000;
    private static void printTimingTable(AList<Integer> Ns, AList<Double> times, AList<Integer> opCounts) {
        System.out.printf("%12s %12s %12s %12s\n", "N", "time (s)", "# ops", "microsec/op");
        System.out.printf("------------------------------------------------------------\n");
        for (int i = 0; i < Ns.size(); i += 1) {
            int N = Ns.get(i);
            double time = times.get(i);
            int opCount = opCounts.get(i);
            double timePerOp = time / opCount * 1e6;
            System.out.printf("%12d %12.2f %12d %12.2f\n", N, time, opCount, timePerOp);
        }
    }

    public static void main(String[] args) {
        timeAListConstruction();
    }

    public static void timeAListConstruction() {
        AList<Integer> listForTest = new AList<>(), opCountsForTest = new AList<>();
        AList<Double> timesForTest = new AList<>();
        Stopwatch stopwatch = new Stopwatch();

        Predicate<Integer> is2Power = (Integer p) -> {
            while(p != 1) {
                if ((p & 1) != 0) return false;
                p >>= 1;
            }
            return true;
        };

        for(int i = 1; i <= MAX_OP_NUMBER; ++ i) {
            listForTest.addLast(i);
            if(i % 1000 == 0 && is2Power.test(i / 1000)) {
                opCountsForTest.addLast(i);
                double time = stopwatch.elapsedTime();
                timesForTest.addLast(time);
            }
        }

        printTimingTable(opCountsForTest, timesForTest, opCountsForTest);
    }
}
