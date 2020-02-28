package code_Thread.day05Synchronized;

public class SafeRannerabeImpl implements Runnable{
    private int ticket = 100;

    // 定义一个任意对象
    Object obj = new Object();

    @Override
    public void run() {
        while (true){
            synchronized (obj){
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
        }
    }

    public int getTicket() {
        return ticket;
    }

    public void setTicket(int ticket) {
        this.ticket = ticket;
    }
}
