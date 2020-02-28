package db;

import java.sql.*;

public class DatabaseQuery {
    public void DatabaseQuery(String sql) throws SQLException, ClassNotFoundException {
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
        Statement stmt = conn.createStatement();
        ResultSet resultSet = stmt.executeQuery(sql);
        System.out.println(resultSet);
    }
}
