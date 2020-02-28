package day08_gouzaoMethod;

public class Student {
    private String name;
    private int age;

    public Student(){
        System.out.println("这里是无参数的构造方法");
    }
    public Student(String name, int age){
        System.out.println("这里是有参数的构造方法");
        this.name = name;
        this.age = age;
    }

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;  // 没有重名参数不要用this 方法
    }
    public void setAge(int age){
        this.age = age;  // 有重名参数在用this 方法
    }
    public int getAge(){
        return age;
    }
}
