package main.java.web.servlet;

import main.java.dao.userDao;
import main.java.domian.User;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

@WebServlet("/updataServlet")
public class UpdataServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 修改编码
        request.setCharacterEncoding("utf-8");
        // 获取参数 封装数据
        Map<String, String[]> parameterMap = request.getParameterMap();
        User setuser = new User();
        try {
            BeanUtils.populate(setuser,parameterMap);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
        // 修改数据
        new userDao().upData(setuser);
        // 返回用户信息列表
        response.sendRedirect(request.getContextPath()+"/userListServlet");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
