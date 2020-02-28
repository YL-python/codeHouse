package code_Thread.day10TheradPool;

public class RunnableImpl implements Runnable {
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName()+"创建新线程执行");
    }
}
