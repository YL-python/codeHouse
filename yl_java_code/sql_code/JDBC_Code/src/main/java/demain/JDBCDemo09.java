package main.java.demain;

/*
* 用户输入账号密码 判断是否存在
* 查询数据库 有结果就成功，没结果就失败
* */

import main.java.util.JDBCUtils;

import java.sql.*;
import java.util.Scanner;

public class JDBCDemo09 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入用户名：");
        String username = sc.nextLine();
        System.out.println("请输入密码：");
        String password = sc.nextLine();
        boolean flag = new JDBCDemo09().login2(username, password);
        if(flag){
            System.out.println("登录成功！");
        }else {
            System.out.println("用户名或密码错误！");
        }
    }
    // 登录方法
    public boolean login(String username,String password){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        if(username == null || password == null){
            return false;
        }
        // 定义sql语句
        String sql = "SELECT * FROM user WHERE username='"+username+"' AND password='"+password+"'";
        try {
            // 连接数据库判断是否成功  修改配置文件哦
            conn = JDBCUtils.getConnection();
            stmt = conn.createStatement();
            //执行sql语句
            rs = stmt.executeQuery(sql);
//            if(rs.next()){
//                return true;
//            }else {
//                return false;
//            }
            return rs.next();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JDBCUtils.close(rs, stmt, conn);
        }
        return false;
    }
    // 用preparedStatement是实现
    public boolean login2(String username,String password){
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        if(username == null || password == null){
            return false;
        }
        // 定义sql语句
        String sql = "SELECT * FROM user WHERE username=? AND password=?";
        try {
            // 连接数据库判断是否成功  修改配置文件哦
            conn = JDBCUtils.getConnection();
            //获取执行对象
            pstmt = conn.prepareStatement(sql);
            //给？赋值
            pstmt.setString(1,username);
            pstmt.setString(2,password);
            //执行sql语句
            rs = pstmt.executeQuery();
            return rs.next();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JDBCUtils.close(rs, pstmt, conn);
        }
        return false;
    }
}
