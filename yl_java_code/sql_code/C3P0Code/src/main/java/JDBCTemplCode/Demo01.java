package main.java.JDBCTemplCode;

/*
* JDBCTemplate基本操作
* */

import main.java.utils.JDBCUtils;
import org.springframework.jdbc.core.JdbcTemplate;

public class Demo01 {
    public static void main(String[] args) {
        // 导包
        // 创建JDBCTemplate 对象
        JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
        // 调用方法
        String sql = "insert into account values(?,?,?)";
        int count = template.update(sql, 5, "xiaomin", 600);
        System.out.println(count);
    }
}
