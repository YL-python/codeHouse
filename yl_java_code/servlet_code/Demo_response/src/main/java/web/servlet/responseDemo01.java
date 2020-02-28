package main.java.web.servlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

// 2019年11月9日09点34分
// 重定向案例  重定向到demo02页面

@WebServlet("/demo01")
public class responseDemo01 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req,resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("demo01被访问了。。。。");
//        访问demo01会跳转到demo02资源

////        设置状态码为302
//        resp.setStatus(302);
////        设置响应头的location
//        resp.setHeader("location","/response/demo02");
        resp.sendRedirect("/response/demo02");


    }
}
