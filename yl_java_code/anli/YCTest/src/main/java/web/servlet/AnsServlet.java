package main.java.web.servlet;

import main.java.dao.StudentDao;
import main.java.domain.Student;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;
import java.util.Set;

@WebServlet("/ansServlet")
public class AnsServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //  设置编码
        request.setCharacterEncoding("utf-8");
        // 封装数据
        Student student = new Student();
        Map<String, String[]> parameterMap = request.getParameterMap();
        try {
            BeanUtils.populate(student,parameterMap);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }

        String id = request.getParameter("id");
        student.setId(Integer.parseInt(id));
        String name = request.getParameter("name");
        student.setName(name);

        // 存到数据库里面
        new StudentDao().upDataForAns(student);
        request.setAttribute("student",student);
        request.getRequestDispatcher("/over.jsp").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
