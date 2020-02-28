package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import yang.muyun.dao.RoleDao;
import yang.muyun.dao.UserDao;
import yang.muyun.domain.Role;
import yang.muyun.domain.User;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class RoleTest {

    private InputStream in;
    private SqlSession session;
    private RoleDao roleDao;

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
        roleDao = session.getMapper(RoleDao.class);
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
        List<Role> roles = roleDao.findAll();
        for(Role role : roles) {
            System.out.println("------每个角色的信息--------");
            System.out.println(role);
            System.out.println(role.getUsers());
        }
    }
}
