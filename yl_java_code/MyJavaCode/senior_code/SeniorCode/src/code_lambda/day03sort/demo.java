package code_lambda.day03sort;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;

public class demo {
    public static void main(String[] args) {
        Person[] pers = {
          new Person("aaa",3),
          new Person("bbb",1),
          new Person("ccc",2)
        };
//        Arrays.sort(pers, new Comparator<Person>() {
//            @Override
//            public int compare(Person o1, Person o2) {
//                return o1.getAge() - o2.getAge();
//            }
//        });
        // 用lanbda 表达式
        Arrays.sort(pers, (Person o1, Person o2) -> {
                return o1.getAge() - o2.getAge();
            }
        );
        // 优化lambda表达式
        Arrays.sort(pers, (o1,o2) -> o1.getAge() - o2.getAge());

        for (Person per : pers) {
            System.out.println(per.toString());
        }
    }
}
