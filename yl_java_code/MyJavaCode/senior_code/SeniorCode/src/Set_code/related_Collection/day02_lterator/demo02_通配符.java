package Set_code.related_Collection.day02_lterator;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class demo02_通配符 {
    public static void main(String[] args) {
        ArrayList<String> list01 = new ArrayList<>();
        list01.add("aaa");
        list01.add("bbb");
        list01.add("ccc");
        ArrayList<Integer> list02 = new ArrayList<>();
        list02.add(1);
        list02.add(2);
        list02.add(3);
        printlist(list01);
        System.out.println("==============");
        printlist(list02);
    }

    public static void printlist(ArrayList<?> list) {
        Iterator<?> it = list.iterator();
        while (it.hasNext()){
            Object o = it.next();
            System.out.println(o);
        }

        for (Object o :list){
            System.out.println(o);
        }

    }
}
