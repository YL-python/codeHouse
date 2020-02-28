package Set_code.related_Collection.day02_lterator;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;

public class demo01 {
    public static void main(String[] args) {
        // 创建集合对象
        Collection<String> coll = new ArrayList<>();
        // 添加元素
        coll.add("aaa");
        coll.add("BBB");
        coll.add("ccc");
        coll.add("111");
        coll.add("222");
        coll.add("333");
        System.out.println(coll);
        //  迭代器有泛型 和集合一致   获取迭代器
        Iterator<String> iter = coll.iterator();
        //迭代器的实现
        while (iter.hasNext()){
            String s = iter.next();
            System.out.println(s);
        }
        System.out.println(coll);

        // foreach
        for(String s: coll){
            System.out.println(s);
        }

    }
}
