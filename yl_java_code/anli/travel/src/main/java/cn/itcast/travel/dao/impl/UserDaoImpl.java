package cn.itcast.travel.dao.impl;

import cn.itcast.travel.dao.UserDao;
import cn.itcast.travel.domain.User;
import cn.itcast.travel.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

public class UserDaoImpl implements UserDao {

    private JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 根据用户名查询用户信息
    @Override
    public User findUserByName(String username) {
        User user = null;
        //  防止在查询用户信息的时候出异常了报 500
        try{
            // 定义sql语句
            String sql = "select * from tab_user where username = ?";
            // 执行sql语句
            user = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<User>(User.class), username);
//            System.out.println(user);
        }catch (Exception e){
        }
        return user;
    }

    // 保存用户信息
    @Override
    public void saveUser(User user) {
        // 定义sql
        String sql = "insert into tab_user(username,password,name,birthday,sex,telephone,email,status,code) values(?,?,?,?,?,?,?,?,?)";
        // 执行sql
        jdbcTemplate.update(sql,
                user.getUsername(),
                user.getPassword(),
                user.getName(),
                user.getBirthday(),
                user.getSex(),
                user.getTelephone(),
                user.getEmail(),
                user.getStatus(),
                user.getCode()
        );

    }

    // 通过激活码查找用户
    @Override
    public User findUserByCode(String code) {
        User user = null;
        try {
            // 定义sql
            String sql = "select * from tab_user where code = ?";
            // 执行sql
            user = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<User>(User.class), code);
        }catch (Exception e){
            e.printStackTrace();
        }
        return user;
    }

    // 设置用户激活状态
    @Override
    public void updateStatus(User user) {
        // 定义sql
        String sql = "update tab_user set status='Y' where uid=?";
        // 执行sql
        jdbcTemplate.update(sql,user.getUid());
    }

    // 按用户名和密码查找用户
    @Override
    public User findUserByNAndP(User user) {
        User u = null;
        try {
            // 定义sql
            String sql = "select * from tab_user where username=? and password=?";
            // 执行sql
            u = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<User>(User.class), user.getUsername(),user.getPassword());
        }catch (Exception e ){
            e.printStackTrace();
        }
        return u;
    }
}
