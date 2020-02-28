package code_Thread.Threadname;

public class MyThread extends Thread {
    public MyThread(String name) {
        super(name);
    }

    public MyThread() {
    }

    @Override
    public void run() {
        System.out.println("=================");
        System.out.println(Thread.currentThread().getName());
    }
}
