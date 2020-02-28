package main.java.jdbc_code;

/*
事务实现数据库转账效果
* */

import main.java.util.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class jdbcDemo09 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt1 = null;
        PreparedStatement pstmt2 = null;
        try {
            // 获取数据库连接
            conn = JDBCUtils.getConnection();

            // 开启事务
            conn.setAutoCommit(false);

            // 定义sql
            // 两个sql  一个减少，一个相加
            String sql1 = "update account set balance = balance - ? WHERE name = ?";
            String sql2 = "update account set balance = balance + ? WHERE name = ?";
            //获取执行sql对象
            pstmt1 = conn.prepareStatement(sql1);
            pstmt2 = conn.prepareStatement(sql2);
            // 设置参数
            pstmt1.setInt(1,500);
            pstmt1.setString(2,"zhangsan");
            pstmt2.setInt(1,500);
            pstmt2.setString(2,"lisi");
            //执行sql语句
            pstmt1.executeUpdate();
            int i = 1/0;
            pstmt2.executeUpdate();

            //提交事务
            conn.commit();

        } catch (Exception e) {   // 抓一个大一点的异常
            // 事务的回滚   一旦发生异常就回滚
            try {
                if(conn!=null){   // 不为空就回滚
                    conn.rollback();
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
            e.printStackTrace();
        }finally {
            JDBCUtils.close(pstmt1,conn);
            JDBCUtils.close(pstmt2,null);
        }
    }
}
