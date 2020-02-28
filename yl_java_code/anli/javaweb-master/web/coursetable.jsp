<%--只显示目前包含的课程--%>

<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>全部课程</title>
    <link href="http://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/htmleaf-demo.css">
</head>
<body>
<div class="htmleaf-container">
    <header class="htmleaf-header">
        <h1>燕山大学学生签到系统</h1>
        <div class="htmleaf-links">
            <a class="htmleaf-icon icon-htmleaf-home-outline" href="index.jsp" title="返回主页"><span>返回主页</span></a>
            <a class="htmleaf-icon icon-htmleaf-arrow-forward-outline" href="login2.jsp"
               title="重新登陆"><span> 返回下载页</span></a>
        </div>
    </header>
    <div class="container">
        <div class="row">
            <div class="col-sm-12 text-center">
                <h1 class="h1">课程表</h1>
                <%--<p>a jQuery plugin to paginate your DOM easily.</p>--%>
            </div>
            <%-- <h3>Paginate  <code>&lt;tabel&gt;</code></h3>--%>
            <table class="table table-bordered">
                <thead>

                <tr>
                    <th>星期一</th>
                    <th>星期二</th>
                    <th>星期三</th>
                    <th>星期四</th>
                    <th>星期五</th>
                </tr>
                </thead>
                <tbody>
                <form action="/tableServlet" method="post">
                    <tr>
                        <% for (int j = 1; j <= 5; j++) {%>

                        <td>
                            <input type="text" name="k<%=j%>" placeholder="第1节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>
                    <tr>
                        <% for (int j = 6; j <= 10; j++) {%>

                        <td><input type="text" name="k<%=j%>" placeholder="第2节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>
                    <tr>
                        <% for (int j = 11; j <= 15; j++) {%>

                        <td><input type="text" name="k<%=j%>" placeholder="第3节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>
                    <tr>
                        <% for (int j = 16; j <= 20; j++) {%>

                        <td><input type="text" name="k<%=j%>" placeholder="第4节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>
                    <tr>
                        <% for (int j = 21; j <= 25; j++) {%>

                        <td><input type="text" name="k<%=j%>" placeholder="第5节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>
                    <tr>
                        <% for (int j = 26; j <= 30; j++) {%>

                        <td><input type="text" name="k<%=j%>" placeholder="第6节课">
                            <input type="text" name="teacher<%=j%>" placeholder="授课教师">
                        </td>
                        <%}%>
                    </tr>

                    <center>
                        <button type="submit">提交</button>
                    </center>

                </form>
                </tbody>
            </table>


        </div>
    </div>
    <center>
        </a><a href="showtable.jsp">
        <button>显示当前课表</button>
    </a>
        </a><a href="index.jsp">
        <button>返回主页</button>
    </a></center>
</div>


<script src="http://cdn.bootcss.com/jquery/1.11.0/jquery.min.js" type="text/javascript"></script>
<script>window.jQuery || document.write('<script src="js/jquery-1.11.0.min.js"><\/script>')</script>
<script type="text/javascript" src="js/paginathing.js"></script>
<%--<script type="text/javascript">--%>
<%--jQuery(document).ready(function ($) {--%>
<%--for (var i = 1; i <= 150; i++) {--%>
<%--$('.list-group').append('<li class="list-group-item"> Item ' + i + '</li>');--%>
<%--}--%>

<%--$('.list-group').paginathing({--%>
<%--perPage: 5,--%>
<%--limitPagination: 9,--%>
<%--containerClass: 'panel-footer',--%>
<%--pageNumbers: true--%>
<%--})--%>

<%--$('.table tbody').paginathing({--%>
<%--perPage: 5,--%>
<%--insertAfter: '.table',--%>
<%--pageNumbers: true--%>
<%--});--%>
<%--});--%>
<%--</script>--%>
</body>
</html>