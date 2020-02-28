package yang.muyun.ui;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import yang.muyun.dao.IAccountDao;
import yang.muyun.service.IAccountService;
import yang.muyun.service.impl.AccountServiceImpl;

// 模拟表现层 调用业务层
public class Client {
    public static void main(String[] args) {
        // 根据 类路径 获取核心容器对象
        ApplicationContext ac = new ClassPathXmlApplicationContext("bean.xml");
        IAccountService as = (IAccountService) ac.getBean("accountService");
        System.out.println(as);

        IAccountDao dao = ac.getBean("accountDao2",IAccountDao.class);
        System.out.println(dao);
        as.saveAccount();
    }
}
