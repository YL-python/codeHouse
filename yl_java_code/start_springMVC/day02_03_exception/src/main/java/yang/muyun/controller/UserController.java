package yang.muyun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import yang.muyun.exception.SysException;

@Controller
@RequestMapping("/user")
public class UserController {

    @RequestMapping("/testException")
    public String testException() throws Exception{
        System.out.println(" testException 方法执行。。。");

        try {
            int a = 10 / 0;
        } catch (Exception e) {
            e.printStackTrace();
            throw new SysException("查询所有用户出现了问题。。。");
        }

        return "success";
    }
}
