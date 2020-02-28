package main.java.cookie;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/cookie04")
public class CookieDemo04 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 创建cookie对象
        Cookie c1 = new Cookie("msg","helloWorld");

        // 设置cookie的存活时间
        c1.setMaxAge(30);  // 把cookie信息存到硬盘内，30秒后删除
        // c1.setMaxAge(-1);  // 默认方式
        // c1.setMaxAge(0);  // 删除信息

        // 发送cookie
        resp.addCookie(c1);
    }
}
