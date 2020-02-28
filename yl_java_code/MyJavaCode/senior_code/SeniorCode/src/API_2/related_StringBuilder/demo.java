package API_2.related_StringBuilder;

public class demo {
    public static void main(String[] args) {
        StringBuilder bu1 = new StringBuilder();
        System.out.println(bu1);
        StringBuilder bu2 = new StringBuilder("abc");
        System.out.println(bu2);
        StringBuilder bu3 =  bu2.append(123);
        System.out.println(bu3);
        System.out.println(bu3 == bu2);
        bu3.append(123).append("def").append("你好");   // 链式编程

        String s = bu3.toString();
        System.out.println(s);

    }
}
