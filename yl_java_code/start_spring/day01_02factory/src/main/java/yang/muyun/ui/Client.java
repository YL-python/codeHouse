package yang.muyun.ui;

import yang.muyun.factory.BeanFactory;
import yang.muyun.service.IAccountService;
import yang.muyun.service.impl.AccountServiceImpl;

// 模拟表现层 调用业务层
public class Client {
    public static void main(String[] args) {
        // IAccountService as = new AccountServiceImpl();
        IAccountService as = (IAccountService) BeanFactory.getBean("accountService");
        as.saveAccount();
    }
}
