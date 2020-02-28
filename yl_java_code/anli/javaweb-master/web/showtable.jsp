<%--只显示目前包含的课程--%>

<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>课程表</title>
    <link href="http://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/htmleaf-demo.css">
</head>
<body>
<%
    //注册数据库驱动
    Class.forName("com.mysql.jdbc.Driver");
//获取数据库连接
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
//创建statement
    Statement stmt = conn.createStatement();
//执行查询
    String sql1 = "select * from coursetable";
    ResultSet rs = stmt.executeQuery(sql1);
%>
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
            <div class="col-sm-8 col-sm-offset-2">
                <%-- <h3>Paginate  <code>&lt;tabel&gt;</code></h3>--%>
                <table class="table table-bordered">
                    <thead>

                    <tr>
                        <th>日期</th>
                        <th>时间</th>
                        <th>课程名</th>
                        <th>授课教师</th>
                    </tr>
                    </thead>
                    <tbody>
                    <%
                        //遍历结果集
                        while (true) {
                            if (!(rs.next())) break;%>
                    <tr>

                            <!-- 输出结果集 -->
                            <td><%=rs.getString("xingqi") %>
                            </td>
                            <%--<input type="hidden" name="ID" value="<%=rs.getString("ID") %>"/>--%>
                            <td><%=rs.getString("jie") %>
                            </td>
                        <td><%=rs.getString("name") %>
                        </td>
                        <td><%=rs.getString("teachers") %>
                        </td>

                            <%--<td>--%>
                                <%--<center>--%>
                                    <%--<button type="submit">4</button>--%>
                                <%--</center>--%>
                            <%--</td>--%>


                    </tr>
                    <%
                        }
                    %>
                    </tbody>
                </table>

            </div>

        </div>
    </div>
    <center>
        <a href="button.jsp">
            <button>新建课表</button>
        </a><a href="index.jsp">
        <button>返回主页</button>
    </a></center>
</div>


<script src="http://cdn.bootcss.com/jquery/1.11.0/jquery.min.js" type="text/javascript"></script>
<script>window.jQuery || document.write('<script src="js/jquery-1.11.0.min.js"><\/script>')</script>
<script type="text/javascript" src="js/paginathing.js"></script>
<script type="text/javascript">
    jQuery(document).ready(function ($) {
        for (var i = 1; i <= 150; i++) {
            $('.list-group').append('<li class="list-group-item"> Item ' + i + '</li>');
        }

        $('.list-group').paginathing({
            perPage: 5,
            limitPagination: 9,
            containerClass: 'panel-footer',
            pageNumbers: true
        })

        $('.table tbody').paginathing({
            perPage: 4,
            insertAfter: '.table',
            pageNumbers: true
        });
    });
</script>
</body>
</html>