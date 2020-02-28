package main.java.jdbc_code;

// ResultSet 正确的使用

import java.sql.*;

public class jdbcDemo07 {
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
            // 获取数据
            while (rs.next()){
                int id = rs.getInt(1);
                String name = rs.getString("name");
                int age = rs.getInt(3);
                String sex = rs.getString(4);
                String add = rs.getString(5);
                int math = rs.getInt(6);
                int eng = rs.getInt(7);
                // 打印数据
                System.out.println(id+"---"+name+"---"+age+"---"+sex+"---"+add+"---"+math+"---"+eng);
            }
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
