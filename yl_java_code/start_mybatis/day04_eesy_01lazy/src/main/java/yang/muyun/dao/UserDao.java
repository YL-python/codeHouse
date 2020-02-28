package yang.muyun.dao;

import yang.muyun.domain.User;

import java.util.List;

public interface UserDao {

    List<User> findAll();

    User findById(Integer userId);
}
