package code_Thread.day08WaitNotify;

public class damo02WaitAndNotify {
    public static void main(String[] args) {
        // 保证锁对象唯一
        Object obj = new Object();
        // 创建顾客线程
        new Thread(){
            @Override
            public void run() {
                while (true){
                    synchronized (obj){
                        System.out.println("我要XX包子XX个");
                        try {
                            obj.wait(2000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println("顾客被唤醒， 开始吃包子");
                        System.out.println("======================");
                    }
                }
            }
        }.start();
        // wait()带参方法，没有被唤醒会自动醒
    }
}
