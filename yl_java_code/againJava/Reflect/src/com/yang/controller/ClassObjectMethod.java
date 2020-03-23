package com.yang.controller;

import com.yang.domain.Person;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class ClassObjectMethod {
    public static void main(String[] args) throws NoSuchFieldException, NoSuchMethodException {
        Class personClass = Person.class;

        // 获取成员变量们
        Field[] fields = personClass.getFields(); // 获取所有 public 修饰的成员变量
        Field age1 = personClass.getField("a");  // 获取对应名字 public 修饰的成员变量

        Field[] declaredFields = personClass.getDeclaredFields(); // 获取所有的成员变量
        for (Field i:declaredFields ) {
            System.out.println(i);
        }
        Field age = personClass.getDeclaredField("a"); // 获取对应名字的成员变量

        // 获取构造方法们
        Constructor[] constructors = personClass.getConstructors();
        Constructor constructor = personClass.getConstructor();

        Constructor[] declaredConstructors = personClass.getDeclaredConstructors();
        Constructor declaredConstructor = personClass.getDeclaredConstructor();

        // 获取成员方法们
        Method[] methods = personClass.getMethods();
        Method method = personClass.getMethod("eat");

        Method[] declaredMethods = personClass.getDeclaredMethods();
        Method declaredMethod = personClass.getDeclaredMethod("eat");

        // 获取类名
        String name = personClass.getName();
        System.out.println(name);

    }
}
