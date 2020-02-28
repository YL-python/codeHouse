package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import yang.muyun.dao.AccountDao;
import yang.muyun.domain.Account;
import yang.muyun.domain.AccountUser;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class AccountTest {
    private InputStream in;
    private SqlSession session;
    private AccountDao accountDao;

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
        accountDao = session.getMapper(AccountDao.class);
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
        List<Account> accounts = accountDao.findAll();
        for(Account account : accounts) {
            System.out.println("--------------");
            System.out.println(account);
            System.out.println(account.getUser());
        }
    }

    @Test  // 测试查询所有方法
    public void findAllAccount(){
        // 5.使用代理对象执行方法
        List<AccountUser> accountusers = accountDao.findAllAccount();
        for(AccountUser a : accountusers) {
            System.out.println(a);
        }
    }
}
