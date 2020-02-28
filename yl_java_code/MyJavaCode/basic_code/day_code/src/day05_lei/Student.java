package day05_lei;

/*

定义学生类
成员变量：名字，年龄
成员方法：吃，睡，学习   成员方法没有  static关键字
    public void eat() {}
    public void sleep() {}
    public void study() {}

*/

public class Student {
    //成员变量
    String name;  // 变量在类中不在方法中
    int age;

    // 成员方法   没有static
    public void eat() {
        System.out.println("吃饭。。。");
    }

    public void sleep(){
        System.out.println("睡觉。。。");
    }

    public void study(){
        System.out.println("学习。。。");
    }

}
