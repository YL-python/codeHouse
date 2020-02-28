package code_Thread.day02Thread;

public class Person extends Thread{
    @Override
    public void run() {
        for(int i = 0; i<20;i++){
            System.out.println("run" + "--->" + i);
        }
    }
}
