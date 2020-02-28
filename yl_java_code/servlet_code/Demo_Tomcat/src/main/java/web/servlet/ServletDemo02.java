package main.java.web.servlet;

/*
2019年11月6日15点12分
servlet的方法解释
*/

import javax.servlet.*;
import java.io.IOException;

public class ServletDemo02 implements Servlet {

    // init初始化方法，在servlet被创建时执行（访问的时候创建）   只会执行一次
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {
        System.out.println("init方法被执行啦!");
    }

    // 获取ServletConfig对象  servlet的配置对象
    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    // 提供服务的方法，每一次 Servlet 被访问都会执行，执行多次
    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        System.out.println("service方法被执行啦!");
    }

    // 获取servlet的一些信息   版本 作者等等
    @Override
    public String getServletInfo() {
        return null;
    }

    // 销毁方法 在Servlet被杀死时候执行 （服务器正常关闭）
    @Override
    public void destroy() {
        System.out.println("destroy方法被执行啦!");
    }
}
