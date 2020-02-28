package code_Thread.day10TheradPool;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class demo01 {
    public static void main(String[] args) {
        // 线程池接口的实现类对象
        ExecutorService es = Executors.newFixedThreadPool(2);
        es.submit(new RunnableImpl());
        es.submit(new RunnableImpl());
        es.submit(new RunnableImpl());
        es.shutdown();
    }
}
