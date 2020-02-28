package cn.itcast.travel.web.servlet.old;

import cn.itcast.travel.domain.ResultInfo;
import cn.itcast.travel.domain.User;
import cn.itcast.travel.service.UserService;
import cn.itcast.travel.service.impl.UserServiceImpl;
import com.fasterxml.jackson.databind.ObjectMapper;
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
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 0.校验验证码
        String check = request.getParameter("check");
        // 从session中获取验证码
        HttpSession session = request.getSession();
        String checkcode_server = (String) session.getAttribute("CHECKCODE_SERVER");
        // 每一次校验都清楚一次
        session.removeAttribute("CHECKCODE_SERVER");

        // 验证码错误
        if(checkcode_server==null || ! checkcode_server.equalsIgnoreCase(check)){
            // 后端和前端之间响应结果信息的对象
            ResultInfo info = new ResultInfo();
            // 验证码错误
            info.setFlag(false);
            info.setErrorMsg("验证码错误!");
            // 把 info 对象变成 json 返回
            ObjectMapper mapper = new ObjectMapper();
            String json = mapper.writeValueAsString(info);
            // 返回数据   设置数据类型是json
            response.setContentType("application/json;charset=utf-8");
            response.getWriter().write(json);
            return;
        }

        // 获取登录的账号密码
        Map<String, String[]> map = request.getParameterMap();
        User user = new User();
        try {
            BeanUtils.populate(user,map);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
        // 调用service判断用户是否存在和激活状态
        UserService userService = new UserServiceImpl();
        ResultInfo info = new ResultInfo();
        User u = userService.login(user);
        if(u == null){
            // 用户名或密码错误
            info.setFlag(false);
            info.setErrorMsg("用户名或密码错误");
        }
        if(u != null && !"Y".equals(u.getStatus())){
            // 用户名没有激活
            info.setFlag(false);
            info.setErrorMsg("您尚未激活，请登录邮箱激活");
        }
        if(u != null && "Y".equals(u.getStatus())){
            // 登陆成功判断
            info.setFlag(true);
            request.getSession().setAttribute("user",u);
        }

        // 把 info 对象变成 json 返回
        ObjectMapper mapper = new ObjectMapper();
        // 返回数据   设置数据类型是json
        response.setContentType("application/json;charset=utf-8");
        mapper.writeValue(response.getOutputStream(),info);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
