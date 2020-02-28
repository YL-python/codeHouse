package link;

import db.Database;
import db.DatabaseQuery;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

@WebServlet(name = "searchstuServlet",urlPatterns = "/searchstuServlet")
public class searchstuServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
String ID=request.getParameter("search");
        String sql="select * from sc where ID='"+ID+"'";
        Database database=new Database();
        ResultSet result= null;
        try {
            result = database.a(sql);
            request.setAttribute("result",result);
            RequestDispatcher requestDispatcher = this.getServletContext().getRequestDispatcher("/showsturesult.jsp");
            requestDispatcher.forward(request, response);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        System.out.println(ID);
        System.out.println(sql);

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
