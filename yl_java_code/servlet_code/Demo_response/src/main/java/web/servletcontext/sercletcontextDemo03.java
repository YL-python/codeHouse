package main.java.web.servletcontext;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/context03")
public class sercletcontextDemo03 extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req,resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // ServletContext 对象 获取文件真实路径
        ServletContext context = this.getServletContext();

        // 获取文件服务器路径
        // 配置文件可以放在 src下，web下，WEB-INF下
        String realPathB = context.getRealPath("/b.txt");  //  /斜杠表示web目录 下的文件
        System.out.println(realPathB);

        String realPathC = context.getRealPath("/WEB-INF/c.txt");  //   web下的WEB-INF目录内的文件
        System.out.println(realPathC);

        String realPathA = context.getRealPath("/WEB-INF/classes/a.txt");  //  访问src目录下的文件
        System.out.println(realPathA);


    }
}
