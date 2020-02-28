package yang.muyun.dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import yang.muyun.domain.Product;

import java.util.List;

public interface IProductDao {

    // 查询所有商品信息
    @Select("select * from product;")
    public List<Product> findAll() throws Exception;

    @Insert("insert into product(productNum,productName,cityName,departureTime,productPrice,productDesc,productStatus) values(#{productNum},#{productName},#{cityName},#{departureTime},#{productPrice},#{productDesc},#{productStatus})")
    void save(Product product);

    // 根据id查询
    @Select("select * from product where id=#{id}")
    public Product findById(int id);
}
