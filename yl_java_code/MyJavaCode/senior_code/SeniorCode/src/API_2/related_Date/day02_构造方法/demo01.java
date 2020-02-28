package API_2.related_Date.day02_构造方法;

        import java.util.Date;

public class demo01 {
    public static void main(String[] args) {
        demo01();  // 无参构造
        demo02();  // 有参构造
        demo03();  // 成员方法 获取时间戳

    }

    private static void demo03() {
        Date date = new Date();
        long time = date.getTime();
        System.out.println(time);
    }

    private static void demo02() {
        Date date = new Date(0L);
        System.out.println(date);
    }

    public static void demo01(){
        Date date = new Date();
        System.out.println(date);
    }
}
