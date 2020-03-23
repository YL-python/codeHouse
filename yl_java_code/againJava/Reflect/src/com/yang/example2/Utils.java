package com.yang.example2;

import java.lang.reflect.Field;

public class Utils {
    public static void getAll(Object obj) throws IllegalAccessException {
        System.out.println(obj);
        // 获取字节码文件
        Class cls = obj.getClass();
        // 获取所有属性
        Field[] fields = cls.getDeclaredFields();
        // 获取属性的值我们需要知道属性值的类型是什么  使用getXXX方法获取值
        for (Field field : fields) {
            field.setAccessible(true); // 隐藏字段暴力反射
            String name = field.getName();  // 获取属性名称
            Object o = field.get(obj);  // 获取属性值
            System.out.println(name + "==>" + o);
        }
    }

    public static void getAllWithAnno(Object obj) throws IllegalAccessException {
        System.out.println(obj);
        // 获取字节码文件
        Class cls = obj.getClass();
        // 获取所有属性
        Field[] fields = cls.getDeclaredFields();
        // 获取属性的值我们需要知道属性值的类型是什么  使用getXXX方法获取值
        for (Field field : fields) {
            field.setAccessible(true); // 隐藏字段暴力反射
            // 有我们自定义注解的才获取值
            if (field.isAnnotationPresent(ylWrite.class)) {
                String name = field.getName();  // 获取属性名称
                Object o = field.get(obj);  // 获取属性值
                System.out.println(name + "==>" + o);
            }
        }
    }

    // 把一个字符串的第一个字母大写、效率是最高的
    private static String bigFirstWord(String word) throws Exception {
        byte[] items = word.getBytes();
        items[0] = (byte) ((char) items[0] - 'a' + 'A');
        return new String(items);
    }
}
