package link;

import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "DelcorServlet",urlPatterns = "/DelcorServlet")
public class DelcorServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String ID=request.getParameter("ID");
        String course=request.getParameter("course");
        String xingqi1=request.getParameter("xingqi");
        String jie1=request.getParameter("jie");
        String sql="delete from course where ID="+ID+"";
        System.out.println(sql);
        Database database=new Database();
        try {
            database.Database(sql);
            response.sendRedirect("showcourse.jsp");
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
