package main.java.web.servlet;

import main.java.dao.userDao;
import main.java.domian.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/findUserServlet")
public class findUserServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 设置编码
        request.setCharacterEncoding("utf-8");
        // 获取参数id
        String id = request.getParameter("id");
        // 用参数查找出对应用户的所有信息
        User user = new userDao().findUserByid(Integer.parseInt(id));
        // 存储数据 请求转发
        request.setAttribute("userbyid",user);
        request.getRequestDispatcher("/updata.jsp").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
