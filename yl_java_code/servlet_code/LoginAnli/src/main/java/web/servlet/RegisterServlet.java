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

@WebServlet("/RegisterServlet")
public class RegisterServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doGet(req, resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 设置编码
        req.setCharacterEncoding("utf-8");
        Map<String, String[]> parameterMap = req.getParameterMap();
        // 创建一个空对象
        User registerUser = new User();
        try {
            BeanUtils.populate(registerUser,parameterMap);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
        // id自增长
        registerUser.setId(-1);
        System.out.println(registerUser);
        // 调用Userdao
        new UserDao().register(registerUser);
        User user = new UserDao().login(registerUser);
        if(user == null){
            req.getRequestDispatcher("/RfailServlet").forward(req,resp);
        }else{
            req.getRequestDispatcher("/RsuccessServlet").forward(req,resp);
        }

    }
}
