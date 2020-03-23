package com.yang.domain;

public class Person {

    // 成员变量
    private String name;
    private int age;

    public int a;
    protected int b;
    int c;
    private int d;


    // 构造方法
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Person() {
    }

    // 成员方法
    public void eat() {
        System.out.println("我在吃东西");
    }

    public void eat(String someting) {
        System.out.println("我在吃" + someting);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", a=" + a +
                ", b=" + b +
                ", c=" + c +
                ", d=" + d +
                '}';
    }
}
