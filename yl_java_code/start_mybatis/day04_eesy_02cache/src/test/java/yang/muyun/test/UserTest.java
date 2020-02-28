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
import java.util.List;

public class UserTest {

    private InputStream in;
    private SqlSession session;
    private SqlSessionFactory factory;
    private UserDao userDao;

    @Before  // 用于在测试之前执行的代码
    public void init() throws IOException {
        // 1.读取配置文件
        in = Resources.getResourceAsStream("SqlMapConfig.xml");
        // 2.1使用构建者创建工厂对象 SqlSessionFactory
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        // 2.2使用 SqlSessionFactory 生产 SqlSession 对象
        factory = builder.build(in);
        // 3.使用工厂创建SqlSession对象
        session = factory.openSession(true);
        // 4.使用SqlSession创建Dao接口的代理对象
        userDao = session.getMapper(UserDao.class);
    }

    @After  // 在测试代码执行之后执行的
    public void destroy() throws IOException {
        // 提交事务
        // session.commit();  // 不然会回滚事务导致添加失败
        // 6.释放资源
        session.close();
        in.close();
    }

    @Test
    public void testFirstLevelCache() {
        // 测试一级缓存
        User user1 = userDao.findById(41);
        System.out.println(user1);
        User user2 = userDao.findById(41);
        System.out.println(user2);
        System.out.println(user1 == user2);

        // 关闭sqlSession  测试缓存
        User user3 = userDao.findById(41);
        System.out.println(user3);
        session.close();
        session = factory.openSession(true);
        userDao = session.getMapper(UserDao.class);
        User user4 = userDao.findById(41);
        System.out.println(user4);
        System.out.println(user3 == user4);

        // 手动清楚缓存
        session.clearCache();
    }

    @Test
    public void testClearCache() {
        // 查询 存入一级缓存
        User user1 = userDao.findById(41);
        System.out.println(user1);

        // 修改数据
        user1.setUsername("update user clear cache");
        user1.setAddress("北京 缓存");
        userDao.updateUser(user1);

        User user2 = userDao.findById(41);
        System.out.println(user2);

        System.out.println(user1 == user2);

        // sqlSession 对象调用修改，添加，删除，commit(),close()方法时会自动清空一级缓存

    }
}