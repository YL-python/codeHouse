package yang.muyun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.support.SessionStatus;
import yang.muyun.domain.Account;
import yang.muyun.domain.User;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Date;
import java.util.Map;

// 控制器类
@Controller
@RequestMapping("/anno")
// 把 msg=美美  存到session域中
@SessionAttributes(value = {"msg"})
public class annoController {

    @RequestMapping(path = "/testRequestParam")
    public String testRequestParam(@RequestParam(value = "name") String username) {
        System.out.println(username);
        return "success";
    }

    @RequestMapping(path = "/testRequestBody")
    public String testRequestBody(@RequestBody() String body) {
        System.out.println(body);
        return "success";
    }

    @RequestMapping(path = "/testPathVariable/{sid}")
    public String testPathVariable(@PathVariable(value = "sid") String id) {
        System.out.println(id);
        return "success";
    }

    @RequestMapping(path = "/testRequestHeader")
    public String testRequestHeader(@RequestHeader(value = "Accept") String header) {
        System.out.println(header);
        return "success";
    }

    @RequestMapping(path = "/testCookieValue")
    public String testCookieValue(@CookieValue(value="JSESSIONID") String cookieValue) {
        System.out.println(cookieValue);
        return "success";
    }

    @RequestMapping(path = "/testModelAttribute")
    public String testModelAttribute(@ModelAttribute(value = "abc") User user) {
        System.out.println("testModelAttribute方法执行了。。。");
        System.out.println(user);
        return "success";
    }

    @ModelAttribute
    public void showUSer(String uname, Map<String, User> map) {
        System.out.println("showUSer方法执行了。。。");
        // 模拟查询数据库
        User user = new User();
        user.setUname(uname);
        user.setUage(20);
        user.setUdate(new Date());
        map.put("abc", user);
    }

    /*
    @ModelAttribute
    public User showUSer(String uname) {
        System.out.println("showUSer方法执行了。。。");
        // 模拟查询数据库
        User user = new User();
        user.setUname(uname);
        user.setUage(20);
        user.setUdate(new Date());
        return user;
    }
     */

    @RequestMapping(path = "/testSessionAttributes")
    public String testSessionAttributes(Model model) {
        System.out.println("testSessionAttributes 方法执行了。。。");
        model.addAttribute("msg", "美美");
        return "success";
    }

    @RequestMapping(path = "/getSessionAttributes")
    public String getSessionAttributes(ModelMap model) {
        System.out.println("getSessionAttributes 方法执行了。。。");
        System.out.println(model.get("msg"));
        return "success";
    }

    @RequestMapping(path = "/delSessionAttributes")
    public String delSessionAttributes(SessionStatus status) {
        System.out.println("delSessionAttributes 方法执行了。。。");
        status.setComplete();
        return "success";
    }

}
