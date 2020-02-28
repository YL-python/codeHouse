package main.java.jdbc_code;

/*
测试JDBC工具类
*/

import main.java.demain.JDBCDemo08;
import main.java.demain.Student;
import main.java.util.JDBCUtils;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class jdbcDemo08 {
    public static void main(String[] args) {
        List<Student> studentList = new JDBCDemo08().findAll();
        System.out.println(studentList);
        System.out.println(studentList.size());
    }

    private List<Student> findAll() {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Student> stuList = null;
        try {
            // 3 定义sql语句
            String sql = "select * from stdent01";
            conn = JDBCUtils.getConnection();
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
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JDBCUtils.close(rs,stmt,conn);
        }
        return stuList;
    }
}
