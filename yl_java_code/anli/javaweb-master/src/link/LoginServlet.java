package link;



import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import db.DBbean;

@WebServlet(name = "LoginServlet",urlPatterns = "/login1.jsp")
public class LoginServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password1");
        DBbean shujuku1=new DBbean();
        System.out.println(username);
        System.out.println(password);
        String sql="select * from user where name='"+username+"'";
        ResultSet rs = shujuku1.executeQuery(sql);

        String passwd=null;
        try {
            while(rs.next()){

                passwd=rs.getString(2);
                System.out.println(passwd);
                System.out.println(password);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        if(passwd.equals(password))
        {
            response.sendRedirect("index.jsp");
        }
        else{
            response.sendRedirect("404.html");
        }

    }


    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        doGet(request, response);
    }

}
