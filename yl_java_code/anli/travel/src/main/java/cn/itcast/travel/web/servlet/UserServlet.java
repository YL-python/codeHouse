package cn.itcast.travel.web.servlet;

import cn.itcast.travel.domain.ResultInfo;
import cn.itcast.travel.domain.User;
import cn.itcast.travel.service.UserService;
import cn.itcast.travel.service.impl.UserServiceImpl;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

@WebServlet("/user/*")
public class UserServlet extends BaseServlet {

    //声明UserService业务对象
    private UserService userService = new UserServiceImpl();

    // 注册功能
    public void regist(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 0.校验验证码
        String check = request.getParameter("check");
        // 从session中获取验证码
        HttpSession session = request.getSession();
        String checkcode_server = (String) session.getAttribute("CHECKCODE_SERVER");
        // 每一次校验都清楚一次
        session.removeAttribute("CHECKCODE_SERVER");

        // 验证码错误
        if(checkcode_server==null || !checkcode_server.equalsIgnoreCase(check)){
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
//        UserService userService = new UserServiceImpl();
//        System.out.println("发送激活码");
        boolean flag = userService.userRegist(user);
//        System.out.println(flag);
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
//        ObjectMapper mapper = new ObjectMapper();
//        String json = mapper.writeValueAsString(info);

        // 返回数据   设置数据类型是json
//        response.setContentType("application/json;charset=utf-8");
////        response.getOutputStream().write();    // 写字节流数据的
//        System.out.println("regist方法执行完毕");
//        response.getWriter().write(json);
        writerValue(info,response);

    }

    // 登录功能
    public void login(HttpServletRequest request, HttpServletResponse response) throws IOException {
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
//        UserService userService = new UserServiceImpl();
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
//        ObjectMapper mapper = new ObjectMapper();
//        // 返回数据   设置数据类型是json
//        response.setContentType("application/json;charset=utf-8");
//        mapper.writeValue(response.getOutputStream(),info);
        writerValue(info,response);
    }

    // 主页面名称展示方法
    public void findOne(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取用户信息 回写数据
        User user = (User) request.getSession().getAttribute("user");
        // 把 user 对象变成 json 返回
        ObjectMapper mapper = new ObjectMapper();
        // 返回数据   设置数据类型是json
//        response.setContentType("application/json;charset=utf-8");
//        mapper.writeValue(response.getOutputStream(),user);
        writerValue(user,response);
    }

    // 退出登录功能
    public void exit(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1.销毁session
        request.getSession().invalidate();

        // 跳转到登录页面
        // 使用重定向需要加虚拟路径
        response.sendRedirect(request.getContextPath()+"/login.html");
    }

    // 激活功能
    public void active(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取激活码
        String code = request.getParameter("code");
        if(code != null){
            // 调用service激活用户
            // UserService userService = new UserServiceImpl();
            boolean flag = userService.activeUser(code);
            String msg;
            if(flag){
                // 激活成功
                msg = "激活成功！请 <a href='../login.html'>登录</a>";
            }else {
                // 激活失败
                msg = "激活失败！请联系管理员！";
            }
//            response.setContentType("text/html;charset=utf-8");
//            response.getWriter().write(msg);
            writerValue(msg,response);
        }
    }
}
