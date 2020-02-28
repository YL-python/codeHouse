package main.java.web.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Enumeration;
import java.util.Iterator;

/*
    2019年11月7日15点07分
* 演示request的常用方法 获取请求头的方法
* */

@WebServlet("/request2")
public class RequestDemo02 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        /* (*)String getHeader(String name):通过请求头的名称获取请求头的值
         * Enumeration<String> getHeaderNames():获取所有的请求头名称 */

        // 获取所有请求头名称
        Enumeration<String> headerNames = req.getHeaderNames();
        // 遍历
        while (headerNames.hasMoreElements()) {
            String name = headerNames.nextElement();
            // 通过名称获取值
            String value = req.getHeader(name);
            System.out.println(name + "---" + value);
        }
        System.out.println("=======================");

        // 不同的头对应不同的操作
        String agent = req.getHeader("user-agent");
        if (agent.contains("Chrome")) {
            System.out.println("谷歌浏览器" + agent);
        } else if (agent.contains("Firefox")) {
            System.out.println("火狐浏览器" + agent);
        } else {
            System.out.println("其他浏览器" + agent);
        }

        System.out.println("=======================");
        // 我从哪里来   referer
        String referer = req.getHeader("referer");
        System.out.println(referer);
        if(referer !=null){
            if(referer.contains("/day")){
                System.out.println("通过正常访问跳转的");
                // 显示不了中文，设置编码
                resp.setContentType("text/html;charset=utf-8");
                resp.getWriter().write("通过正常访问跳转的");
            }else {
                System.out.println("非正常访问");
                resp.setContentType("text/html;charset=utf-8");
                resp.getWriter().write("非正常访问");
            }
        }

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

    }
}
