package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import yang.muyun.dao.UserDao;
import yang.muyun.dao.impl.UserDaoImpl;
import yang.muyun.domain.User;

import java.io.IOException;
import java.io.InputStream;
import java.util.Date;
import java.util.List;

public class MybatisTest {

    private InputStream in;
    private UserDao userDao;

    @Before  // 用于在测试之前执行的代码
    public void init() throws IOException {
        // 1.读取配置文件
        in = Resources.getResourceAsStream("SqlMapConfig.xml");
        // 2.1使用构建者创建工厂对象 SqlSessionFactory
        SqlSessionFactoryBuilder builder = new SqlSessionFactoryBuilder();
        // 2.2使用 SqlSessionFactory 生产 SqlSession 对象
        SqlSessionFactory factory = builder.build(in);
        // 3.使用工厂创建 UserDao对象
        userDao = new UserDaoImpl(factory);
    }

    @After
    public void destroy() throws IOException {
        in.close();
    }

    @Test  // 测试查询所有方法
    public void testFindAll(){
        // 5.使用代理对象执行方法
        List<User> users = userDao.findAll();
        for(User user : users) {
            System.out.println(user);
        }
    }

    @Test  // 测试添加方法
    public void testSaveUser(){
        User user = new User();
        user.setAddress("江西南昌");
        user.setBirthday(new Date());
        user.setSex("男");
        user.setUsername("mybatis saveUser");
        System.out.println("保存操作之前："+user);
        // 5.使用代理对象执行方法
        userDao.saveUser(user); // 需要回滚事务
        System.out.println("保存操作之后："+user);
    }

    @Test  // 测试更新数据方法
    public void testUpdateUser(){
        User user = new User();
        user.setId(63);
        user.setAddress("111111");
        user.setBirthday(new Date());
        user.setSex("女");
        user.setUsername("userdaoimpl updateUser");
        // 5.使用代理对象执行方法
        userDao.updateUser(user);
    }

    @Test  // 测试删除用户方法
    public void testDeleteUser(){
        // 5.使用代理对象执行方法
        userDao.deleteUser(67);
    }

    @Test  // 测试查询一个方法
    public void testFindById(){
        // 5.使用代理对象执行方法
        User user = userDao.findById(46);
        System.out.println(user);
    }

    @Test  // 测试模糊查询方法
    public void testFindByName(){
        // 5.使用代理对象执行方法
        // 需要提供 %
        List<User> userList = userDao.findByName("%王%");
        for(User user : userList) {
            System.out.println(user);
        }
    }

    @Test  // 测试 带聚合函数的查询 方法
    public void testFindTotal(){
        // 5.使用代理对象执行方法
        int num = userDao.findTotal();
        System.out.println("总共有："+num+" 条记录");
    }
}
