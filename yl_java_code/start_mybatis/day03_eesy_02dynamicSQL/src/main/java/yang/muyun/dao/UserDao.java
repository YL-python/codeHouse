package yang.muyun.dao;

import yang.muyun.domain.QueryVo;
import yang.muyun.domain.User;

import java.util.List;

public interface UserDao {

    List<User> findAll();

    User findById(Integer userId);

    List<User> findByName(String username);

    // 用对象 来查询
    List<User> findUserByVo(QueryVo queryVo);

    // 根据传入的参数条件查询
    List<User> findUserByCondition(User user);

    // 范围查询
    List<User> findUserInIds(QueryVo queryVo);
}
