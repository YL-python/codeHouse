package yang.muyun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

// 控制器类
@Controller
@RequestMapping("/user")
public class HelloController {

    @RequestMapping(path = "/hello")
    public String sayHello() {
        System.out.println("Hello SpringMVC...");
        // 返回的字符串默认是返回的页面的名称
        return "success";
    }

    @RequestMapping(path = "/save")
    public String testSave() {
        System.out.println("save方法执行...");
        return "success";
    }

}
