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

@WebServlet("/registerUserServlet")
public class RegisterUserServlet extends HttpServlet {
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

        // 1.获取数据
        Map<String, String[]> map = request.getParameterMap();
        // 2.封装对象
        User user = new User();
        try {
            BeanUtils.populate(user,map);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
        // 3.调用service完成注册
        UserService userService = new UserServiceImpl();
        boolean flag = userService.userRegist(user);
        // 4.响应结果
        // 后端和前端之间响应结果信息的对象
        ResultInfo info = new ResultInfo();
        if(flag){
            // 注册成功
            info.setFlag(true);
        }else {
            // 注册失败
            info.setFlag(false);
            info.setErrorMsg("注册失败!");
        }

        // 把 info 对象变成 json 返回
        ObjectMapper mapper = new ObjectMapper();
        String json = mapper.writeValueAsString(info);

        // 返回数据   设置数据类型是json
        response.setContentType("application/json;charset=utf-8");
//        response.getOutputStream().write();    // 写字节流数据的
        response.getWriter().write(json);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
