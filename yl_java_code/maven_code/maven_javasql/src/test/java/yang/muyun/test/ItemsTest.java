package yang.muyun.test;

import org.junit.Test;
import yang.muyun.dao.impl.ItemsDaoImpl;
import yang.muyun.domain.Items;

import java.util.List;

public class ItemsTest {
    @Test
    public void findAllTest() throws Exception {
        ItemsDaoImpl itemsDao = new ItemsDaoImpl();
        List<Items> all = itemsDao.findAll();
        for (Items items : all) {
            System.out.println(items);
        }
    }
}
