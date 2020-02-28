package yang.muyun.dao;

import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;
import yang.muyun.domain.User;

import java.util.List;

// 开启二级缓存
@CacheNamespace(blocking = true)
public interface UserDao {

    // 查询所有用户
    @Select("select * from user")
    @Results(id="userMap",value={
            @Result(id=true,column = "id",property = "userId"),
            @Result(column = "username",property = "userName"),
            @Result(column = "address",property = "userAddress"),
            @Result(column = "sex",property = "userSex"),
            @Result(column = "birthday",property = "userBirthday"),
            @Result(property = "accounts",column = "id",
                    many = @Many(select = "yang.muyun.dao.AccountDao.findAccountByUid",
                            fetchType = FetchType.LAZY))
    })
    List<User> findAll();

    // 根据id查询用户
    @Select("select * from user  where id=#{id} ")
    @ResultMap("userMap")  // 引用
    User findById(Integer userId);

    // 根据用户名称模糊查询
    @Select("select * from user where username like #{username} ")
    @ResultMap("userMap")
    List<User> findUserByName(String username);

}
