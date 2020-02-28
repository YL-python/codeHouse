package yang.muyun.mybatis.utils;

import yang.muyun.mybatis.cfg.Configuration;

import java.sql.Connection;
import java.sql.DriverManager;

// 创建数据源的工具类
public class DataSourceUtil {

    // 获取连接的方法
    public static Connection getConnection(Configuration cfg){
        try {
            Class.forName(cfg.getDriver());
            return DriverManager.getConnection(cfg.getUrl(), cfg.getUsername(), cfg.getPassword());
        }catch(Exception e){
            throw new RuntimeException(e);
        }
    }
}
