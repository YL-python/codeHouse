package yang.muyun.service;

import yang.muyun.domain.Product;

import java.util.List;

public interface IProductService {

    public List<Product> findAll() throws Exception;

    void save(Product product);
}
