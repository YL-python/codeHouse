package main.java.web.servlet;

import main.java.dao.userDao;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/delCheckUserServlet")
public class DelCheckUserServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取所有的参数
        String[] uids = request.getParameterValues("uid");
        // 遍历删除
        if(uids!=null && uids.length>0){
            userDao dao = new userDao();
            for (String uid : uids) {
                dao.delUserByid(Integer.parseInt(uid));
            }
        }
        // 跳转到查找页面
        response.sendRedirect(request.getContextPath()+"/findUserByPageServlet");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
