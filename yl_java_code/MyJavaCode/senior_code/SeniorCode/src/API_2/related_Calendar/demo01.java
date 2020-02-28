package API_2.related_Calendar;

import java.util.Calendar;
import java.util.Date;

public class demo01 {
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();
        System.out.println(c);

        demo_get();
        demo_set();
        dem0_getTime();
    }

    private static void dem0_getTime() {
        Calendar c = Calendar.getInstance();
        Date date = c.getTime();
        System.out.println(date);
    }

    private static void demo_set() {
        Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        c.set(Calendar.YEAR, 9999);
        System.out.println(c.get(Calendar.YEAR));
    }

    public  static void demo_get(){
        Calendar c = Calendar.getInstance();
        int year =  c.get(Calendar.YEAR); // 获取日历对象的某个字段信息
        System.out.println(year);
    }

}
