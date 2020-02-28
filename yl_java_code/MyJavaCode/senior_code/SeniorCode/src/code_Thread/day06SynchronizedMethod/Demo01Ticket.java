package code_Thread.day06SynchronizedMethod;

public class Demo01Ticket {
    public static void main(String[] args) {
        SafeRannerabeImpl run = new SafeRannerabeImpl();
        Thread th01 = new Thread(run);
        Thread th02 = new Thread(run);
        Thread th03 = new Thread(run);
        th01.start();
        th02.start();
        th03.start();
    }
}
