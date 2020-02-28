package main.java.web.servlet;

import main.java.dao.userDao;
import main.java.domian.Admin;
import main.java.domian.User;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.List;
import java.util.Map;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 修改编码
        request.setCharacterEncoding("utf-8");
        // 接收数据
        String vcode = request.getParameter("vcode");
        // 验证码判断
        HttpSession session = request.getSession();
        String checkcode_server =(String) session.getAttribute("CHECKCODE_SERVER");
        session.removeAttribute("CHECKCODE_SERVER");  // 把获取的验证码信息清楚保证验证码是一次性的
        // 防止验证码空指针异常
        checkcode_server = (checkcode_server == null) ? "" : checkcode_server;
        vcode = (vcode == null) ? "" : vcode;
        if(! vcode.equalsIgnoreCase(checkcode_server)){
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
        Admin rea = new userDao().loginAdmin(admin);
        if(rea != null){
            // 登录成功
            // 把用户信息存到Session中
            session.setAttribute("admin", rea);
            // 查询所有数据存到request中
//            userDao dao = new userDao();
//            List<User> allUser = dao.findAllUser();
//            request.setAttribute("users",allUser);
            // 把所有信息存到request 中
            String citystr = "北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区";
            String[] citys = citystr.split("，");
            session.setAttribute("citys",citys);
            // 跳转到信息页面
            response.sendRedirect(request.getContextPath()+"/findUserByPageServlet");
//            request.getRequestDispatcher("/findUserByPageServlet").forward(request,response);
        }else{
            // 用户名或密码错误
            request.setAttribute("login_msg","用户名或密码错误！");
            // 跳转到登录页面
            request.getRequestDispatcher("/login.jsp").forward(request,response);
        }
    }
}
