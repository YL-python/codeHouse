package cn.itcast.travel.service;

public interface FavoriteService {
    // 判断是否收藏
    public boolean isFavorite(String rid, int uid);

    // 添加喜欢数
    public void add(String rid,int uid);
}
