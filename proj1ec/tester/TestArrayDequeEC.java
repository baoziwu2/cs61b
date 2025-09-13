package tester;

import org.junit.Test;
import static org.junit.Assert.*;

import student.StudentArrayDeque;

import edu.princeton.cs.algs4.StdRandom;

public class TestArrayDequeEC {
    @Test
    public void randomizedTest() {
        StudentArrayDeque<Integer> studentDeque = new StudentArrayDeque<>();
        ArrayDequeSolution<Integer> solutionDeque = new ArrayDequeSolution<>();

        StringBuilder failureSequence = new StringBuilder();
        int roundNumber = 50000;

        for (int i = 0; i < roundNumber; i++) {
            int operation = StdRandom.uniform(0, 4);

            if (solutionDeque.isEmpty()) {
                int randVal = StdRandom.uniform(0, 100);
                if (StdRandom.bernoulli()) { // bernoulli() gives a 50/50 chance
                    studentDeque.addFirst(randVal);
                    solutionDeque.addFirst(randVal);
                    failureSequence.append("addFirst(").append(randVal).append(")\n");
                } else {
                    studentDeque.addLast(randVal);
                    solutionDeque.addLast(randVal);
                    failureSequence.append("addLast(").append(randVal).append(")\n");
                }
            } else {
                // Deque is not empty, can perform any operation
                Integer studentVal, solutionVal;
                int randVal;
                switch (operation) {
                    case 0: // addFirst
                        randVal = StdRandom.uniform(0, 100);
                        studentDeque.addFirst(randVal);
                        solutionDeque.addFirst(randVal);
                        failureSequence.append("addFirst(").append(randVal).append(")\n");
                        break;

                    case 1: // addLast
                        randVal = StdRandom.uniform(0, 100);
                        studentDeque.addLast(randVal);
                        solutionDeque.addLast(randVal);
                        failureSequence.append("addLast(").append(randVal).append(")\n");
                        break;

                    case 2: // removeFirst
                        studentVal = studentDeque.removeFirst();
                        solutionVal = solutionDeque.removeFirst();
                        failureSequence.append("removeFirst()\n");
                        assertEquals(failureSequence.toString(), solutionVal, studentVal);
                        break;

                    case 3: // removeLast
                        studentVal = studentDeque.removeLast();
                        solutionVal = solutionDeque.removeLast();
                        failureSequence.append("removeLast()\n");
                        assertEquals(failureSequence.toString(), solutionVal, studentVal);
                        break;
                }
            }
        }
    }
}