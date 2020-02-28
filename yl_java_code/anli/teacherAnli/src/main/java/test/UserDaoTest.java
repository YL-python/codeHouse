package main.java.test;

import main.java.dao.UserDao;
import main.java.domain.User;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class UserDaoTest {
    @Test
    public void addUsersTest(){
        User user = new User(1, "zhangsan", "123123", "大数据", 0);
        ArrayList<User> users = new ArrayList<>();
        users.add(user);
        new UserDao().addUsers(users);
    }

    @Test
    public void getUsersTest(){
        List<User> users = new UserDao().getUsers();
        System.out.println(users);
    }

    @Test
    public void findUserByNumTest(){
        List<User> users = new UserDao().findUserByNum(6);
        System.out.println(users);
    }

    @Test
    public void findUserBeforeIDTest(){
        User userBeforeID = new UserDao().findUserBeforeID(5);
        System.out.println(userBeforeID);
    }

}
