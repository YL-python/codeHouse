package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import yang.muyun.dao.UserDao;
import yang.muyun.domain.User;

import java.io.IOException;
import java.io.InputStream;

public class SecondLevelCacheTest {

    private InputStream in;
    private SqlSession session;
    private SqlSessionFactory factory;

    @Before  // 用于在测试之前执行的代码
    public void init() throws IOException {
        // 1.读取配置文件
        in = Resources.getResourceAsStream("SqlMapConfig.xml");
        // 2.1使用构建者创建工厂对象 SqlSessionFactory
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        // 2.2使用 SqlSessionFactory 生产 SqlSession 对象
        factory = builder.build(in);
    }

    @After  // 在测试代码执行之后执行的
    public void destroy() throws IOException {

    }

    @Test
    public void testSecondLevelCache() {
        SqlSession session1 = factory.openSession();
        UserDao dao1 = session1.getMapper(UserDao.class);
        User user1 = dao1.findById(41);
        System.out.println(user1);
        session1.close(); // 一级缓存消失


        SqlSession session2 = factory.openSession();
        UserDao dao2 = session2.getMapper(UserDao.class);
        User user2 = dao2.findById(41);
        System.out.println(user2);

        session2.close();
        System.out.println(user1 == user2);

        // 它指的是Mybatis中SqlSessionFactory对象的缓存。
        // 由同一个SqlSessionFactory对象创建的SqlSession共享其缓存
    }

}