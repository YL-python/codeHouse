package main.java.dataSource.druidCode;

/*
* 使用连接池工具类
* 完成一个添加的操作
* */

import main.java.utils.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DtuidDemo02UseJDBCUtils {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt= null;
        try {
            // 获取连接
            conn = JDBCUtils.getConnection();
            // 定义sql
            String sql = "insert into account values(?,?,?)";
            // 获取执行sql对象
            pstmt = conn.prepareStatement(sql);
            // 给sql赋值
            pstmt.setInt(1,4);
            pstmt.setString(2,"xiaohuan");
            pstmt.setInt(3,10000);
            // 执行sql
            int count = pstmt.executeUpdate();
            System.out.println(count);
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
//            关闭资源
            JDBCUtils.close(pstmt, conn);
        }
    }
}
