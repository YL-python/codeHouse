package yang.muyun.dao;

import yang.muyun.domain.QueryVo;
import yang.muyun.domain.User;

import java.util.List;

public interface UserDao {

    List<User> findAll();

    void saveUser(User user);

    void updateUser(User user);

    void deleteUser(Integer userId);

    User findById(Integer userId);

    List<User> findByName(String username);

    // 查询总用户数
    int findTotal();

    // 用对象 来查询
    List<User> findUserByVo(QueryVo queryVo);
}
