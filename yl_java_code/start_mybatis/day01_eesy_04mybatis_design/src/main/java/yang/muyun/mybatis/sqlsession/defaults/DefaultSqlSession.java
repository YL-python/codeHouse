package yang.muyun.mybatis.sqlsession.defaults;

import yang.muyun.mybatis.cfg.Configuration;
import yang.muyun.mybatis.sqlsession.SqlSession;
import yang.muyun.mybatis.sqlsession.proxy.MapperProxy;
import yang.muyun.mybatis.utils.DataSourceUtil;

import java.lang.reflect.Proxy;
import java.sql.Connection;

// SqlSession 接口的实现类
public class DefaultSqlSession implements SqlSession {

    private Configuration cfg;
    private Connection connection;

    public DefaultSqlSession(Configuration cfg){
        this.cfg = cfg;
        connection = DataSourceUtil.getConnection(cfg);
    }

    // 创建代理对象
    public <T> T getMapper(Class<T> daoInterfaceClass) {
        return (T) Proxy.newProxyInstance(daoInterfaceClass.getClassLoader(),
                new Class[]{daoInterfaceClass},new MapperProxy(cfg.getMappers(), connection));
    }

    // 释放资源
    public void close() {
        if(connection != null) {
            try {
                connection.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
