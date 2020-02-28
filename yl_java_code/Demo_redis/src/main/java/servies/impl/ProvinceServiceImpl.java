package main.java.servies.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import main.java.dao.ProvinceDao;
import main.java.dao.impl.ProvinceDaoImpl;
import main.java.domain.Province;
import main.java.jedis.util.JedisPoolUtils;
import main.java.servies.ProvinceService;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

import java.util.List;

public class ProvinceServiceImpl implements ProvinceService {
    //  provinceDao返回结果集  给Service  通过Service返回给客户端

    // 定义dao
    private ProvinceDao dao = new ProvinceDaoImpl();

    @Override
    public List<Province> findAll() {
        return dao.findAll();
    }

    // 使用缓存
    @Override
    public String findAllJson(){
        // 1.在redis中查询数据
        // 1.1获取redis客户端,获取数据
        Jedis jedis = new JedisPoolUtils().getJedis();
        String province_json = jedis.get("province");
        // 1.2看缓存中有没有数据
        if(province_json == null || province_json.length()==0){
            // 没有数据就查询数据库在存数据到缓存中并且返回
            System.out.printf("redis中没有数据，查询数据库。。。");
            List<Province> provinceList = dao.findAll();
            // 把列表变成json对象
            ObjectMapper mapper = new ObjectMapper();
            try {
                province_json = mapper.writeValueAsString(provinceList);
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }
            // 吧数据存到缓存中
            jedis.set("province",province_json);
            jedis.close();
        }else{
            System.out.println("redis中有数据，查询缓存。。。");
        }
        // 有数据就直接吧数据返回
        return province_json;
    }
}
