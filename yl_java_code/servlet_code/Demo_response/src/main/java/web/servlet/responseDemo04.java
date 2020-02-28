package main.java.web.servlet;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

// 2019年11月9日09点34分
// 在浏览器页面上输出字节数据

@WebServlet("/demo04")
public class responseDemo04 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req,resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        resp.setContentType("text/html;charset=utf-8");
        // 获取字节输出流
        ServletOutputStream sos = resp.getOutputStream();
        // 输出数据
        sos.write(32);
        sos.write("hello".getBytes());
    }
}
