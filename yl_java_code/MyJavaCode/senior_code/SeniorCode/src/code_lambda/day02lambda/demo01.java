package code_lambda.day02lambda;

public class demo01 {
    public static void main(String[] args) {
        // 匿名内部类
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName() + "线程开始启动");
            }
        }).start();

        // lambda表达式
        new Thread(() -> {
                System.out.println(Thread.currentThread().getName() + "线程开始启动");
            }
        ).start();
    }
}
