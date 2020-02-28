package yang.muyun.dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;
import yang.muyun.domain.Account;

import java.util.List;

@Repository()
public interface AccountDao {

    @Select("select * from account")
    public List<Account> findAll();

    @Insert("insert into account (name,money) values (#{name}, #{money})")
    public void saveAccount(Account account);
}
