package link;

import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "AddcourseServlet",urlPatterns = "/AddcourseServlet")
public class AddcourseServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String coursename = request.getParameter("coursename");
        String teacher= request.getParameter("teacher");
        System.out.println(coursename);
        System.out.println(teacher);
        Database database=new Database();
        String sql1="insert into course(coursename,teacher)values('"+coursename+"','"+teacher+"')";
//        String sql1="insert into user values('"+name_send+"','"+phone_send+"')";
//        String sql1="insert into good VALUES(4,'asd',23,'d','sda',325,'dsf','dcs',34,34)";
        try {
            database.Database(sql1);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
response.sendRedirect("index.jsp");
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
