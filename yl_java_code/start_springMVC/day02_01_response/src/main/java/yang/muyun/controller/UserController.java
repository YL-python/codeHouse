package yang.muyun.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;
import yang.muyun.domain.User;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Controller
@RequestMapping("/user")
public class UserController {

    @RequestMapping("/testString")
    public String testString(Model model) {
        System.out.println(" testString 方法执行了。。。");

        // 模拟查询数据库
        User user = new User();
        user.setUsername("zhangsan");
        user.setPassword("123");
        user.setAge(18);
        // 把数据存到 request 域
        model.addAttribute("user", user);

        return "success";
    }

    @RequestMapping("/testVoid")
    public void testVoid(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println(" testVoid 方法执行了。。。");
        // 没有返回值会默认跳转到 路径下的文件

        // 可以自己进行资源转发, 是一个请求，不用写项目路径
        // 在服务器内部 需要写 /WEB-INF/pages/
        // request.getRequestDispatcher("/WEB-INF/pages/success.jsp").forward(request,response);

        // 可以自己进行重定向, 是两个请求，需要写项目路径
        // 在服务器外部 不需要写 /WEB-INF/pages/
        // response.sendRedirect(request.getContextPath() + "/index.jsp");

        // 设置中文乱码
        response.setCharacterEncoding("UTF-8");
        response.setContentType("text/html;charset=UTF-8");
        // 直接进行响应
        response.getWriter().print("hahahhah 你好");

        System.out.println("后续代码  11  。。。");
        return;
        // System.out.println("后续代码  22  。。。");
    }

    @RequestMapping("/testModelAndView")
    public ModelAndView testModelAndView() {
        System.out.println(" testModelAndView 方法执行了。。。");

        // 创建 ModelAndView 对象
        ModelAndView mv = new ModelAndView();

        // 模拟查询数据库
        User user = new User();
        user.setUsername("小小");
        user.setPassword("123");
        user.setAge(18);

        // 把数据存到 mv 对象中，底层实现是 ModelMap 就是会把数据存到 request 域对象中
        mv.addObject("user", user);

        // 跳转到那个页面  使用试图解析器
        mv.setViewName("success");
        return mv;
    }

    @RequestMapping("/testForwardOrRedirect")
    public String testForwardOrRedirect() {
        System.out.println(" testForwardOrRedirect 方法执行了。。。");

        // 请求转发
        // return "forward:/WEB-INF/pages/success.jsp";

        // 重定向  不需要加项目名称，底层会帮我们加
        return "redirect:/index.jsp";
    }

    @RequestMapping("/testAjax")
    public @ResponseBody
    User testAjax(@RequestBody User user) {
        System.out.println(" testAjax 方法执行了。。。");
        // 前端传json数据 后台已经帮我们封装到user对象内了
        System.out.println(user);
        // 模拟查询数据库
        user.setUsername("xiaomin");
        user.setAge(40);
        // 做响应
        return user;
        // 返回对象，框架会 因为ResponseBody注解 帮我们吧数据转成json数据 并且返回
    }

}
