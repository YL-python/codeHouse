package mian.java.dao;

import mian.java.domain.Admin;
import mian.java.utils.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

public class UserDao {

    // 获取一个JDBCTemlate对象，是一个简化数据库操作的框架对象
    public static JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 定义一个login方法用来查找数据库中有没有对应的数据
    public Admin loginAdmin(Admin loginAdmin){
        try {
            // 定义sql语句
            String sql = "select * from adminuser where username=? and password=?";
            //调用查询方法，把结果封装成一个Object(Admin对象)
            // new BeanPropertyRowMapper<Object>(Object.class)  固定格式   后面的参数对应着？号处
            Admin admin = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<Admin>(Admin.class), loginAdmin.getUsername(), loginAdmin.getPassword());
            return admin;
        }catch (Exception e){
            e.printStackTrace();
            return null;
        }
    }
}
