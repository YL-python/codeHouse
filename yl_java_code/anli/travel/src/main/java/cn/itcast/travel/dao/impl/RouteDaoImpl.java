package cn.itcast.travel.dao.impl;

import cn.itcast.travel.dao.RouteDao;
import cn.itcast.travel.domain.Route;
import cn.itcast.travel.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.ArrayList;
import java.util.List;

public class RouteDaoImpl implements RouteDao {
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    // 根据cid和rname查询总记录数
    @Override
    public int findTotalCount(int cid, String rname) {
        // String sql = "select count(*) from tab_route where cid = ?";
        String sql = " select count(*) from tab_route where 1 = 1 ";
        StringBuilder sb = new StringBuilder(sql);
        List params = new ArrayList(); // 条件集合
        // 判断两个参数是否有值
        if(cid != 0){
            sb.append(" and cid = ? ");
            params.add(cid);
        }
        if(rname != null && rname.length() > 0){
            sb.append(" and rname like ? ");
            params.add("%"+rname+"%");
        }

        sql = sb.toString();
        return template.queryForObject(sql,Integer.class,params.toArray());
    }

    // 根据cid start pageSize  rname查询当前页的数据
    @Override
    public List<Route> findByPage(int cid, int start, int pageSize, String rname) {
        // String sql = "select * from tab_route where cid = ? limit ?,?";
        String sql = " select * from tab_route where 1 = 1 ";
        StringBuilder sb = new StringBuilder(sql);
        List params = new ArrayList(); // 条件集合
        // 判断两个参数是否有值
        if(cid != 0){
            sb.append(" and cid = ? ");
            params.add(cid);
        }
        if(rname != null && rname.length() > 0){
            sb.append(" and rname like ? ");
            params.add("%"+rname+"%");
        }
        sb.append(" limit ? , ? ");
        params.add(start);
        params.add(pageSize);

        sql = sb.toString();
        return template.query(sql,new BeanPropertyRowMapper<Route>(Route.class),params.toArray());
    }

    // 根据id值查找线路详细信息
    @Override
    public Route findOne(int rid) {
        String sql = "select * from tab_route where rid = ?";
        return template.queryForObject(sql,new BeanPropertyRowMapper<Route>(Route.class),rid);
    }
}
