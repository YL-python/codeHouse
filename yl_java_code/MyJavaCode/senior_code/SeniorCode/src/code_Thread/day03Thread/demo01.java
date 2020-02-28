package code_Thread.day03Thread;

public class demo01 {
    public static void main(String[] args) {
        RunnableImpl mt = new RunnableImpl();
        Thread t1 = new Thread(mt);
        t1.setName("xiaoxiao");
        t1.start();
        for(int i = 0; i<20;i++){
            System.out.println(Thread.currentThread().getName() + "--->" + i);
        }
    }
}
