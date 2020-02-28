package main.java.dao;

import main.java.domian.Admin;
import main.java.domian.User;
import main.java.utils.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class userDao {
    // 获取一个JDBCTemlate对象，是一个简化数据库操作的框架对象
    public static JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 定义一个loginAdmin方法用来查找数据库中有没有对应的数据
    public Admin loginAdmin(Admin loginadmin){
        try {
            // 定义sql语句
            String sql = "select * from adminuser where username=? and password=?";
            //调用查询方法，把结果封装成一个Object(Admin对象)
            // new BeanPropertyRowMapper<Object>(Object.class)  固定格式   后面的参数对应着？号处
            Admin admin = jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<Admin>(Admin.class),
                    loginadmin.getUsername(), loginadmin.getPassword());
            return admin;
        }catch (Exception e){
            e.printStackTrace();
            return null;
        }
    }

    // 定义添加方法
    // insert into user values(null,?,?,?,?,?,?)  // 会报错
    public void addUser(User user){
        String sql = "insert into user values(?,?,?,?,?,?,?)";
        jdbcTemplate.update(sql,null,user.getName(),user.getGender(),user.getAge(),user.getAddress(),user.getQq(),user.getEmail());
    }

    // 定义查找全部用户的方法
    public List<User> findAllUser(){
        // 定义sql语句
        String sql = "select * from user";
        List<User> users = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class));
        return users;
    }

    // 定义删除用户的方法
    public void delUserByid(int id){
        String sql = "delete from user where id=?";
        jdbcTemplate.update(sql,id);
    }

    // 定义查找用户所有信息的方法
    public User findUserByid(int id){
        String sql = "select * from user where id=?";
        User user = jdbcTemplate.query(sql, new BeanPropertyRowMapper<User>(User.class), id).get(0);
        return user;
    }

    // 定义修改数据的方法
    public void upData(User user){
        String sql = "update user set name=?,gender=?,age=?,address=?,qq=?,email=? where id=?";
        jdbcTemplate.update(sql,user.getName(),user.getGender(), user.getAge(), user.getAddress(),user.getQq(),user.getEmail(),user.getId());
    }

    // 定义查询中记录数的方法
    public int getTotalCount(Map<String, String[]> parameterMap){
        // 动态查询
        String sql = "select count(*) from user where 1=1 ";
        StringBuilder sb = new StringBuilder(sql);
        // 遍历map获取参数
        Set<String> keySet = parameterMap.keySet();
        // 来一个参数集合
        ArrayList<Object> arrayList = new ArrayList<>();
        for (String key : keySet) {
            String value = parameterMap.get(key)[0];
            // 排出分页的参数
            if("currentPage".equals(key)){
                continue;
            }
            if(value!=null && !"".equals(value)){
                // 表示有值
                sb.append(" and "+key+" like ? ");
                arrayList.add("%"+value+"%");  // 装？ 号的值
            }
        }
//        System.out.println(sb.toString());
        //  可变参数的本质上是一个数组
        return jdbcTemplate.queryForObject(sb.toString(),Integer.class,arrayList.toArray());
    }

    // 分页查询的方法
    public List<User> findUserByPage(int start, int rows, Map<String, String[]> parameterMap){
        // 分页查询，  开始索引，每页的数据
        String sql = "select * from user where 1=1 ";
        StringBuilder sb = new StringBuilder(sql);
        // 遍历map获取参数
        Set<String> keySet = parameterMap.keySet();
        // 来一个参数集合
        ArrayList<Object> arrayList = new ArrayList<>();
        for (String key : keySet) {
            String value = parameterMap.get(key)[0];
            // 排出分页的参数
            if("currentPage".equals(key)){
                continue;
            }
            if(value!=null && !"".equals(value)){
                // 表示有值
                sb.append(" and "+key+" like ? ");
                arrayList.add("%"+value+"%");  // 装？ 号的值
            }
        }
        sb.append(" limit ?,?");
        arrayList.add(start);
        arrayList.add(rows);
//        System.out.println(sb.toString());
        List<User> users = jdbcTemplate.query(sb.toString(), new BeanPropertyRowMapper<User>(User.class), arrayList.toArray());
        return users;
    }
}
