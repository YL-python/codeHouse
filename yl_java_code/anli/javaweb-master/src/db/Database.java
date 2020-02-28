package db;

import java.sql.*;

public class Database {
    public void Database(String sql) throws SQLException, ClassNotFoundException {
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
        Statement stmt = conn.createStatement();
        int result = stmt.executeUpdate(sql);
        System.out.println(result);
        stmt.close();
        conn.close();
    }
    public ResultSet a(String sql) throws  SQLException, ClassNotFoundException{
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
        Statement stmt = conn.createStatement();
        ResultSet result = stmt.executeQuery(sql);
        return result;
    }
}
