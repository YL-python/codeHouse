package main.java.web.servlet;

import main.java.dao.userDao;
import main.java.domian.PageBean;
import main.java.domian.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.util.Map;

@WebServlet("/findUserByPageServlet")
public class FindUserByPageServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        // 获取页码参数  // 对参数处理
        String currentPage = request.getParameter("currentPage");
        int intCurrentPage;
        if(currentPage == null || currentPage.length()==0){
            intCurrentPage =0;
        }else{
            intCurrentPage = Integer.parseInt(currentPage);
        }

        // 获取多条件模糊查询的参数
        Map<String, String[]> parameterMap = request.getParameterMap();
//        System.out.println(parameterMap.keySet());

        // 查询数据 接收返回的对象
        PageBean<User> pageUser = new PageBean<User>();
        userDao dao = new userDao();
        int totalCount = dao.getTotalCount(parameterMap);  // 查询一共少数据
        int rows = pageUser.getRows();  // 每一页展示多少数据
        int totalPage = ( totalCount % rows ) == 0 ? totalCount / rows : ( totalCount / rows ) + 1; // 有多少页

        // 每一页的数据
        if(intCurrentPage>=1 && intCurrentPage<=totalPage){
            int start = (intCurrentPage-1) * rows;
            List<User> pageUserList = dao.findUserByPage(start, rows,parameterMap);
            pageUser.setTotalCount(totalCount);  // 总数据个数
            pageUser.setTotalPage(totalPage);  // 总共多少页
            pageUser.setUserList(pageUserList);  // 每一页的用户信息
            pageUser.setCurrentPage(intCurrentPage);  // 当前页码
        }else {
            List<User> pageUserList = dao.findUserByPage(0, rows, parameterMap);
            pageUser.setTotalCount(totalCount);  // 总数据个数
            pageUser.setTotalPage(totalPage);  // 总共多少页
            pageUser.setUserList(pageUserList);  // 每一页的用户信息
            pageUser.setCurrentPage(1);  // 当前页码
        }
        // 把对象存到requests中在资源转发
//        System.out.println(pageUser);
        request.setAttribute("pb",pageUser);
        request.setAttribute("parameterMap",parameterMap);
        request.getRequestDispatcher("/list.jsp").forward(request,response);

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
