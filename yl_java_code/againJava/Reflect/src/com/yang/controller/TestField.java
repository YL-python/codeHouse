package com.yang.controller;

import com.yang.domain.Person;

import java.lang.reflect.Field;

public class TestField {
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        Class personClass = Person.class;

        // 获取成员变量们
        Field[] fields = personClass.getFields(); // 获取所有 public 修饰的成员变量
        Field age1 = personClass.getField("a");  // 获取对应名字 public 修饰的成员变量

        Field[] declaredFields = personClass.getDeclaredFields(); // 获取所有的成员变量
        Field age = personClass.getDeclaredField("a"); // 获取对应名字的成员变量

        Person person = new Person();

        // 获取到成员变量对象之后可以对齐进行  get  set操作
        Field a = personClass.getDeclaredField("a");
        Integer value = (Integer) a.get(person);
        System.out.println(value);
        a.set(person, 100);
        System.out.println(person);

        // 访问修饰符不是public 的 成员变量时  会报 非法访问
        Field d = personClass.getDeclaredField("d");

        // 忽略访问权限修饰符的安全检查
        d.setAccessible(true);  // 暴力反射
        d.set(person, 120);
        System.out.println(person);
    }
}
