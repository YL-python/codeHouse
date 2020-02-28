package day06_fengzhuang;

/*
发现年龄可以传负数不合理，
采用 private 关键字对年龄变量修饰

private  修饰的变量在本类中可以随意访问，在别的类里面就不能访问了  能间接访问
*/

public class Person {

    String name;
    private int age;

    public void show(){
        System.out.println("show方法\n" + "名字是：" + name + "年龄是：" + age);
    }

    // 定义两个方法间接访问被保护的变量
    public void setAge(int num) {
        if(num < 100 && num >= 0){
            age = num;
        }else {
            System.out.println("数据不合理");
        }
    }
    public int getAge(){
        return age;
    }
}
