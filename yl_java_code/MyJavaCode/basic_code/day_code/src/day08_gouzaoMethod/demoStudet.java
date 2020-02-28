package day08_gouzaoMethod;

public class demoStudet {
    public static void main(String[] args) {
        Student stu1 = new Student();
        System.out.println("============");

        Student stu2 = new Student("xiaohong", 18);
        System.out.println("名字：" + stu2.getName() + ",年龄" + stu2.getAge());

        // 修改参数的时候要用set方法
        stu2.setAge(21);
        System.out.println("名字：" + stu2.getName() + ",年龄" + stu2.getAge());
    }
}
