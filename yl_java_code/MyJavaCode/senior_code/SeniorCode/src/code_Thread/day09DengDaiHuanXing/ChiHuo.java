package code_Thread.day09DengDaiHuanXing;

public class ChiHuo extends Thread {
    private BaoZi bz;

    public ChiHuo(BaoZi bz) {
        this.bz = bz;
    }

    @Override
    public void run() {
        int count = 0;
        while (true){
            synchronized (bz){
                if (bz.flag = false){
                    try {
                        bz.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.println("吃货正在吃"+bz.pi+bz.xian+"的包子"+count);
                bz.flag = false;
                bz.notify();
                System.out.println("吃货吃完了"+bz.pi+bz.xian+"包子，包子铺开始生成包子"+count);
                System.out.println("==========================");
                count++;
            }
        }
    }
}
