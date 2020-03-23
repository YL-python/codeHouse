package com.yang.controller;

import com.yang.domain.Person;

public class getClassObject {
    public static void main(String[] args) throws ClassNotFoundException {
        // 类加载器把 Java代码加载进内存生成 class类对象
        // class对象内把我们 写的Java代码的所有部分都封装成了对象

        // 获取class类对象的三种方法

        // 1 通过全类名
        Class class1 = Class.forName("com.yang.domain.Person");
        System.out.println(class1);


        // 2 类名.Class
        Class<Person> class2 = Person.class;
        System.out.println(class2);

        // 实例对象.getClass()
        Person person = new Person();
        Class class3 = person.getClass();
        System.out.println(class3);

        System.out.println(class1 == class2);  // true
        System.out.println(class1 == class3);  // true
    }
}
