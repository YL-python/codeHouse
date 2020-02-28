package yang.muyun.ui;

import yang.muyun.service.IAccountService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * 模拟一个表现层，用于调用业务层
 */
public class Client {

    public static void main(String[] args) {
        //1.获取核心容器对象
         ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
        IAccountService as1  = (IAccountService)ac.getBean("accountService");
        IAccountService as2  = (IAccountService)ac.getBean("accountService2");
        IAccountService as3  = (IAccountService)ac.getBean("accountService3");

        as1.saveAccount();
        as2.saveAccount();
        as3.saveAccount();

    }
}
