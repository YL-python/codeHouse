package main.java.servlet;

import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;

// 2019年11月9日09点34分
// 在浏览器页面上输出字节数据

@WebServlet("/check")
public class CheckCode extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req,resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        int width = 100;
        int height = 50;
//        resp.setContentType("text/html;charset=utf-8");

        // 创建一个画图对象
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        // 美化图片
        // 填充背景色   获取画笔对象
        Graphics g = image.getGraphics();
        g.setColor(Color.pink);
        g.fillRect(0,0,width,height);  // 填充方法

        // 画边框
        g.setColor(Color.BLUE);
        g.drawRect(0,0,width-1,height-1);  // 绘画方法

        // 写验证码
        String str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890";
        Random ran = new Random();
//        int index = ran.nextInt(str.length());
//        char c = str.charAt(index);
        g.setColor(Color.BLACK);
        StringBuilder sb = new StringBuilder();
        for(int i=1; i<=4; i++){
            char c = str.charAt(ran.nextInt(str.length()));
            sb.append(c);
            g.drawString(c +"",width/5*i,height/2);
        }
        String checkCode = sb.toString();

        // 把checkCode存到session中
        HttpSession session = req.getSession();
        session.setAttribute("checkCode",checkCode);

        // 画干扰线
        g.setColor(Color.GREEN);
        for(int i=1;i<=10;i++){
            int x1 = ran.nextInt(width);
            int x2 = ran.nextInt(width);
            int y1 = ran.nextInt(height);
            int y2 = ran.nextInt(height);
            g.drawLine(x1,y1,x2,y2);
        }

        // 加载图片
        ImageIO.write(image, "jpg", resp.getOutputStream());
    }
}
