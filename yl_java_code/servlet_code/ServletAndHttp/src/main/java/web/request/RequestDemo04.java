package main.java.web.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Collection;
import java.util.Enumeration;
import java.util.Map;
import java.util.Set;

/*
    2019年11月7日15点07分
* 演示request的常用方法 通用获取请求参数方法
* */

@WebServlet("/request4")
public class RequestDemo04 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        get获取请求参数
//        String username = req.getParameter("username");
//        System.out.println(username);
        this.doPost(req, resp);


    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//        post获取请求参数
        // 获取用户名

        // 修改编码
        req.setCharacterEncoding("utf-8");

        String username = req.getParameter("username");
        System.out.println(username);

        // 获取hobby参数
        String[] hobbies = req.getParameterValues("hobby");
        for (String hobby : hobbies) {
            System.out.println(hobby);
        }

        // 获取所有请求参数的名称
        Enumeration<String> parameterNames = req.getParameterNames();
        while (parameterNames.hasMoreElements()){
            String name = parameterNames.nextElement();
            // 用名称获取值
            String value = req.getParameter(name);
            System.out.println(name+"---"+value);
        }

        // 获取所有参数的map集合
        Map<String, String[]> parameterMap = req.getParameterMap();
        Set<String> keyset = parameterMap.keySet();
        for (String name : keyset) {
            // 根据name获取值
            String[] values = parameterMap.get(name);
            System.out.println(name);
            for (String value : values) {
                System.out.println(value);
            }
            System.out.println("==============");
        }



    }
}
