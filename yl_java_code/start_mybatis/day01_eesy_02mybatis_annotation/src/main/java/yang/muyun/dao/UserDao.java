package yang.muyun.dao;

import org.apache.ibatis.annotations.Select;
import yang.muyun.domain.User;

import java.util.List;

// 用户的持久层接口
public interface UserDao {

    // 查询所有用户方法
    @Select("select * from user")
    List<User> findAll();

}
