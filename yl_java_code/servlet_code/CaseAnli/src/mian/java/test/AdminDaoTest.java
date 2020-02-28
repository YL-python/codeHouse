package mian.java.test;

import mian.java.dao.UserDao;
import mian.java.domain.Admin;
import org.junit.Test;


public class AdminDaoTest {

    @Test
    public void testloginAdmin(){
        // 创建登录用户
        Admin admin = new Admin();
        admin.setUsername("zhansan");
        admin.setPassword("12311");

        // 创建数据库调用对象
        UserDao dao = new UserDao();
        Admin login = dao.loginAdmin(admin);
        System.out.println(login);
    }

}
