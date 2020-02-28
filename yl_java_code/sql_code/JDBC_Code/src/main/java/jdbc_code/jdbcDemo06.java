package main.java.jdbc_code;

//  ResultSet 基本使用

import java.sql.*;

public class jdbcDemo06 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            Class.forName("com.mysql.jdbc.Driver");
            String sql = "select * from stdent01";
            conn = DriverManager.getConnection("jdbc:mysql:///db1", "root", "root");
            stmt = conn.createStatement();
            // 执行sql语句
            rs = stmt.executeQuery(sql);
            // 处理结果
            // 先让光标向下一行
            rs.next();
            // 获取数据
            int id1 = rs.getInt(1);
            String name1 = rs.getString("name");
            int age1 = rs.getInt(3);
            String sex1 = rs.getString(4);
            String add1 = rs.getString(5);
            int math1 = rs.getInt(6);
            int eng1 = rs.getInt(7);
            // 打印数据
            System.out.println(id1+"---"+name1+"---"+age1+"---"+sex1+"---"+add1+"---"+math1+"---"+eng1);  // 1---张三---18---男---江西---999---50
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
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
    }
}
