package yang.muyun.test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import yang.muyun.service.AccountService;

public class TestSpring {

    @Test
    public void Run1(){
        // 加载配置文件
        ApplicationContext ac = new ClassPathXmlApplicationContext("classpath:applicationContext.xml");
        // 获取对象
        AccountService as = (AccountService) ac.getBean("accountService");
        // 调用方法
        as.findAll();
    }
}
