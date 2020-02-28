package code_Thread.day07Lock;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class SafeRannerabeImpl implements Runnable{
    private int ticket = 100;

    Lock l = new ReentrantLock();
    @Override
    public void run() {
        while (true){
            l.lock();
            if (ticket > 0){
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                ticket--;
            }
            l.unlock();
        }
    }

    public int getTicket() {
        return ticket;
    }

    public void setTicket(int ticket) {
        this.ticket = ticket;
    }
}
