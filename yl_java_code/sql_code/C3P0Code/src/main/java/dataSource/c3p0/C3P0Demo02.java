package main.java.dataSource.c3p0;

/*
* c3p0连接参数的使用
* */

import com.mchange.v2.c3p0.ComboPooledDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

public class C3P0Demo02 {
    public static void main(String[] args) throws SQLException {
        // 获取数据库连接池对象   什么都不传使用默认的配置  传一个字符串回去找对应的配置信息
        DataSource ds = new ComboPooledDataSource("otherc3p0");
        // 获取连接
        for (int i = 1; i <=11 ; i++) {
            Connection conn = ds.getConnection();
            System.out.println(i+":"+conn);
            if(i == 5){
                conn.close(); // 归还
            }
        }
    }
}
