package main.java.web.servlet;

import main.java.dao.StudentDao;
import main.java.domain.Student;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {
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
        // 存到数据库里面
        int id = new StudentDao().addStudent(student);
        int test = id%3+1;
        student.setId(id);
        student.setTest(test);
        request.setAttribute("student",student);
        // 资源转发
        request.getRequestDispatcher("/test"+String.valueOf(test)+".jsp").forward(request,response);
    }


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
