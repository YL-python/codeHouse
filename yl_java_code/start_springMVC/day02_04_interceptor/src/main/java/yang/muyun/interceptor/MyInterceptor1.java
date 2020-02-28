package yang.muyun.interceptor;

import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class MyInterceptor1 implements HandlerInterceptor {

    // 预处理方法 在 controller方法执行之前执行
    // 返回值是 true表示放行，进入到下一个拦截器，没有就执行 controller方法
    // 返回值是 false表示不放行，可以用 原生 HTTP对象进行跳转
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        System.out.println("拦截器 1 预处理方法 执行了");
        return true;
        // request.getRequestDispatcher("/WEB-INF/pages/error.jsp").forward(request,response);
        // return false;
    }

    // 后处理方法
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        System.out.println("拦截器 1 后处理方法 执行了");
    }

    // success.jsp 执行完毕之后执行的方法
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        System.out.println("拦截器 1 最后处理方法 执行了");
    }
}
