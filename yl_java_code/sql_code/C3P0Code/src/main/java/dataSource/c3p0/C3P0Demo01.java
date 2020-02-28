package main.java.dataSource.c3p0;

/*
* 演示C3P0的使用
* */

import com.mchange.v2.c3p0.ComboPooledDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

public class C3P0Demo01 {
    public static void main(String[] args) throws SQLException {
        // 创建数据库连接池对象
        DataSource ds = new ComboPooledDataSource();
        //获取连接对象
        Connection conn = ds.getConnection();
        // 打印
        System.out.println(conn);
    }
}
