package main.java.web.servlet;

import main.java.dao.UserDao;
import main.java.domain.User;
import main.java.excel.ExcelReader;
import main.java.excel.ExcelWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/writeExcelFileServlet")
public class WriteExcelFileServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 设置编码
        request.setCharacterEncoding("utf-8");
        // 获取参数
        String FilePath = request.getParameter("writeFilePath");
//        System.out.println(FilePath);
        // 数据库读取用户数据列表
        List<User> users = new UserDao().getUsers();
        // 写入excel
        String fileName = new ExcelWriter().writeExcel(FilePath, users);
        // 跳转
        request.setAttribute("readOrWriteFileMsg","数据库数据导出excel成功,文件保存在："+fileName);
        request.getRequestDispatcher("/list.jsp").forward(request,response);

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
