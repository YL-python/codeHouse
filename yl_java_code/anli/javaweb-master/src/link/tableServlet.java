package link;

import db.DBbean;
import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;
import java.util.Enumeration;

@WebServlet(name = "tableServlet",urlPatterns = "/tableServlet")
public class tableServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        for (int i = 1; i <= 20; i++) {

//            request.getParameter(k + "i");
            int id = i;
            String name = request.getParameter("k"+i);
            String teacher = request.getParameter("teacher"+i);
            System.out.println(i);
            if (name==null){
                name="";
            }
            if (teacher==null){teacher="";}
            Database database = new Database();
            String sql = "update coursetable set name='"+name+"' ,teachers='"+teacher+"'  where ID=" +id;
            System.out.println(sql);
            try {
                database.Database(sql);
            } catch (SQLException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
        }
        response.sendRedirect("showtable.jsp");

    }
}