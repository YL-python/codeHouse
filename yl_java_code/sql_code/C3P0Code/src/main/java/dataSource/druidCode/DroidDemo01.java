package main.java.dataSource.druidCode;

/*
* Droid基本使用演示
* */

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.InputStream;
import java.sql.Connection;
import java.util.Properties;

public class DroidDemo01 {
    public static void main(String[] args) throws Exception {
        // 1 导包
        // 2 定义配置文件
        // 3 加载配置文件
        Properties pro = new Properties();
        InputStream is = DroidDemo01.class.getClassLoader().getResourceAsStream("D:\\Intellij_IDEA\\DataSourceCode\\C3P0Code\\src\\druid.properties");
        pro.load(is);
        // 4 获取连接池对象
        DataSource ds = DruidDataSourceFactory.createDataSource(pro);
        // 5 获取连接
        Connection conn = ds.getConnection();
        System.out.println(conn);
    }
}
