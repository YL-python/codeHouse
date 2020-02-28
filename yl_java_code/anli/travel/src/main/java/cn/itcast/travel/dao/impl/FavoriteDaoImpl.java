package cn.itcast.travel.dao.impl;

import cn.itcast.travel.dao.FavoriteDao;
import cn.itcast.travel.domain.Favorite;
import cn.itcast.travel.util.JDBCUtils;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.Date;

public class FavoriteDaoImpl implements FavoriteDao {

    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    // 根据rid 和uid查询收藏信息
    @Override
    public Favorite findByRidAndUid(int rid, int uid) {
        Favorite favorite = null;
        try {
            String sql = " select * from tab_favorite where rid = ? and uid = ?";
            favorite = template.queryForObject(sql, new BeanPropertyRowMapper<Favorite>(Favorite.class), rid, uid);
        } catch (DataAccessException e) {
            System.out.println("没有查询到收藏信息");
        }
        return favorite;
    }

    @Override
    public int findCountByRid(int rid) {
        String sql = " select count(*) from tab_favorite where rid = ?";
        return template.queryForObject(sql, Integer.class, rid);
    }

    @Override
    public void insert(int rid, int uid) {
        String sql = " insert into tab_favorite values(?,?,?)";
        template.update(sql,rid,new Date(),uid);
    }
}
