package link;

import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "ShowlistServlet",urlPatterns = "/ShowlistServlet")
public class ShowlistServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String ID=request.getParameter("ID");
        String course=request.getParameter("course");
        String xingqi=request.getParameter("xingqi");
        String jie=request.getParameter("jie");
//        String sql="delete from sc where ID="+ID+"and course='"+course+"' and xingqi1='"+xingqi+"' and jie1='"+jie+"'";
        String sql="delete from sc where  ID="+ID+" and course='"+course+"' and xingqi1='"+xingqi+"' and jie1='"+jie+"'";
        System.out.println(sql);
        Database database=new Database();
        try {
            database.Database(sql);
            response.sendRedirect("showalllist.jsp");
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
