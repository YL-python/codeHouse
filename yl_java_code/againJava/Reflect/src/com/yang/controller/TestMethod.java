package com.yang.controller;

import com.yang.domain.Person;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class TestMethod {
    public static void main(String[] args) throws Exception {
        Class personClass = Person.class;

        // 获取成员方法们
        // 获取到一个方法必须要有 方法名和参数列表
        Method[] methods = personClass.getMethods();
        Method method = personClass.getMethod("eat", String.class);

        Method[] declaredMethods = personClass.getDeclaredMethods();
        Method declaredMethod = personClass.getDeclaredMethod("eat", String.class);

        // 获取方法
        Method declaredMethod1 = personClass.getDeclaredMethod("eat", String.class);
        System.out.println(declaredMethod1);
        // 获取到方法之后我们的下一步操作 一般都是执行方法
        Person person = new Person();
        declaredMethod1.invoke(person, "苹果");

        Method declaredMethod2 = personClass.getDeclaredMethod("eat");
        System.out.println(declaredMethod2);
        declaredMethod2.invoke(person);

        System.out.println("===========================");

        // 获取所有public 修饰的方法
        Method[] methods1 = personClass.getMethods();
        for (Method method1 : methods1) {
            System.out.println(method1);
            // 获取方法名称
            String name = method1.getName();
            System.out.println(name);
        }

        // 暴力反射
        method.setAccessible(true);
    }
}
