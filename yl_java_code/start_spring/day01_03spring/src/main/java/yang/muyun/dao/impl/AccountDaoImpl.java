package yang.muyun.dao.impl;

import yang.muyun.dao.IAccountDao;

// 账户的持久层实现类
public class AccountDaoImpl implements IAccountDao {
    public void saveAccount() {
        System.out.println("向数据库中保存数据成功");
    }
}
