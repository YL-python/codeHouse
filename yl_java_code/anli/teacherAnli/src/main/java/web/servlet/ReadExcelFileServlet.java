package main.java.web.servlet;

import main.java.dao.UserDao;
import main.java.domain.User;
import main.java.excel.ExcelReader;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/readExcelFileServlet")
public class ReadExcelFileServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 设置编码
        request.setCharacterEncoding("utf-8");
        // 获取路径
        String FilePath = request.getParameter("readFilePath");
//        System.out.println(FilePath);
        // 读取用户数据列表
        List<User> users = new ExcelReader().readexcel(FilePath);
        // 写入数据库
        new UserDao().addUsers(users);
        // 跳转
        request.setAttribute("readOrWriteFileMsg","excel数据导入数据库成功");
        request.getRequestDispatcher("/list.jsp").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
