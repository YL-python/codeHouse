package link;

import db.Database;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

@WebServlet(name = "testServlet",urlPatterns = "/testServlet")
public class testServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String ID=request.getParameter("search");
        System.out.println(ID);
//        try {
//            Class.forName("com.mysql.jdbc.Driver");
//        } catch (ClassNotFoundException e) {
//            e.printStackTrace();
//        }
//        Connection conn = null;
//        try {
//            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/software?user=root&password=961008&useSSL=false&serverTimezone=UTC");
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
//        Statement stmt = null;
//        try {
//            stmt = conn.createStatement();
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
        String sql = "select * from sc where ID="+ID+"";
//        System.out.println(sql);
//
//        ResultSet result = null;
//        try {
//            result = stmt.executeQuery(sql);
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
        Database search=new Database();
        ResultSet result=null;
        try {
            result=search.a(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        request.setAttribute("result",result);
        RequestDispatcher requestDispatcher = this.getServletContext().getRequestDispatcher("/showsturesult.jsp");
        requestDispatcher.forward(request, response);


//        response.sendRedirect("showresult.jsp");
    }
    }


