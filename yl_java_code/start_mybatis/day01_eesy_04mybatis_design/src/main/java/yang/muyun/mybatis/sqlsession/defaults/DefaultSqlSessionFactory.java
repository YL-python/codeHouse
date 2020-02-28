package yang.muyun.mybatis.sqlsession.defaults;


import yang.muyun.mybatis.cfg.Configuration;
import yang.muyun.mybatis.sqlsession.SqlSession;
import yang.muyun.mybatis.sqlsession.SqlSessionFactory;

// SqlSessionFactory 接口的实现类
public class DefaultSqlSessionFactory implements SqlSessionFactory {

    private Configuration cfg;

    public DefaultSqlSessionFactory(Configuration cfg){
        this.cfg = cfg;
    }

    // 用于创建一个新的操作数据库对象
    public SqlSession openSession() {
        return new DefaultSqlSession(cfg);
    }
}
