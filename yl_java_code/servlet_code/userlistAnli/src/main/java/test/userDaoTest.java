package main.java.test;

import main.java.dao.userDao;
import main.java.domian.Admin;
import main.java.domian.User;
import org.junit.Test;

import java.util.List;

public class userDaoTest {

    @Test
    public void loginadminTest(){
        Admin loginadmin = new Admin();
        loginadmin.setUsername("lisi");
        loginadmin.setPassword("1231");

        userDao dao = new userDao();
        Admin admin = dao.loginAdmin(loginadmin);
        System.out.println(admin.toString());
    }

    @Test
    public void addUserTest(){
        User user = new User();
        user.setName("yyy");
        user.setAge(200);
        userDao dao = new userDao();
        dao.addUser(user);
    }

    @Test
    public void findAllUserTest(){
        List<User> allUser = new userDao().findAllUser();
        for (User user : allUser) {
            System.out.println(user);
        }
    }

    @Test
    public void cityTest(){
        String citys = "北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区";
        String[] split = citys.split("，");
        for (String s : split) {
            System.out.printf(s);
        }
    }

    @Test
    public void intTest(){
        System.out.println(Integer.parseInt("5"));
    }

    @Test
    public void findUserByidTest(){
        User userByid = new userDao().findUserByid(1);
        System.out.println(userByid);
    }

    @Test
    public void upDataTest(){
        User user = new User();
        user.setName("yyy");
        user.setAge(200);
        user.setId(28);
        new userDao().upData(user);
        User userByid = new userDao().findUserByid(user.getId());
        System.out.println(userByid);
    }
}
