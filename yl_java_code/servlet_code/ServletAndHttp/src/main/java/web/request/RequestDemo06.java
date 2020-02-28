package main.java.web.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Enumeration;
import java.util.Map;
import java.util.Set;

/*
    2019年11月7日15点07分
* 演示request的常用方法 通用获取请求参数方法
* */

@WebServlet("/request6")
public class RequestDemo06 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取数据
        Object msg = req.getAttribute("msg");
        System.out.println(msg);

        System.out.println("6666666666666被调用");
    }
}
