package cn.itcast.travel.web.servlet;

import cn.itcast.travel.domain.PageBean;
import cn.itcast.travel.domain.Route;
import cn.itcast.travel.domain.User;
import cn.itcast.travel.service.FavoriteService;
import cn.itcast.travel.service.RouteService;
import cn.itcast.travel.service.impl.FavoriteServiceImpl;
import cn.itcast.travel.service.impl.RouteServiceImpl;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/route/*")
public class RouteServlet extends BaseServlet {

    private RouteService routeService = new RouteServiceImpl();
    private FavoriteService favoriteService = new FavoriteServiceImpl();

    // 分页查询
    public void pageQuery(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 接受参数
        String currentPageStr = request.getParameter("currentPage");
        String pageSizeStr = request.getParameter("pageSize");
        String cidStr = request.getParameter("cid");

        String rnameStr = request.getParameter("rname");
        if(rnameStr != null && rnameStr.length()>0 && !"null".equals(rnameStr)){
            // 汉字重新编码
            rnameStr = new String(rnameStr.getBytes("iso-8859-1"),"utf-8");
        }else{
            rnameStr = null;
        }

        // 处理参数
        int currentPage;  // 当前页码，默认值是1
        if(currentPageStr!=null && currentPageStr.length() > 0){
            currentPage = Integer.parseInt(currentPageStr);
        }else{
            currentPage = 1;
        }
        int pageSize;  // 每一页显示的条数，默认值是5
        if(pageSizeStr!=null && pageSizeStr.length() > 0){
            pageSize = Integer.parseInt(pageSizeStr);
        }else{
            pageSize = 5;
        }
        int cid;  // 分类的id
        if(cidStr!=null && cidStr.length() > 0 && !"null".equals(cidStr)){
            cid = Integer.parseInt(cidStr);
        }else{
            cid = 0;
        }

        // 调用service对象查询pageBean对象
        PageBean<Route> pages =  routeService.pageQuery(cid, currentPage ,pageSize, rnameStr);

        // 序列化为json并返回数据
        writerValue(pages,response);
    }

    // 根据id查询一个旅游线路的详细信息
    public void findOne(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 接收id参数
        String ridStr = request.getParameter("rid");
        // 调用service查询route对象
        Route route = routeService.findOne(ridStr);
        // 转json写回客户端
        writerValue(route, response);

    }

    // 判断当前登录的用户是否收藏过改线路
    // 根据id查询一个旅游线路的详细信息
    public void isFavorite(HttpServletRequest request, HttpServletResponse response) throws IOException {

        // 获取线路id
        String ridStr = request.getParameter("rid");

        // 获取当前登录的用户user
        User user = (User) request.getSession().getAttribute("user");
        int uid;
        if(user == null){
            // 用户没有登录
            uid = 0;
        }else{
            //用户已经登录
            uid = user.getUid();
        }

        // 调用FavoriteService
        boolean flag = favoriteService.isFavorite(ridStr, uid);

        // 会写数据
        writerValue(flag, response);
    }

    public void addFavorite(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 获取线路id
        String ridStr = request.getParameter("rid");

        // 获取当前登录的用户user
        User user = (User) request.getSession().getAttribute("user");
        int uid;
        if(user == null){
            // 用户没有登录
            return ;
        }else{
            //用户已经登录
            uid = user.getUid();
        }

        favoriteService.add(ridStr,uid);
    }
}
