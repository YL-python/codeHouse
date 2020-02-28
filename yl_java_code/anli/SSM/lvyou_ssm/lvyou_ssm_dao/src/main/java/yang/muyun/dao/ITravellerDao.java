package yang.muyun.dao;

        import org.apache.ibatis.annotations.Select;
        import yang.muyun.domain.Traveller;

        import java.util.List;


public interface ITravellerDao {

    // 根据id查询
    @Select("select * from traveller where id in (select travellerId from order_traveller where orderId = #{ordersId})")
    public List<Traveller> findByOrdersId(int ordersId);
}
