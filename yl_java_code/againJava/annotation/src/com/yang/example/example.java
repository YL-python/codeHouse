package com.yang.example;

// 需求：写一个小框架，能创建任意对象并执行对象中的任意方法

import java.lang.reflect.Method;

@Pro(className = "com.yang.domain.Student",methodName = "eat")
public class example {
    public static void main(String[] args) throws Exception {

        // 1.1解析注解 从字节码文件中获取注解对象
        Class exampleClass = example.class;
        // 1.2获取注解对象实际上就是在内存中创建了一个 注解 接口子类 实现类对象
        Pro annotation = (Pro) exampleClass.getAnnotation(Pro.class);
        // 注解对象 调用注解中定义的 抽象方法 并获取返回值
        String className = annotation.className();
        String methodName = annotation.methodName();

        System.out.println(className);
        System.out.println(methodName);

        // 获取到全类名和方法名之后就简单了
        // 反射加载对象进内存
        Class cls = Class.forName(className);
        // 创建对象
        Object obj = cls.newInstance();
        // 获取方法对象
        Method method = cls.getMethod(methodName);
        // 对象执行方法
        method.invoke(obj);


        // 注解定义在方法上时
        // method.getAnnotation()
    }
}


/*
public class ProImpl implements Pro{
    @Override
    public String className() {
        return 注解使用时被附的值;
    }
    @Override
    public String methodName() {
        return 注解使用时被附的值;
    }
}
*/