package yang.muyun.mybatis.io;


import java.io.InputStream;

// 使用类加载器读取配置文件
public class Resources {

    // 根据传入的参数获取字节输入流
    public static InputStream getResourceAsStream(String filePath){
        return Resources.class.getClassLoader().getResourceAsStream(filePath);
    }
}
