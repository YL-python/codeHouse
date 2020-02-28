package cn.itcast.travel.web.servlet;

import com.fasterxml.jackson.databind.ObjectMapper;

import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class BaseServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp){
        //完成方法分发
        //1.获取请求路径
        String uri = req.getRequestURI(); //   /travel/user/add
//        System.out.println("请求uri:"+uri);//  /travel/user/add
        //2.获取方法名称
        String methodName = uri.substring(uri.lastIndexOf('/') + 1);
//        System.out.println("方法名称："+methodName);
        //3.获取方法对象Method
        //谁调用我？我代表谁
//        System.out.println(this);//UserServlet的对象cn.itcast.travel.web.servlet.UserServlet@4903d97e
        try {
            //获取方法
            Method method = this.getClass().getMethod(methodName, HttpServletRequest.class, HttpServletResponse.class);
            //4.执行方法
            method.invoke(this,req,resp);
//            System.out.println(methodName+"被执行");

            // 方法名是protected，不能被直接获取 用暴力反射能解决问题但是不太好，好的是把我们要的方法的修饰符改成public
            // Method method2 = this.getClass().getDeclaredMethod(methodName, HttpServletRequest.class, HttpServletResponse.class);
            //暴力反射
            //method.setAccessible(true);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 把传入的数据转成json写回客户端
    public void writerValue(Object obj,HttpServletResponse response) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        response.setContentType("application/json;charset=utf-8");
        mapper.writeValue(response.getOutputStream(),obj);
    }

    // 把传入的数据转成json字符串在返回
    public String writerValueAsString(Object obj,HttpServletResponse response) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        return mapper.writeValueAsString(obj);
    }
}
