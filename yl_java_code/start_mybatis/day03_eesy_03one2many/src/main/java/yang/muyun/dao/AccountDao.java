package yang.muyun.dao;

import yang.muyun.domain.Account;
import yang.muyun.domain.AccountUser;

import java.util.List;

public interface AccountDao {

    List<Account> findAll();

    // 查询所有账户，并且带有用户名和用户地址信息
    List<AccountUser> findAllAccount();

}
