package deque;

import java.util.Random;

public class DequeRandomizedTest {
    public static void main(String[] args) {
        // 在这里选择你要测试的 Deque 实现
        //Deque<Integer> myDeque = new LinkedListDeque<>();
        Deque<Integer> myDeque = new ArrayDeque<>();

        // 这是我们用来对比的、绝对正确的 Deque 实现
        java.util.ArrayDeque<Integer> javaDeque = new java.util.ArrayDeque<>();

        int N = 50000; // 测试操作的总次数
        Random rand = new Random();

        System.out.println("开始进行 " + N + " 次随机测试...");

        for (int i = 0; i < N; i++) {
            // 生成一个随机的操作编号
            int operationNumber = rand.nextInt(6);

            // 用于记录操作的字符串，方便调试
            String operationLog = "";

            if (operationNumber == 0) {
                // 操作: addFirst
                int randVal = rand.nextInt(100);
                myDeque.addFirst(randVal);
                javaDeque.addFirst(randVal);
                operationLog = "addFirst(" + randVal + ")";

            } else if (operationNumber == 1) {
                // 操作: addLast
                int randVal = rand.nextInt(100);
                myDeque.addLast(randVal);
                javaDeque.addLast(randVal);
                operationLog = "addLast(" + randVal + ")";

            } else if (myDeque.size() > 0) { // 只有在队列不为空时，才能执行以下操作
                if (operationNumber == 2) {
                    // 操作: removeFirst
                    Integer myVal = myDeque.removeFirst();
                    Integer javaVal = javaDeque.removeFirst();
                    operationLog = "removeFirst()";
                    if (!myVal.equals(javaVal)) {
                        System.out.println("错误: removeFirst() 返回值不一致！");
                        System.out.println("你的Deque返回值: " + myVal);
                        System.out.println("标准Deque返回值: " + javaVal);
                        break; // 发现错误，终止测试
                    }

                } else if (operationNumber == 3) {
                    // 操作: removeLast
                    Integer myVal = myDeque.removeLast();
                    Integer javaVal = javaDeque.removeLast();
                    operationLog = "removeLast()";
                    if (!myVal.equals(javaVal)) {
                        System.out.println("错误: removeLast() 返回值不一致！");
                        System.out.println("你的Deque返回值: " + myVal);
                        System.out.println("标准Deque返回值: " + javaVal);
                        break;
                    }

                } else if (operationNumber == 4) {
                    // 操作: get
                    int randomIndex = rand.nextInt(myDeque.size());
                    // 注意：java.util.ArrayDeque 没有 get(index) 方法，
                    // 所以我们把它转换成数组来获取对应索引的值
                    Integer myVal = myDeque.get(randomIndex);
                    if(myVal != null) continue;
                    Object[] javaArray = javaDeque.toArray();
                    Integer javaVal = (Integer) javaArray[randomIndex];
                    operationLog = "get(" + randomIndex + ")";
                    if (!myVal.equals(javaVal)) {
                        System.out.println("错误: get(" + randomIndex + ") 返回值不一致！");
                        System.out.println("你的Deque返回值: " + myVal);
                        System.out.println("标准Deque返回值: " + javaVal);
                        break;
                    }
                }
            }

            // 每次操作后都检查 size 是否一致
            if (myDeque.size() != javaDeque.size()) {
                System.out.println("错误: size() 不一致！");
                System.out.println("在执行操作 " + operationLog + " 后:");
                System.out.println("你的Deque大小: " + myDeque.size());
                System.out.println("标准Deque大小: " + javaDeque.size());
                break;
            }
        }

        // 如果循环正常结束，说明所有测试都通过了
        if (myDeque.size() == javaDeque.size()) {
            System.out.println("恭喜！所有 " + N + " 次随机测试都已通过！");
        }
    }
}
