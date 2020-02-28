package code_Thread.Threadname;

public class demo01getname {
    public static void main(String[] args) {

        System.out.println(Thread.currentThread().getName());// 获取主线程的名字
        MyThread mt1 = new MyThread();
        mt1.start();


        MyThread mt2 = new MyThread();
        mt2.setName("xiaoxiao");
        mt2.start();

        MyThread mt3 = new MyThread("dada");
        mt3.start();

    }
}
