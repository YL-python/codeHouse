package yang.muyun.dao.impl;

import org.springframework.stereotype.Repository;
import yang.muyun.dao.IAccountDao;

// 账户的持久层实现类
@Repository("accountDao1")
public class AccountDaoImpl1 implements IAccountDao {
    public void saveAccount() {
        System.out.println("向数据库中保存数据成功111");
    }
}
