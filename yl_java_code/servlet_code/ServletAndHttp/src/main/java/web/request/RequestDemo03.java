package main.java.web.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.channels.ClosedByInterruptException;
import java.util.Enumeration;

/*
    2019年11月7日15点07分
* 演示request的常用方法 获取请求体的方法
* */

@WebServlet("/request3")
public class RequestDemo03 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        BufferedReader br = req.getReader();
        String line = null;
        while ((line = br.readLine()) != null){
            System.out.println(line);
        }
    }
}
