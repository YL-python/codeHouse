package code_lambda.day01Runnable;

public class demoRunnable {
    public static void main(String[] args) {
        Runnable r1 = new RunnablmImpl();
        new Thread(r1).start();

        Runnable r2 = new Runnable() {
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+"线程开始启动");            }
        };
        new Thread(r2).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+"线程开始启动");            }
        }).start();
    }
}
