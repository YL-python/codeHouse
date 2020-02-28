package main.java.web.servletcontext;

import main.java.utils.DownLoadUtils;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.FileInputStream;
import java.io.IOException;

@WebServlet("/downloadServlet")
public class DownlaodServlat extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doPost(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // 获取请求参数
        String filename = req.getParameter("filename");
        // 加载文件进内存
        ServletContext servletContext = this.getServletContext();
        String realPath = servletContext.getRealPath("/images/" + filename);
        FileInputStream fis = new FileInputStream(realPath);

        // 设置响应头
        String mimeType = servletContext.getMimeType(filename);
        resp.setHeader("Content-Type", mimeType);

        // 解决中文名称乱码问题
        String useragent = req.getHeader("user-agent");
        filename = DownLoadUtils.getFileName(useragent, filename);
        resp.setHeader("Content-disposition", "attachment;filename=" + filename);

        // 吧输入流中的数据写入到输出流中
        ServletOutputStream outputStream = resp.getOutputStream();
        byte[] buff = new byte[1024 * 8];
        int len = 0;

        while ((len = fis.read(buff)) != -1) {
            outputStream.write(buff, 0, len);
        }
        fis.close();
//
    }
}
