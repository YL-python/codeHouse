package main.java.web.servlet;

import main.java.dao.UserDao;
import main.java.domain.User;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doGet(req, resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 设置编码
        req.setCharacterEncoding("utf-8");
//        // 获取请求参数
//        String username = req.getParameter("username");
//        String password = req.getParameter("password");
////        封装User对象
//        User loginuser = new User();
//        loginuser.setUsername(username);
//        loginuser.setPassword(password);

        Map<String, String[]> parameterMap = req.getParameterMap();
        // 创建一个空对象
        User loginuser = new User();
        // 使用工具类
        try {
            BeanUtils.populate(loginuser,parameterMap);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }

        // 调用Userdao
        User user = new UserDao().login(loginuser);
        // 判断user
        if(user == null){
            //登陆失败
            req.getRequestDispatcher("/failServlet").forward(req,resp);

        }else{
            // 登录成功
            // 存储数据
            req.setAttribute("user",user);
            // 转发数据
            req.getRequestDispatcher("/successServlet").forward(req,resp);
        }
    }
}
