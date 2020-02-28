package code_Thread.day03lambdaThread;

public class demo01 {
    public static void main(String[] args) {

        new Thread(){
            @Override
            public void run() {
                for(int i = 0; i< 20;i++){
                    System.out.println(Thread.currentThread().getName()+"==>"+i);
                }
            }
        }.start();

        Runnable r = new Runnable() {
            @Override
            public void run() {
                for(int i = 0; i< 20;i++){
                    System.out.println(Thread.currentThread().getName()+"==>"+i);
                }
            }
        };
        new Thread(r).start();
    }
}
