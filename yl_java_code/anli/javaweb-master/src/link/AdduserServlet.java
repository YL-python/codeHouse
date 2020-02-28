package link;

import db.Database;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "AdduserServlet",urlPatterns = "/regist.jsp")
public class AdduserServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String username = request.getParameter("username");
        String password = request.getParameter("password1");
        System.out.println(username);
        System.out.println(password);
        Database database=new Database();
        String sql1="insert into user(name,password)values('"+username+"','"+password+"')";
//        String sql1="insert into user values('"+name_send+"','"+phone_send+"')";
//        String sql1="insert into good VALUES(4,'asd',23,'d','sda',325,'dsf','dcs',34,34)";
        try {
            database.Database(sql1);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        response.sendRedirect("login2.jsp");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
