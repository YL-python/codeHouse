package yang.muyun.service.impl;

import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import yang.muyun.dao.IOrdersDao;
import yang.muyun.dao.IProductDao;
import yang.muyun.domain.Orders;
import yang.muyun.domain.Product;
import yang.muyun.service.IOrdersService;
import yang.muyun.service.IProductService;

import java.util.List;

@Service
@Transactional  // 事务注解
public class OrdersServiceImpl implements IOrdersService {

    @Autowired
    private IOrdersDao ordersDao;

    @Override
    public List<Orders> findAll(int page, int size) throws Exception {
        PageHelper.startPage(page,size);
        return ordersDao.findAll();
    }

    @Override
    public Orders findById(int orderId) {
        return ordersDao.findById(orderId);
    }
}
