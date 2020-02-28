package yang.muyun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import yang.muyun.domain.Account;
import yang.muyun.domain.User;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// 控制器类
@Controller
@RequestMapping("/param")
public class ParamController {

    @RequestMapping(path = "/nameAndpassword")
    public String nameAndpassword(String username, String password) {
        System.out.println("用户名："+username);
        System.out.println("密码："+password);
        return "success";
    }

    @RequestMapping(path = "/saveAccount", method = {RequestMethod.POST})
    public String saveAccount(Account account) {
        System.out.println("用户名："+account);
        return "success";
    }

    @RequestMapping(path = "/saveUser", method = {RequestMethod.POST})
    public String saveUser(User u) {
        System.out.println("用户名："+u);
        return "success";
    }

    @RequestMapping(path = "/testServlet")
    public String testServlet(HttpServletRequest request, HttpServletResponse response) {
        System.out.println(request);
        System.out.println(response);
        System.out.println(request.getSession());
        System.out.println(request.getSession().getServletContext());
        return "success";
    }

}
