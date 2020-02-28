package main.java.web.filter;

import javax.servlet.*;
import java.io.IOException;

//@WebFilter("/*")
public class FilterDemo03 implements Filter {
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("init方法执行了...");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        // 对request对象执行的消息增强
        System.out.println("filter被执行了---");

        // 放行
        filterChain.doFilter(servletRequest,servletResponse);

        // 对response消息的数据增强
        // System.out.println("filter回来了。。。。");
    }

    @Override
    public void destroy() {
        System.out.println("destroy方法执行了。。。");
    }
}
