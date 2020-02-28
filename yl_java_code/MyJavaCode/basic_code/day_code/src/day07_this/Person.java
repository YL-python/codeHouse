package day07_this;

public class Person {
    String name;

    public void sayHello(String name){
        // 用this 关键字区别两个 name
        System.out.println(name + "你好，我是" + this.name);
    }
}
