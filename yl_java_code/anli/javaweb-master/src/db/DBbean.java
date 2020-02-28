package db;
import java.sql.*;
import java.io.*;

public class DBbean implements Serializable{

        private String driverStr="com.mysql.jdbc.Driver";
        private Statement stmt=null;
        public DBbean()
        {
            try{
                Class.forName(driverStr);
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
                stmt=conn.createStatement();
            }
            catch(Exception ex){
                System.out.println("无法同数据库建立连接");
            }
        }
        public int executeUpdate(String s){
            int result =0;
            try{
                result=stmt.executeUpdate(s);
            }
            catch(Exception ex){System.out.println("执行更新错误!");
            }
            return result;
        }

        public ResultSet executeQuery(String s){
            ResultSet rs=null;
            try{
                rs=stmt.executeQuery(s);
            }
            catch(Exception ex){
                ex.printStackTrace();
                System.out.println("执行查询错误!");}
            return rs;
        }
    }


