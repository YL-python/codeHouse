package yang.muyun.service;

import yang.muyun.domain.Account;

import java.util.List;

public interface AccountService {

    public List<Account> findAll();
    public void saveAccount(Account account);
}
