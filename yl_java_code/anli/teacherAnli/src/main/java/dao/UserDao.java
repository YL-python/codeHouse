package main.java.dao;

import main.java.domain.User;
import main.java.utils.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.ArrayList;
import java.util.List;

public class UserDao {
    // 获取一个JDBCTemlate对象，是一个简化数据库操作的框架对象
    public static JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 定义添加多用户方法
    public void addUsers(List<User> users){
        jdbcTemplate.update("delete from teacher;");
        String sql = "insert into teacher values(?,?,?,?,?)";
        for (User user : users) {
            jdbcTemplate.update(sql,user.getId(),user.getName(),user.getTel(),user.getTeacher_home(),user.getCount());
        }
    }
    // 定义获取多用户方法
    public List<User> getUsers(){
        String sql = "select * from teacher";
        List<User> users = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class));
        return users;
    }

    // 定义重置count列方法
    public void resetCount(){
        String sql = "update teacher set count=?;";
        jdbcTemplate.update(sql,0);
    }

    // 定义查找指定数量数据的方法
    public List<User> findUserByNum(int num){
        // 查找最小值
        Integer min = jdbcTemplate.queryForObject("select min(count) from teacher", Integer.class);
        // 查找最小值的个数
        Integer min_count = jdbcTemplate.queryForObject("select count(*) from teacher where count=?", Integer.class,min);
        if(min_count >= num){  // 如果最小值的个数 比要查找的个数多就查找 指定个数  并且把count设置成 min+1
            String sql ="select * from teacher where count=? limit 0,?;";
            List<User> users = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class), min, num);
            List ids = new ArrayList();
            for (User user : users) {
                ids.add(user.getId());
            }
            for (Object id : ids) {
                jdbcTemplate.update("update teacher set count=? where id=?",(min+1),id);
            }
            return users;
        }else { // 如果最小值不够了 就找最小值的个数 和(num-min_count)个 min+1  个值
            String sql ="select * from teacher where count=? limit 0,?;";
            List<User> users1 = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class), min, min_count);
            List ids1 = new ArrayList();
            for (User user : users1) {
                ids1.add(user.getId());
            }
            for (Object id : ids1) {
                jdbcTemplate.update("update teacher set count=? where id=?",(min+1),id);
            }

            List<User> users2 = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class), min+1, num-min_count);
            List ids2 = new ArrayList();
            for (User user : users2) {
                ids2.add(user.getId());
            }
            for (Object id : ids2) {
                jdbcTemplate.update("update teacher set count=? where id=?",(min+2),id);
            }
            users1.addAll(users2);
            return users1;
        }
    }

    // 定义重置已知id的count列方法
    public void reduceCountById(int id){
        Integer count = jdbcTemplate.queryForObject("select count from teacher where id=?", Integer.class,id);
        String sql = "update teacher set count=? where id=?;";
        jdbcTemplate.update(sql,count-1,id);
    }

    // 在id后查找一条数据
    public User findUserBeforeID(int id){
        // 查找最小值
        Integer min = jdbcTemplate.queryForObject("select min(count) from teacher", Integer.class);
        System.out.println("最小值"+min);
        // 找当前ID位于第几个
//        Integer temp = jdbcTemplate.queryForObject("select count(*) from teacher where id<=?", Integer.class,id);
//        System.out.println("这个数据在第几位？---"+temp);
        // 找id后的一个
        User user = jdbcTemplate.queryForObject("select * from teacher where count=? AND id>? limit 0,1", new BeanPropertyRowMapper<>(User.class),min,id);
        jdbcTemplate.update("update teacher set count=? where id=?",(min+1),user.getId());
        return user;
    }

}
