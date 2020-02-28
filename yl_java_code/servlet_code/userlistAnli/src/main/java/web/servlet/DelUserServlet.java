package main.java.web.servlet;

import main.java.dao.userDao;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/delUserServlet")
public class DelUserServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 没有涉及到中文不需要修改编码
        // 获取id参数
        String id = request.getParameter("id");
        // 数据库删除对应数据
        new userDao().delUserByid(Integer.parseInt(id));
        // 查询表并跳转
//        request.getRequestDispatcher(request.getContextPath()+"/userListServlet").forward(request,response);
        response.sendRedirect(request.getContextPath()+"/findUserByPageServlet");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
