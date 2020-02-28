package day05_lei;

/*
类不能直接使用  要创建一个对象
1.导包
import 包名.类名   // 在同一个包的文件可以不写导包语句

2.创建
类名 对象名 = new 类名称();

3.使用
3.1 使用成员变量：对象名.成员变量名
3.2 使用成员方法：对象名.成员方法名(参数)

*/

// 1 导包
import day05_lei.Student;

public class use_student {
    public static void main(String[] args) {
        // 2 创建对象
        Student stu1 = new Student();

        // 3 使用
        System.out.println(stu1.name);
        System.out.println(stu1.age);
        stu1.eat();
        stu1.sleep();
        stu1.study();

    }
}
