<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" isELIgnored="false" %>
<%@taglib prefix="security" uri="http://www.springframework.org/security/tags" %>
<aside class="main-sidebar">
    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar">
        <!-- Sidebar user panel -->
        <div class="user-panel">
            <div class="pull-left image">
                <img src="${pageContext.request.contextPath}/images/user2-160x160.jpg"
                     class="img-circle" alt="User Image">
            </div>
            <div class="pull-left info">
                <p id="userName">
<%--                    ${sessionScope.SPRING_SECURITY_CONTEXT.authentication.principal.username}--%>
                        <security:authentication property="principal.username"/>
                </p>
                <a href="#"><i class="fa fa-circle text-success"></i> 在线</a>
            </div>
        </div>

        <!-- sidebar menu: : style can be found in sidebar.less -->
        <ul class="sidebar-menu">
            <li class="header">菜单</li>
            <li id="admin-index"><a
                href="${pageContext.request.contextPath}/pages/main.jsp"><i
                    class="fa fa-dashboard"></i> <span>首页</span></a></li>

            <li class="treeview"><a href="#"> <i class="fa fa-folder"></i>
                <span>个人中心</span> <span class="pull-right-container"> <i
                        class="fa fa-angle-left pull-right"></i>
				</span>
            </a>
                <ul class="treeview-menu">
                    <li>
                        <a href="${pageContext.request.contextPath}/pages/signin.jsp">
                            <i class="fa fa-circle-o"></i> 每日打卡
                        </a>
                    </li>
                    <li>
                        <a href="${pageContext.request.contextPath}/qd/AllInformation?page=1">
                            <i class="fa fa-circle-o"></i> 我的打卡记录
                        </a>
                    </li>
                    <li><a
                            href="${pageContext.request.contextPath}/pages/main.jsp">
                        <i class="fa fa-circle-o"></i> 打卡时间排行榜
                    </a>
                    </li>
                </ul>
            </li>
        </ul>
    </section>
    <!-- /.sidebar -->
</aside>