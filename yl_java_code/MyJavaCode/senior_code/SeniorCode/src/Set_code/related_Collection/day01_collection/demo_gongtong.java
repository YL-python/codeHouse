package Set_code.related_Collection.day01_collection;

import java.util.ArrayList;
import java.util.Collection;

// 共性方法

public class demo_gongtong {
    public static void main(String[] args) {
        // 接口指向实现类 多态
        Collection<String> coll = new ArrayList<>();
        System.out.println(coll);  // 结果不是地址就说明重写了toString方法

        System.out.println("===================");
        coll.add("yang");  // 返回值是true  一般不接收
        coll.add("long");
        coll.add("123");
        System.out.println(coll);

        System.out.println("===================");
        coll.remove("yang");
        coll.remove("666");
        System.out.println(coll);

        System.out.println("===================");
        System.out.println(coll.contains("yang"));
        System.out.println(coll.contains("long"));
        System.out.println(coll);

        System.out.println("===================");
        System.out.println(coll.isEmpty());
        System.out.println(coll);
        System.out.println("===================");
        System.out.println(coll.size());
        System.out.println(coll);
    }
}
