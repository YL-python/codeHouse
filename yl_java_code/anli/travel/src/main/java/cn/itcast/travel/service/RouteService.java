package cn.itcast.travel.service;

import cn.itcast.travel.domain.PageBean;
import cn.itcast.travel.domain.Route;

public interface RouteService {
    // 分页查询的方法
    PageBean<Route> pageQuery(int cid, int currentPage, int pageSize, String rname);

    // 根据id值查找线路详细信息
    Route findOne(String rid);
}
