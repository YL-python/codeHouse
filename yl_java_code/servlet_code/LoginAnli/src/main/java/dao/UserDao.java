package main.java.dao;

// 提供login方法
// 操作数据库中User表
import main.java.domain.User;
import main.java.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

public class UserDao {

    public static JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 登录方法，登录成功返回User  失败返回Null
    public User login(User loginUser){
        try{
            // 编写sql
            String sql = "select * from user where username=? and password=?";
            // 调用查找方法
            User user = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<User>(User.class),
                    loginUser.getUsername(), loginUser.getPassword());
            return user;
        }catch (Exception e){
            e.printStackTrace();  // 记入日志
            return null;
        }
    }
    public void register(User registerUser){
        String sql = "insert into user values(?,?,?)";
        jdbcTemplate.update(sql,null,registerUser.getUsername(),registerUser.getPassword());
    }
}
