package yang.muyun.test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import yang.muyun.dao.ItemsDao;
import yang.muyun.domain.Items;
import yang.muyun.service.ItemsService;

public class ItemsTest {

    @Test
    public void findById(){
        //获取spring容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
        //dao测试
        //从容器中拿到所需的dao的代理对象
        ItemsDao itemsDao = ac.getBean(ItemsDao.class);
        //调用方法
        Items items = itemsDao.findById(1);
        System.out.println(items);
    }


    @Test
    public void findById2(){
        //获取spring容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("applicationContext.xml");
//        service测试
        ItemsService itemsService = ac.getBean(ItemsService.class);
        //调用方法
        Items items = itemsService.findById(1);
        System.out.println(items.getName());
    }

}
