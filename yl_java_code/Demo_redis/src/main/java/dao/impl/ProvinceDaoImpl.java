package main.java.dao.impl;

import main.java.dao.ProvinceDao;
import main.java.domain.Province;
import main.java.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.List;

public class ProvinceDaoImpl implements ProvinceDao {

    // 1.声明成员变量 jdbctemplement
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    @Override
    public List<Province> findAll() {
        String sql = "select * from province";
        List<Province> provinceList = template.query(sql, new BeanPropertyRowMapper<Province>(Province.class));
        return provinceList;
    }
}
