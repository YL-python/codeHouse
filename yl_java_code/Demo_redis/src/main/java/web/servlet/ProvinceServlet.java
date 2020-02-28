package main.java.web.servlet;

import com.fasterxml.jackson.databind.ObjectMapper;
import main.java.domain.Province;
import main.java.servies.ProvinceService;
import main.java.servies.impl.ProvinceServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/provinceServlet")
public class ProvinceServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        /*  数据库方法
        // 调用service查询
        ProvinceService servlet = new ProvinceServiceImpl();
        List<Province> provinceList = servlet.findAll();
        // 序列化List集合变成Json
        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(provinceList);
        */


        // 缓存方法
        ProvinceService servlet = new ProvinceServiceImpl();
        String json = servlet.findAllJson();  // 返回值是json字符串
        System.out.println(json);

        // 返回结果  设置响应文件为json/用流写出去就行
        response.setContentType("application/json;charset=utf-8");
        response.getWriter().write(json);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
