package main.java.web.filter;

import main.java.domian.Admin;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

@WebFilter("/*")
public class loginFilter implements javax.servlet.Filter {
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {
        // 强转  只有HTTPServlet里面才有对应的方法
        HttpServletRequest requests = (HttpServletRequest) req;
        // 获取资源路径
        String requestURI = requests.getRequestURI();
        // 排处和登录有关的资源  js/css/图片/一些不要要登录就能访问的页面   checkCodeServlet
        if(requestURI.contains("/login.jsp") || requestURI.contains("/index.jsp") || requestURI.contains("/loginServlet") || requestURI.contains("/checkCodeServlet") || requestURI.contains("/css/") || requestURI.contains("/js/") || requestURI.contains("/fonts/")){
            // 表示用户就是想登录  放行
            chain.doFilter(req, resp);
        }else{  // 判断用户登录过了
            Admin admin = (Admin) requests.getSession().getAttribute("admin");
            if(admin != null){
                // 表示用户登录过了  放行
                chain.doFilter(req, resp);
            }else {
                // 表示没有登录，跳转登录页面
                req.setAttribute("login_msg","您未登录，请登录");
                requests.getRequestDispatcher("/login.jsp").forward(req,resp);
            }

        }




    }

    public void init(FilterConfig config) throws ServletException {
    }

    public void destroy() {
    }
}
