<%@ page import="java.sql.ResultSet" %><%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2018/7/8
  Time: 18:12
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>查询结果</title>
    <link href="http://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/htmleaf-demo.css">
</head>
<body>
<%ResultSet rs = (ResultSet) request.getAttribute("result");%>
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
                <h1 class="h1">查询结果</h1>
                <%--<p>a jQuery plugin to paginate your DOM easily.</p>--%>
            </div>

                <%-- <h3>Paginate  <code>&lt;tabel&gt;</code></h3>--%>
                <table class="table table-bordered">
                    <thead>

                    <tr>
                        <th>学号</th>
                        <th>学生姓名</th>
                        <th>班级</th>
                        <th>所选课程</th>
                        <th>星期</th>
                        <th>时间</th>
                        <th>授课教师</th>
                        <th>是否签到</th>
                        <th>删除记录</th>
                        <th>点击签到</th>
                    </tr>
                    </thead>
                    <tbody>
                    <%
                        //遍历结果集
                        while (true) {
                            if (!(rs.next())) break;%>
                    <tr>
                        <form action="/ShowlistServlet" method="post">
                            <!-- 输出结果集 -->
                            <td><%=rs.getString("ID") %>
                            </td>
                            <input type="hidden" name="ID" value="<%=rs.getString("ID") %>"/>
                            <td><%=rs.getString("studentname") %>
                            </td>
                            <td><%=rs.getString("class") %>
                            </td>

                            <td> <%=rs.getString("course") %>
                            </td>
                            <td><%=rs.getString("xingqi1") %>
                            </td>
                            <td><%=rs.getString("jie1") %>
                            </td> <input type="hidden" name="course" value="<%=rs.getString("course") %>"/>
                            <input type="hidden" name="xingqi" value="<%=rs.getString("xingqi1") %>"/>
                            <input type="hidden" name="jie" value="<%=rs.getString("jie1") %>"/>
                            <td><%=rs.getString("teacher") %>
                            </td>
                            <td><%=rs.getString("qiandao") %>
                            </td>

                            <td>
                                <button type="submit">删除</button>
                            </td>
                        </form>
                        <form method="post" action="/qiandaoServlet">
                            <td>
                                <button type="submit">签到</button>
                            </td>
                            <input type="hidden" name="xingqi" value="<%=rs.getString("xingqi1") %>"/>
                            <input type="hidden" name="jie" value="<%=rs.getString("jie1") %>"/>
                            <input type="hidden" name="ID" value="<%=rs.getString("ID") %>"/>
                            <input type="hidden" name="course" value="<%=rs.getString("course") %>"/>
                        </form>
                    </tr>
                    <%
                        }
                    %>
                    </tbody>
                </table>



        </div>
    </div>


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
