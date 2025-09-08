package timingtest;
import edu.princeton.cs.algs4.Stopwatch;
import net.sf.saxon.om.Item;

import java.util.function.Predicate;

/**
 * Created by hug.
 */
public class TimeSLList {
    private static final int MAX_OP_NUMBER = 128000;
    private static final int OP_NUMBER = 10000;

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
        timeGetLast();
    }

    public static void addLastUntil(int x, SLList<Integer> list) {
        while(list.size() < x) list.addLast(5);
    }

    public static double getTimeAfterOperator(SLList<Integer> list) {
        Stopwatch stopWatch = new Stopwatch();
        for(int i = 0; i < OP_NUMBER; ++ i)
            list.getLast();
        return stopWatch.elapsedTime();
    }

    public static void timeGetLast() {
        AList<Integer> testNumberInDocker = new AList<>(), testOpNumberInDocker = new AList<>();
        AList<Double> testTimes = new AList<>();
        SLList<Integer> testDocker = new SLList<>();

        Predicate<Integer> is2Power = (Integer p) -> {
           return p == (p & -p);
        };

        for(int i = 1; i <= MAX_OP_NUMBER; ++ i) {
            if(i % 1000 == 0 && is2Power.test(i / 1000)) {
                testNumberInDocker.addLast(i);
                testOpNumberInDocker.addLast(OP_NUMBER);
                addLastUntil(i, testDocker);
                double time = getTimeAfterOperator(testDocker);
                testTimes.addLast(time);
            }
        }

        printTimingTable(testNumberInDocker, testTimes, testOpNumberInDocker);
    }

}
