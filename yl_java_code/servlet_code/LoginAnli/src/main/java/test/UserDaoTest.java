package main.java.test;

import main.java.dao.UserDao;
import main.java.domain.User;
import org.junit.Test;

public class UserDaoTest {
    @Test
    public void testLogin(){
        User loginuser = new User();
        loginuser.setUsername("superbaby");
        loginuser.setPassword("123666");

        UserDao dao = new UserDao();
        User user = dao.login(loginuser);

        System.out.println(user);
    }

    @Test
    public void testRegister(){
        User registeruser = new User();
        registeruser.setUsername("lissss");
        registeruser.setPassword("li");
        registeruser.setId(-1);
        UserDao dao = new UserDao();
        dao.register(registeruser);
        System.out.println(registeruser);
    }

}
