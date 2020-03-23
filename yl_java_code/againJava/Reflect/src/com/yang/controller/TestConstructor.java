package com.yang.controller;

import com.yang.domain.Person;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class TestConstructor {
    public static void main(String[] args) throws Exception {
        Class personClass = Person.class;

        // 获取构造方法们
        Constructor[] constructors = personClass.getConstructors();
        Constructor constructor = personClass.getConstructor();

        Constructor[] declaredConstructors = personClass.getDeclaredConstructors();
        Constructor declaredConstructor = personClass.getDeclaredConstructor();

        // 构造方法一定和类名一致，唯一的区别就是 参数
        Constructor declaredConstructor1 = personClass.getDeclaredConstructor(String.class, int.class);
        System.out.println(declaredConstructor1);

        Constructor declaredConstructor2 = personClass.getDeclaredConstructor();
        System.out.println(declaredConstructor2);

        // 构造方法是用来创建对象的
        Object p1 = declaredConstructor1.newInstance("zhangzan", 10);
        System.out.println(p1);

        // 获取的 构造方法对象获取时用几个参数 ，创建对象的时候也就只能用几个参数
        Object p2 = declaredConstructor2.newInstance();
        System.out.println(p2);

        //很多时候我们只是想用空参构造方法创建对象
        // class对象帮我们简化了这个操作
        Object p3 = personClass.newInstance();
        System.out.println(p3);

        // 暴力反射
        constructor.setAccessible(true);
    }
}
