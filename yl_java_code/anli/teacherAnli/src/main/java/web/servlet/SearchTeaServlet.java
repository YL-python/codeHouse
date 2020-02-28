package main.java.web.servlet;

import main.java.dao.UserDao;
import main.java.domain.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.List;

@WebServlet("/searchTeaServlet")
public class SearchTeaServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 修改编码
        request.setCharacterEncoding("utf-8");
        // 获取参数
        String tea_num = request.getParameter("tea_num");
        HttpSession session = request.getSession();
        session.setAttribute("tea_num",tea_num);
        // 获取用户列表
        List<User> users = new UserDao().findUserByNum(Integer.parseInt(tea_num));
        // 获取session
        session.setAttribute("teachers",users);
        // 存储数据
        // 重定向
        response.sendRedirect(request.getContextPath()+"/list.jsp");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
