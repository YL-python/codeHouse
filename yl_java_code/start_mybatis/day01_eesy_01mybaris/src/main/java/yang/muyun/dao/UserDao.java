package yang.muyun.dao;

import yang.muyun.domain.User;

import java.util.List;

// 用户的持久层接口
public interface UserDao {

    // 查询所有用户方法
    List<User> findAll();

}
