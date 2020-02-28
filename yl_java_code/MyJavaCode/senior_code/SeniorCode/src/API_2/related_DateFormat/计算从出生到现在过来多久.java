package API_2.related_DateFormat;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class 计算从出生到现在过来多久 {
    public static void main(String[] args) throws ParseException {
        /*
        获取当前时间戳
        获取出生的时间戳
        把时间戳的差转成日期
        */
        Date date = new Date();
        long nowTime = date.getTime();
        System.out.println(nowTime);
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date2 = sdf.parse("2000-04-12 00:00:00");
        Long csTime = date2.getTime();
        System.out.println(csTime);
        Long count = nowTime - csTime;
        int miao = (int) (count / 1000);
        int feng = (int) (miao / 60);
        int shi = (int) (feng / 60);
        int tian = (int) (shi / 24);
        int nian = (int) (tian / 365);
        System.out.print(nian + "年" );
        System.out.print(tian + "天" );
        System.out.print(shi + "小时" );
        System.out.print(feng + "分" );
        System.out.print(miao + "秒" );

    }
}
