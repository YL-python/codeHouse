package main.java.web.request;

import javax.servlet.RequestDispatcher;
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
* 演示request的常用方法 资源跳转
* */

@WebServlet("/request5")
public class RequestDemo05 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("555555555被调用");
//        RequestDispatcher requestDispatcher = req.getRequestDispatcher("/request6");
//        requestDispatcher.forward(req, resp);

        // 转发之前存储数据到 request域中
        req.setAttribute("msg","hello");

        req.getRequestDispatcher("/request6").forward(req, resp);
    }
}
