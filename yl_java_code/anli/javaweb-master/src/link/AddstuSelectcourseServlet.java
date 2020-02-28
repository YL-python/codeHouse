package link;

import com.sun.xml.internal.bind.v2.model.core.ID;
import db.DBbean;
import db.Database;
import db.DatabaseQuery;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

@WebServlet(name = "AddstuSelectcourseServlet",urlPatterns = "/AddstuSelectcourseServlet")
public class AddstuSelectcourseServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String ID=request.getParameter("stuid");
        String studentname=request.getParameter("stuname");
        String course = request.getParameter("course");
        String class1=request.getParameter("class");
        String qiandao="否";

//        String teacher= request.getParameter("teacher");
        System.out.println(ID);
//        System.out.println(coursename);
        System.out.println(studentname);
        System.out.println(course);
        System.out.println(class1);
        System.out.println(qiandao);


//        Database database=new Database();
        DBbean dBbean=new DBbean();
//        String sql1="insert into course(coursename,teacher)values('"+coursename+"','"+teacher+"')";
        String sqlQ="select * from coursetable where name='"+course+"'";
        System.out.println(sqlQ);
        ResultSet resultSet=dBbean.executeQuery(sqlQ);
        try{
        while (resultSet.next())
        {
            String teacher = null;

            try {
                teacher = resultSet.getString("teachers");
                String jie = resultSet.getString("jie");
                String xingqi = resultSet.getString("xingqi");
                String sql1="insert into sc(ID,studentname,class,course,xingqi1,jie1,teacher,qiandao)values("+ID+",'"+studentname+"','"+class1+"','"+course+"','"+xingqi+"','"+jie+"','"+teacher+"','"+qiandao+"')";
                System.out.println(sql1);
                try {
                    Database database=new Database();
                    database.Database(sql1);
                } catch (ClassNotFoundException e) {
                    System.out.println("无操作1");
                }
//                response.sendRedirect("index.jsp");
            } catch (SQLException e) {
                System.out.println("无操作2");
            }
            System.out.println(teacher);
        }
            response.sendRedirect("AddstuSelectcourse1.jsp");
    }

    catch (SQLException e){
        System.out.println("未查到教师");
        }

    }
Database database=new Database();


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
