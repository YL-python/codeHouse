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

@WebServlet("/modifyTeaServlet")
public class ModifyTeaServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 修改编码
        request.setCharacterEncoding("utf-8");
        // 获取参数
        String id = request.getParameter("id");
        HttpSession session = request.getSession();
        // 把count值-1
        UserDao userDao = new UserDao();
        userDao.reduceCountById(Integer.parseInt(id));

        // 在这个id后查找一条数据
        User userBeforeID = userDao.findUserBeforeID(Integer.parseInt(id));
        List<User> teachers =(List<User>) session.getAttribute("teachers");
        System.out.println("1111111111"+teachers);
        int temp = -1;
        for (User teacher : teachers) {
            if (teacher.getId() == Integer.parseInt(id)){
                temp = teachers.indexOf(teacher);
            }
        }
        if(temp!=-1){
            teachers.remove(temp);
        }

        teachers.add(userBeforeID);

        // 存储数据
        session.setAttribute("teachers",teachers);
        // 重定向
        response.sendRedirect(request.getContextPath()+"/list.jsp");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
