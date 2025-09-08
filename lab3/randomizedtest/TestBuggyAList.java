package randomizedtest;

import edu.princeton.cs.algs4.StdRandom;
import org.junit.Test;
import timingtest.AList;

import java.util.Objects;

import static org.junit.Assert.*;

/**
 * Created by hug.
 */
public class TestBuggyAList {
    static void addLastInBothList(AListNoResizing<Integer> correctList, BuggyAList<Integer> testList, int x) {
        correctList.addLast(x);
        testList.addLast(x);
    }

    static void removeLastInBothList(AListNoResizing<Integer> correctList, BuggyAList<Integer> testList) {
        correctList.removeLast();
        testList.removeLast();
    }

    static boolean isSame(AListNoResizing<Integer> correctList, BuggyAList<Integer> testList) {
       if(correctList.size() != testList.size()) return false;
       for(int i = 0; i < correctList.size(); ++ i)
           if(!Objects.equals(correctList.get(i), testList.get(i)))
               return false;
       return true;
    }

    @Test
    public void testThreeAddThreeRemove() {
        int a = 4, b = 5, c = 6;
        AListNoResizing<Integer> correctList = new AListNoResizing<>();
        BuggyAList<Integer> testList = new BuggyAList<>();
        addLastInBothList(correctList, testList, a);
        addLastInBothList(correctList, testList, b);
        addLastInBothList(correctList, testList, c);

        for(int i = 1; i <= 3; ++ i) {
            removeLastInBothList(correctList, testList);
            assertTrue(isSame(correctList, testList));
        }
    }

    @Test
    public void randomizedTest() {
        AListNoResizing<Integer> correctList = new AListNoResizing<>();
        BuggyAList<Integer> testList = new BuggyAList<>();
//        AList<String> operationsLog = new AList<>();

        int N = 5000;
        for (int i = 0; i < N; i += 1) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                // addLast
                int randVal = StdRandom.uniform(0, 100);
                addLastInBothList(correctList, testList, randVal);
                assertTrue(isSame(correctList, testList));
//                System.out.println("addLast(" + randVal + ")");
            } else if (operationNumber == 1) {
                // size
                int size = correctList.size();
//                System.out.println("size: " + size);
            } else if (operationNumber == 2) {
                // getLast
                int sizeOnCorrectList = correctList.size(), sizeOnTestList = correctList.size();
                assertEquals(sizeOnCorrectList, sizeOnTestList);
                if(sizeOnCorrectList > 0) assertEquals(correctList.getLast(), testList.getLast());
//                if (sizeOnCorrectList > 0) System.out.println("getLast: " + correctList.getLast() + testList.getLast());
//                else System.out.println("the dockers are empty");
            } else {
                // removeLast
                int sizeOnCorrectList = correctList.size(), sizeOnTestList = correctList.size();
                assertEquals(sizeOnCorrectList, sizeOnTestList);
                if(sizeOnCorrectList > 0) assertEquals(correctList.removeLast(), testList.removeLast());
//                if (sizeOnCorrectList > 0) System.out.println("removeLast: " + correctList.removeLast() +  testList.removeLast());
//                else System.out.println("the dockers are empty");
            }
            assertTrue(isSame(correctList, testList));
        }
    }
}
