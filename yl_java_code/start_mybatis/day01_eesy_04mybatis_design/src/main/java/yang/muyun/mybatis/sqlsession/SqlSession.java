package yang.muyun.mybatis.sqlsession;

// 自定义  mybatis  中和数据库交互的核心类
// 可以创建dao接口的代理对象
public interface SqlSession {
    // 根据 dao的接口的字节码 创建一个代理对象
    <T> T getMapper(Class<T> daoInterfaceClass);

    // 释放资源
    void close();
}
