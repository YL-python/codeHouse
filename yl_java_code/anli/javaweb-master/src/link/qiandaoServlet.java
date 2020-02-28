package link;

import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "qiandaoServlet",urlPatterns = "/qiandaoServlet")
public class qiandaoServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
    String ID=request.getParameter("ID");
        String course=request.getParameter("course");
        String xingqi=request.getParameter("xingqi");
        String jie=request.getParameter("jie");

    String shi="是";
    String sql="update sc set qiandao='"+shi+"'where ID="+ID+" and course='"+course+"' and xingqi1='"+xingqi+"' and jie1='"+jie+"'";
        System.out.println(sql);
        System.out.println(ID);
        Database database=new Database();
        try {
            database.Database(sql);

        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        response.sendRedirect("nocheck.jsp");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
