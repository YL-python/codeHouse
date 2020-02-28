package code_Thread.day08WaitNotify;

public class damo03WaitAndNotify {
    public static void main(String[] args) {
        // 保证锁对象唯一
        Object obj = new Object();
        // 创建顾客线程
        new Thread(){
            @Override
            public void run() {
                while (true){
                    synchronized (obj){
                        System.out.println("顾客一：我要XX包子XX个");
                        try {
                            obj.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println("顾客一被唤醒， 开始吃包子");
                        System.out.println("======================");
                    }
                }
            }
        }.start();
        new Thread(){
            @Override
            public void run() {
                while (true){
                    synchronized (obj){
                        System.out.println("顾客二：我要XX包子XX个");
                        try {
                            obj.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        System.out.println("顾客二被唤醒， 开始吃包子");
                        System.out.println("======================");
                    }
                }
            }
        }.start();
        // 创建老板线程
        new Thread(){
            @Override
            public void run() {
                while (true){
                    System.out.println("正在做包子，请等待");
                    try {
                        // 用一秒钟做包子
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    synchronized (obj){
                        System.out.println("做好包子了");
//                        obj.notify();
                        obj.notifyAll();
                    }
                }
            }
        }.start();
    }
}
