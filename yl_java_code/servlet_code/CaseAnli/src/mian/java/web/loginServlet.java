package mian.java.web;

import mian.java.dao.UserDao;
import mian.java.domain.Admin;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

@WebServlet("/loginServlet")
public class loginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 修改编码
        request.setCharacterEncoding("utf-8");
        // 接收数据
        String vcode = request.getParameter("vcode");
        // 验证码判断
        HttpSession session = request.getSession();
        String checkcode_server =(String) session.getAttribute("CHECKCODE_SERVER");
        session.removeAttribute("CHECKCODE_SERVER");  // 把获取的验证码信息清楚保证验证码是一次性的
        System.out.println("没进入if");
        if(! checkcode_server.equalsIgnoreCase(vcode)){
            // 验证码错误
            request.setAttribute("login_msg","验证码错误！");
            // 跳转到登录页面
            request.getRequestDispatcher("/login.jsp").forward(request,response);
            return;
        }

        // 验证码正确
        // 用工具类封装数据
        Admin admin = new Admin();
        Map<String, String[]> parameterMap = request.getParameterMap();
        try {
            BeanUtils.populate(admin,parameterMap);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }

        // 调用servlet查询
        Admin rea = new UserDao().loginAdmin(admin);
        if(rea != null){
            // 登录成功
            // 把用户信息存到Session中
            session.setAttribute("admin", rea);
            // 跳转到信息页面
            response.sendRedirect(request.getContextPath()+"/list.jsp");
        }else{
            // 用户名或密码错误
            request.setAttribute("login_msg","用户名或密码错误！");
            // 跳转到登录页面
            request.getRequestDispatcher("/login.jsp").forward(request,response);
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
