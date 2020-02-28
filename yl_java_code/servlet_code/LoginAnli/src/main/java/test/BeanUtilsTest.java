package main.java.test;

import main.java.domain.User;
import org.apache.commons.beanutils.BeanUtils;
import org.junit.Test;

import java.lang.reflect.InvocationTargetException;

public class BeanUtilsTest {
    @Test
    public void BeanUtilstest() throws InvocationTargetException, IllegalAccessException {
        User user = new User();
        BeanUtils.setProperty(user,"username","zhangsan");
        System.out.println(user);
    }
}
