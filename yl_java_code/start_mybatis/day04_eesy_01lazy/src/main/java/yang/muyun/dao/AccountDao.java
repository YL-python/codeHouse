package yang.muyun.dao;

import yang.muyun.domain.Account;
import yang.muyun.domain.AccountUser;

import java.util.List;

public interface AccountDao {

    List<Account> findAll();

    // 根据用户id查询账户信息
    List<Account> findAccountByUid(Integer uid);
}
