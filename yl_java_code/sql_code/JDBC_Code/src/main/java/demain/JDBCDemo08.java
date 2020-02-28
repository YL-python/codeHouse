package main.java.demain;

// 定义一个方法，查询stdent01表的数据将其封装为对象，然后装载集合，返回。

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class JDBCDemo08 {
    public static void main(String[] args) {
        List<Student> studentList = new JDBCDemo08().findAll();
        System.out.println(studentList);
        System.out.println(studentList.size());
    }

    public List<Student> findAll() {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Student> stuList = null;
        try {
            // 1 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            // 2 获取连接数据库对象
            conn = DriverManager.getConnection("jdbc:mysql:///db1", "root", "root");
            // 3 定义sql语句
            String sql = "select * from stdent01";
            // 4 获取sql执行对象
            stmt = conn.createStatement();
            // 5 执行sql
            rs = stmt.executeQuery(sql);
            // 6 遍历结果集 封装对象 转载集合
            Student stu = null;
            stuList= new ArrayList<>();
            while (rs.next()){
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                String sex = rs.getString("sex");
                String add = rs.getString("address");
                int math = rs.getInt("math");
                int eng = rs.getInt("english");
                stu = new Student();  // 创建对象并且赋值
                stu.setId(id);
                stu.setName(name);
                stu.setAge(age);
                stu.setSex(sex);
                stu.setAdd(add);
                stu.setMath(math);
                stu.setEng(eng);
                // 转载集合
                stuList.add(stu);
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            // 7 释放资源
            if(rs!=null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(stmt!=null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(conn!=null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
        return stuList;
    }
}
