package com.yang.exampe;

// 需求：写一个小框架，能创建任意对象并执行对象中的任意方法

// 分析  把需要创建的对象和需要执行的方法写道一个配置文件中，我们的框架加载配置文件并执行方法

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.Properties;

public class example {
    public static void main(String[] args) throws Exception {
        // 创建类加载器对象
        ClassLoader classLoader = example.class.getClassLoader();
        InputStream is = classLoader.getResourceAsStream("config.properties");
        // 加载配置文件
        Properties properties = new Properties();
        properties.load(is);

        // 获取配置文件中的数据
        String className = properties.getProperty("className");
        String methodName = properties.getProperty("methodName");

        // 反射加载对象进内存
        Class cls = Class.forName(className);
        // 创建对象
        Object obj = cls.newInstance();
        // 获取方法对象
        Method method = cls.getMethod(methodName);
        // 对象执行方法
        method.invoke(obj);
    }
}
