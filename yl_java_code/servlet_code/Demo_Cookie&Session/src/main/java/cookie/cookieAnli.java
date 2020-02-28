package main.java.cookie;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.text.SimpleDateFormat;
import java.util.Date;

@WebServlet("/cookie")
public class cookieAnli extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=utf-8");
        // 获取所有的cookie
        Cookie[] cookies = request.getCookies();
        boolean temp = false;
        String value = "";
        if(cookies != null && cookies.length > 0){
            for (Cookie cookie : cookies) {
                String name = cookie.getName();
                if ("lastTime".equals(name)){
                    temp = true;
                    value = cookie.getValue();
                    break;
                }
            }
        }
        if(temp){
            //中文需要URL编码和解码才能使用
            value = URLDecoder.decode(value, "utf-8");
            response.getWriter().write("<h1>欢迎回来，您上次访问的时间是："+value+"</h1>");
            response.addCookie(getCookie());

        }else {
            response.getWriter().write("<h1>欢迎访问本站，这是您第一次访问哦！"+"</h1>");
            response.addCookie(getCookie());
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }

    public Cookie getCookie() throws UnsupportedEncodingException {
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss");
        String date_str = sdf.format(date);
        String encode = URLEncoder.encode(date_str, "utf-8");
        Cookie cookie = new Cookie("lastTime", encode);
        cookie.setMaxAge(60*60);  // 一小时
        return cookie;
    }
}
