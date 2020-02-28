<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.ResultSet" %><%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2018/6/30
  Time: 18:12
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page errorPage="404.html" %>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>网站首页</title>
    <link rel="stylesheet" type="text/css" href="css/htmleaf-demo.css">
    <link rel="stylesheet" type="text/css" href="css/nav.css">
    <link rel="stylesheet" type="text/css" href="fonts/iconfont.css">
    <link rel="stylesheet" type="text/css" href="css/xx/iconfont.css">
    <link rel="stylesheet" href="css/shutter.css">
    <style>
        #1 {
            color: white;
        }
    </style>
</head>
<body>
<div class="nav">
    <div class="nav-top">
        <div id="mini" style="border-bottom:1px solid rgba(255,255,255,.1)"><img src="images/mini.png"></div>
    </div>
    <ul>
        <li class="nav-item">
            <a href="javascript:;"><i class="my-icon nav-icon icon_1"></i><span>系统管理</span><i
                    class="my-icon nav-more"></i></a>
            <ul>
                <li><a href="login2.jsp"><span>管理员登陆</span></a></li>
                <li><a href="regist2.jsp"><span>增加管理员</span></a></li>
                <li><a href="showuser.jsp"><span>管理员列表</span></a></li>
                <%--去登陆页面，管理员与用户两个选项--%>
            </ul>
        </li>
        <li class="nav-item">
            <a href="javascript:;"><i class="my-icon nav-icon icon_3"></i><span>学生管理</span><i
                    class="my-icon nav-more"></i></a>
            <ul>
                <li><a href="AddstuSelectcourse1.jsp"><span>学生选课</span></a></li>
                <%--<li><a href=""><span>收取快递</span></a></li>--%>
                <li><a href="showalllist.jsp"><span>开始签到</span></a></li>
            </ul>
        </li>
        <li class="nav-item">
            <a href="javascript:;"><i class="my-icon nav-icon icon_3"></i><span>课程管理</span><i
                    class="my-icon nav-more"></i></a>
            <ul>
                <%--<li><a href="addcourse2.jsp"><span>添加课程</span></a></li>--%>
                <%--<li><a href="showcourse.jsp"><span>课程列表</span></a></li>--%>
                <li><a href="button.jsp"><span>新建课表</span></a></li>
                    <li><a href="showtable.jsp"><span>当前课表</span></a></li>
            </ul>
        </li>
        <li class="nav-item">
            <a href="javascript:;"><i class="my-icon nav-icon icon_2 "></i><span>快速查询</span><i
                    class="my-icon nav-more"></i></a>
            <ul>
                <li><a href="Searchstu.jsp"><span>通过学号查询</span></a></li>
                <li><a href="Searchcor.jsp"><span>通过课程查询</span></a></li>
                <li><a href="Searchxingqi.jsp"><span>通过日期查询</span></a></li>
                <%--去登陆页面，管理员与用户两个选项--%>
            </ul>
        </li>
    </ul>
</div>
<div class="htmleaf-container">
    <header class="htmleaf-header">
        <h1>燕山大学学生签到系统</h1>
        <br>
        <br>
        <div class="htmleaf-links">
            <a class="htmleaf-icon icon-htmleaf-home-outline" href="index.jsp" title="返回主页"
               target="_blank"><span> 返回主页</span></a>
            <a class="htmleaf-icon icon-htmleaf-arrow-forward-outline" href="login2.jsp" title="重新登陆"
               target="_blank"><span> 重新登陆</span></a>
        </div>
    </header>

    <div class="shutter">
        <div class="shutter-img">
            <a href="https://www.ysu.edu.cn/info/1847/5430.htm" data-shutter-title="欢迎报考燕山大学"><img
                    src="images/a5%20(1).jpg" alt="#"></a>
            <a href="https://news.ysu.edu.cn/info/1016/14377.htm" data-shutter-title="我在燕大等你"><img
                    src="images/a5%20(2).jpg" alt="#"></a>
            <a href="https://www.ysu.edu.cn/info/1996/5526.htm" data-shutter-title="长亭古道 无问西东——2018毕业生晚会精彩回顾"><img
                    src="images/20180702.jpg" alt="#"></a>
            <a href="https://news.ysu.edu.cn/info/1016/14393.htm" data-shutter-title="迈向“双一流”的五星级大学"><img
                    src="images/a5%20(4).jpg" alt="#"></a>
        </div>
        <ul class="shutter-btn">
            <li class="prev"></li>
            <li class="next"></li>
        </ul>
        <div class="shutter-desc">
            <p>燕山大学</p>
        </div>
    </div>
</div>
<%--<div class="htmleaf-header" id="1" style="font-family: 幼圆">--%>

<script src="http://cdn.bootcss.com/jquery/1.11.0/jquery.min.js" type="text/javascript"></script>
<script>window.jQuery || document.write('<script src="js/jquery-1.11.0.min.js"><\/script>')</script>
<script type="text/javascript" src="js/nav.js"></script>

<script src="http://www.jq22.com/jquery/jquery-1.10.2.js"></script>
<script src="js/velocity.js"></script>
<script src="js/shutter.js"></script>
<script>
    $(function () {
        $('.shutter').shutter({
            shutterW: 1000, // 容器宽度
            shutterH: 358, // 容器高度
            isAutoPlay: true, // 是否自动播放
            playInterval: 3000, // 自动播放时间
            curDisplay: 3, // 当前显示页
            fullPage: false // 是否全屏展示
        });
    });
</script>
</body>
</html>
</html>
