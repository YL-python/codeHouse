package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import yang.muyun.dao.UserDao;
import yang.muyun.domain.User;

import java.io.InputStream;
import java.util.List;

public class MybatisTest {

    // 入门案例
    public static void main(String[] args) throws Exception {
        // 1.读取配置文件
        InputStream in = Resources.getResourceAsStream("SqlMapConfig.xml");
        // 2.1使用构建者创建工厂对象 SqlSessionFactory
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        // 2.2使用 SqlSessionFactory 生产 SqlSession 对象
        SqlSessionFactory factory = builder.build(in);
        // 3.使用工厂创建SqlSession对象
        SqlSession session = factory.openSession();
        // 4.使用SqlSession创建Dao接口的代理对象
        UserDao userDao = session.getMapper(UserDao.class);
        // 5.使用代理对象执行方法
        List<User> users = userDao.findAll();
        for(User user : users) {
            System.out.println(user);
        }
        // 6.释放资源
        session.close();
        in.close();
    }
}
