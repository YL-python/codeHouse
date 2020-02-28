package main.java.jdbc_code;

/*
// 6.执行sql
int count = stmt.executeUpdate(sql);
执行  修改  语句
*/

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class jdbcDemo03 {
    public static void main(String[] args){
        Connection conn = null;
        Statement stmt = null;
        try {
            // 1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            // 2.定义sql语句
            String sql = "update stdent01 set math=87,english=99 where id=3";
            // 3.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db1","root","root");
            // 4.获取sql执行对象
            stmt = conn.createStatement();
            // 5.执行sql语句
            int count = stmt.executeUpdate(sql);
            // 6.处理结果
            System.out.println(count);

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
