package main.java.jdbc_code;

/*
    jdbc快速入门
*/

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class jdbcDemo01 {
    public static void main(String[] args) throws Exception {

        // 1.导入驱动jar包  添加到库
        // 2.注册驱动
        Class.forName("com.mysql.jdbc.Driver");
        // 3.获取数据库的连接对象    jdbc:mysql://IP:端口/数据库名   用户   密码
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db1", "root", "root");
        // 4.定义sql语句
        String sql = "update stdent01 set math=999 where id=1";
        // 5.获取执行sql的对象  Statement
        Statement stmt = conn.createStatement();
        // 6.执行sql
        int count = stmt.executeUpdate(sql);
        // 7.处理结果
        System.out.println(count);
        // 8.释放资源
        stmt.close();
        conn.close();
    }
}
