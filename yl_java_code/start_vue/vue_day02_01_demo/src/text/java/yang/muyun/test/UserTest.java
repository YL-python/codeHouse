package yang.muyun.test;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import yang.muyun.domain.User;
import yang.muyun.service.IUserService;

import java.util.List;

/**
 * 用户的业务层测试
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:applicationContext.xml")
public class UserTest {

    @Autowired
    private IUserService userService;

    @Test
    public void test(){
        System.out.println(1);
    }

    @Test
    public void testFindAll(){
        List<User> users = userService.findAll();
        System.out.println(users);
    }

    @Test
    public void testFindOne(){
        User user = userService.findById(1);
        System.out.println(user);
    }

    @Test
    public void testUpdate(){
        User user = userService.findById(1);
        System.out.println("修改之前的用户"+user);

        user.setAge(55);
        userService.updateUser(user);

        user = userService.findById(1);
        System.out.println("修改之后的用户"+user);
    }
}
