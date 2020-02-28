package day05_lei;

public class use_student_return {
    public static void main(String[] args) {
        Student stu1 = new Student();
        stu1 = set_stu(stu1);
        System.out.println(stu1.name);
        System.out.println(stu1.age);

    }
    public static Student set_stu(Student stu){
        stu.name = "zhangsooooan";
        stu.age = 19;
        return stu;
    }
}
