package cn.itcast.travel.dao;

import cn.itcast.travel.domain.Favorite;

public interface FavoriteDao {

    // 判断是否收藏
    public Favorite findByRidAndUid(int rid, int uid);

    public int findCountByRid(int rid);

    public void insert(int rid, int uid);

}
