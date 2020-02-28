package cn.itcast.travel.service.impl;

import cn.itcast.travel.dao.CategoryDao;
import cn.itcast.travel.dao.impl.CategoryDaoImpl;
import cn.itcast.travel.domain.Category;
import cn.itcast.travel.service.CategoryService;
import cn.itcast.travel.util.JedisUtil;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.Tuple;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Set;

public class CategoryServiceImpl implements CategoryService {

    private CategoryDao categoryDao = new CategoryDaoImpl();

    // 查询所有分类的方法
    @Override
    public List<Category> findAll() {
        // 先查缓存
        // 获取redis客户端
        Jedis jedis = JedisUtil.getJedis();
        // 用sortedset 排序查询分数和名称
//        Set<String> categorys = jedis.zrange("category", 0, -1);
        Set<Tuple> categorys = jedis.zrangeWithScores("category", 0, -1);

        // 缓存有直接返回
        List<Category> cs = null;
        if(categorys == null || categorys.size() == 0){
            System.out.println("从数据库中查询");
            // 缓存没有就查询数据库添加到缓存中在返回
            cs = categoryDao.findAll();
//            System.out.println(cs);
            cs.sort(new Comparator<Category>() {
                @Override
                public int compare(Category o1, Category o2) {
                    return o1.getCid()-o2.getCid();
                }
            });
//            System.out.println(cs);
            for (Category c : cs) {
                jedis.zadd("category",c.getCid(),c.getCname());
            }
        }else{
            // 有数据把set变成list
//            System.out.println("从redis中查询");
            cs = new ArrayList<Category>();
            for (Tuple t: categorys) {
                Category c = new Category();
                c.setCid((int) t.getScore());
                c.setCname(t.getElement());
                cs.add(c);
            };
//            System.out.println(cs);
        }
        return cs;
    }
}
