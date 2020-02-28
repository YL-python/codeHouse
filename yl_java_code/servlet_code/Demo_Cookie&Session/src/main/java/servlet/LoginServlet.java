package main.java.servlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.Map;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 设置编码
        request.setCharacterEncoding("utf-8");
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String checkCode = request.getParameter("checkCode");

        // 获取session对象
        HttpSession session = request.getSession();
        String checkCodeAns =(String) session.getAttribute("checkCode");
        // 获取完之后立即删除
        session.removeAttribute("checkCode");

        if(checkCodeAns!=null && checkCodeAns.equalsIgnoreCase(checkCode)){
            if("zhansan".equals(username) && "123".equals(password)){
                // 登录成功 存信息 重定向
                session.setAttribute("username",username);
//                session.setAttribute("password",password);
                response.sendRedirect(request.getContextPath()+"/success.jsp");
            }else{
                request.setAttribute("login_error","用户名或密码错误！");
                // 内部转发的方法
                request.getRequestDispatcher("/login.jsp").forward(request,response);
            }
        }else{
            request.setAttribute("cc_error","验证码错误！");
            // 内部转发的方法
            request.getRequestDispatcher("/login.jsp").forward(request,response);
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
