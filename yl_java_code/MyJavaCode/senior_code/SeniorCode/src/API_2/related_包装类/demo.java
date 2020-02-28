package API_2.related_包装类;

public class demo {
    public static void main(String[] args) {
        // 装箱
        Integer in1 = new Integer(123);
        System.out.println(in1);
        Integer in2 = new Integer("123456");
        System.out.println(in2);

        Integer in3 = Integer.valueOf(2131231);
        System.out.println(in3);
        Integer in4 = Integer.valueOf("2131231");
        System.out.println(in4);

        // 拆箱
        int i = in1.intValue();
        System.out.println(i);

        // 自动包装和拆箱
        Integer in5 = 3;
        in5 = in5 + 5;
        System.out.println(in5);
    }
}
