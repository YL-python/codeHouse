package main.java.jdbc_code;

/*
// 6.执行sql
int count = stmt.executeUpdate(sql);
执行  增 insert  语句
*/

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class jdbcDemo02 {
    public static void main(String[] args){
        Statement stmt = null;
        Connection conn = null;
        try {
            // 1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            // 2. 定义sql语句
            // String sql = "insert into stdent01 values(3, '小小', 25, '女', '南昌', 777, 888)";
            // String sql = "insert into stdent01 values(4, '小王', 50, '女', '九江', 66, 87)";
            String sql = "insert into stdent01 values(5, '小黄', 18, '女', '好吃国', 100, 100)";
            // 3. 获取Connection对象
            conn = DriverManager.getConnection("jdbc:mysql:///db1", "root", "root");
            // 4. 获取执行sql对象 Statement
            stmt = conn.createStatement();
            // 5. 执行sql语句
            int count = stmt.executeUpdate(sql);
            // 6. 处理结果
            if(count==1){
                System.out.println("添加成功");
            }else {
                System.out.println("添加失败");
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            if(stmt != null){
                try {
                    stmt.close();  // 先使用的conn对象
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
