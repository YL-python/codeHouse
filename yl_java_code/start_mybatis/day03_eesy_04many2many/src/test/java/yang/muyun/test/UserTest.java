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
    private UserDao userDao;

    @Before  // 用于在测试之前执行的代码
    public void init() throws IOException {
        // 1.读取配置文件
        in = Resources.getResourceAsStream("SqlMapConfig.xml");
        // 2.1使用构建者创建工厂对象 SqlSessionFactory
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        // 2.2使用 SqlSessionFactory 生产 SqlSession 对象
        SqlSessionFactory factory = builder.build(in);
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

    @Test  // 测试查询所有方法
    public void testFindAll(){
        // 5.使用代理对象执行方法
        List<User> users = userDao.findAll();
        for(User user : users) {
            System.out.println("-------------------");
            System.out.println(user);
            System.out.println(user.getRoles());
        }
    }

    @Test  // 测试查询一个方法
    public void testFindById(){
        // 5.使用代理对象执行方法
        User user = userDao.findById(46);
        System.out.println(user);
    }
}
