package code_lambda.day01Runnable;

public class RunnablmImpl implements Runnable {
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName()+"线程开始启动");
    }
}
