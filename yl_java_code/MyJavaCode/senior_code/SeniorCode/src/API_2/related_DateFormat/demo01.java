package API_2.related_DateFormat;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class demo01 {
    public static void main(String[] args) throws ParseException {
        demo01();  // 格式化
        demo02();  // 解析
    }

    private static void demo02() throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date =  sdf.parse("2019-09-28 14:34:00");
        System.out.println(date);
        System.out.println(date.getTime());
    }

        public static void demo01(){
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        // 传时间戳返回格式化的时间  String
        Date date =  new Date();
        System.out.println(date.getTime());  // 1569652440583
        String Time = sdf.format(date.getTime());
        System.out.println(Time);  // 2019-09-28 14:34:00
    }
}
