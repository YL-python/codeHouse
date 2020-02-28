package day05_lei;

public class use_student_canshu {
    public static void main(String[] args) {
        Student stu1 = new Student();
        stu1.name = "zhangsan";
        stu1.age = 18;
        print_stu(stu1);
    }

    public static void print_stu(Student stu){
        System.out.println(stu.name);
        System.out.println(stu.age);
    }
}
