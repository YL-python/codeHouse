package yang.muyun.service;


import yang.muyun.domain.Orders;


import java.util.List;

public interface IOrdersService {

    public List<Orders> findAll(int page,int size) throws Exception;

    Orders findById(int orderId);
}
