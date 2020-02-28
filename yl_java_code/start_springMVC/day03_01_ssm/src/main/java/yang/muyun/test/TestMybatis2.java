package yang.muyun.test;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import yang.muyun.dao.AccountDao;
import yang.muyun.domain.Account;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class TestMybatis2 {

    @Autowired
    private AccountDao accountDao;

    /**
     * 测试查询
     * @throws Exception
     */
    @Test
    public void Run1() throws IOException {
        // 查询所有数据
        List<Account> list = accountDao.findAll();
        for(Account account : list){
            System.out.println(account);
        }
    }

    /**
     * 测试保存
     * @throws Exception
     */
    @Test
    public void run2() throws Exception {
        Account account = new Account();
        account.setName("熊大");
        account.setMoney(400d);

        // 保存
        accountDao.saveAccount(account);
    }
}
