package code_Thread.day06SynchronizedMethod;

public class SafeRannerabeImpl implements Runnable{
    private int ticket = 100;

    @Override
    public void run() {
        while (true){
            maipiao();
        }
    }

    public synchronized void maipiao(){
        if (ticket > 0){
            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
            ticket--;
        }
    }

    public int getTicket() {
        return ticket;
    }

    public void setTicket(int ticket) {
        this.ticket = ticket;
    }
}
