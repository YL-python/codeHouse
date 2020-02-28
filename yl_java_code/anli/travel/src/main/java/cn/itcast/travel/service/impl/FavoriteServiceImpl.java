package cn.itcast.travel.service.impl;

import cn.itcast.travel.dao.FavoriteDao;
import cn.itcast.travel.dao.impl.FavoriteDaoImpl;
import cn.itcast.travel.domain.Favorite;
import cn.itcast.travel.service.FavoriteService;

public class FavoriteServiceImpl implements FavoriteService {

    private FavoriteDao favoriteDao = new FavoriteDaoImpl();

    // 判断是否收藏
    @Override
    public boolean isFavorite(String rid, int uid) {
        //  Integer.getInteger(rid)   操操操操操

//        System.out.println("11111");
//        System.out.println(favoriteDao);
//        System.out.println(rid+"3333"+uid);
//        Favorite favorite = favoriteDao.findByRidAndUid(Integer.getInteger(rid), uid);
//        System.out.println(favorite != null);
//        return favorite != null;

        // Integer.parseInt(rid)  操操操操操
        Favorite favorite = favoriteDao.findByRidAndUid(Integer.parseInt(rid), uid);

        return favorite != null;//如果对象有值，则为true，反之，则为false
    }

    @Override
    public void add(String rid, int uid) {
        favoriteDao.insert(Integer.parseInt(rid), uid);
    }
}
