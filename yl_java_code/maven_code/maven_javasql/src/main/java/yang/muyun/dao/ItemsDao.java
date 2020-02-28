package yang.muyun.dao;

import yang.muyun.domain.Items;

import java.sql.SQLException;
import java.util.List;

public interface ItemsDao {
    public List<Items> findAll() throws Exception;
}
