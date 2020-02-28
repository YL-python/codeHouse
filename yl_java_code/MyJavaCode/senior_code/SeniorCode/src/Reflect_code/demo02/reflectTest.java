package Reflect_code.demo02;

/*
    不改变代码的前提下可以创建任意类对象并执行其中的方法
*/

import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.Properties;

public class reflectTest {
    public static void main(String[] args) throws Exception {
        // 1 加载配置文件
        // 1.1创建Properties对象
        Properties pro = new Properties();
        // 1.2加载配置文件，转换为一个集合
        // 1.2.1获取class目录下的配置文件
        ClassLoader classLoader = reflectTest.class.getClassLoader();
        InputStream is = classLoader.getResourceAsStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\Reflect_code\\demo02\\pro.properties");
        pro.load(is);

        // 2 获取配置文件的数据
        String classname = pro.getProperty("className");
        String methodname = pro.getProperty("methodName");

        // 3 加载该类进内存
        Class<?> cls = Class.forName(classname);
        // 4 创建对象
        Object obj = cls.newInstance();
        // 5 获取方法
        Method method = cls.getMethod(methodname);
        // 6 执行方法
        method.invoke(obj);

    }
}
