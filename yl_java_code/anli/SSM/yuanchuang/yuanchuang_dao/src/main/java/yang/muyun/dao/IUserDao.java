package yang.muyun.dao;


import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import yang.muyun.domain.RegisterData;
import yang.muyun.domain.UserInfo;

public interface IUserDao {
    // 保存一个学生信息到学生表中
    @Insert("insert into user(username,password,userXingMing,userClass,userPhoneNum,userBirthday,userSex) values(#{username},#{password},#{userXingMing},#{userClass},#{userPhoneNum},#{userBirthday},#{userSex})")
    void save(UserInfo userInfo);


    // 通过账户和密码查找用户
    @Select("select * from user where username=#{username} and password=#{password}")
    UserInfo findStudentByUsernameAndPassword(@Param("username") String username, @Param("password") String password);

    // 通过用户名查找用户详情信息
    @Select("select * from user where username=#{username}")
    UserInfo findByUsername(String username);

    // 通过用户名修改用户信息
    @Insert("update user set username=#{username},password=#{password},userXingMing=#{userXingMing},userClass=#{userClass},userPhoneNum=#{userPhoneNum},userBirthday=#{userBirthday},userSex=#{userSex} where id=#{id};")
    void updateByUsername(UserInfo userInfo);

    @Select("select count(username) from user where username=#{username}")
    Integer findUsername(RegisterData data);
}
