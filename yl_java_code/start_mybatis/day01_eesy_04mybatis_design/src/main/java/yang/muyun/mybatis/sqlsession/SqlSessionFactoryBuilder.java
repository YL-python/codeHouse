package yang.muyun.mybatis.sqlsession;

import yang.muyun.mybatis.cfg.Configuration;
import yang.muyun.mybatis.sqlsession.defaults.DefaultSqlSessionFactory;
import yang.muyun.mybatis.utils.XMLConfigBuilder;

import java.io.InputStream;

// 用于创建一个SqlSessionFactory 对象
public class SqlSessionFactoryBuilder {

    // 根据 参数字节流 来构建一个SqlSessionFactory工厂
    public SqlSessionFactory build(InputStream config){
        Configuration cfg = XMLConfigBuilder.loadConfiguration(config);
        return new DefaultSqlSessionFactory(cfg);
    }
}
