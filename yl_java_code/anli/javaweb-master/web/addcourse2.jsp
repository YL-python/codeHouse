<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.ResultSet" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="UTF-8" %>
<%--周一更新的--%>
<%--学生选课页面，同时录入学生信息--%>
<%--<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">--%>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>学生选课</title>
    <script type="text/javascript" src="res/js/jquery-1.5.1.min.js"></script>
    <script>
        $(function () {
            $("div").click(function () {
                $(this).addClass("select");
            });
        })
    </script>
    <script>
        function check() {
            if (forma.coursename.value == "") {
                alert("课程名不能为空!");
                forma.coursename.focus();
                return false;
            }
            if (forma.teacher.value == "") {
                alert("教师姓名不能为空!");
                forma.teachere.focus();
                return false;
            }
            return ture;
        }
    </script>

    <style>
        body {
            background: #66667c;
        }

        .exlist {
            background-color: #F9EE70;
            margin: 30px auto;
            padding: 5px;
            width: 680px;
            min-height: 200px;
            height: auto;
            font-family: "微软雅黑";
            -webkit-box-shadow: 4px 4px 5px #333; /*webkit*/
            -moz-box-shadow: 4px 4px 5px #333; /*firefox*/
            box-shadow: 4px 4px 5px #333; /*opera或ie9*/
        }

        #title {
            width: 200px;
            margin: 20px auto;
        }

        #title legend {
            font-size: 26px;
        }

        div.exlist_title {
            background-color: #F9EE70;
            width: 680px;
            height: 20px;
        }

        div.exlist_title img {
            float: right;
            margin: -15px 10px;
        }

        /*-----------form-----------*/

        fieldset {
            width: 90%;
            border: 1px dashed #666;
            margin: 40px auto;
        }

        legend {
            background-color: #F9EE70;
            height: 120px;
            height: 30px;
            color: #630;
            font-weight: bolder;
            font-size: 20px;
            line-height: 30px;
            margin: -20px 10px 10px;
            padding: 0 10px;
        }

        div.row {
            margin: 10px;
            padding: 5px;
        }

        div.row label {
            height: 20px;
            font-size: 16px;
            line-height: 20px;
            margin: 0 10px;
        }

        input.txt {
            background-color: #F9EE70;
            color: #333;
            width: 150px;
            height: 20px;
            margin: 0 10px;
            font-size: 16px;
            line-height: 20px;
            border: none;
            border-bottom: 1px solid #565656;
        }

        input.txt:focus {
            color: #333;
            background-color: #FF0;
            border-bottom: 1px solid #F00;
        }

        select {
            width: 100px;
        }

        option {
            text-align: center;
        }

        input.btn {
            width: 50px;
            height: 20px;
            color: #000008B;
            background-color: transparent;
            border: 0;
            padding: 0;
        }

    </style>
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
    String sql1 = "select * from course";
    ResultSet rs = stmt.executeQuery(sql1);
%>
<div class="exlist">
    <div class="exlist_title"><img src="images/paper-clip.png"/></div>
    <div id="title">
        <legend>课程信息</legend>
    </div>
    <form method="get" action="/AddcourseServlet" name="forma" onSubmit="return check()">
        <fieldset>
            <legend>课程信息</legend>
            <div class="row">
                <label>1. 课程名:</label>
                <input style="width:150px" class="txt" type="text" name="coursename"/>

            </div>
            <div class="row">
                <label>2. 授课教师:</label>
                <input class="txt" type="text" name="teacher"/>
            </div>
        </fieldset>

        <center><input type="submit" value="提交信息" size="25"></center>
        <br>
        <br>

        <center><input type="reset" value="重置" size="25">
            <a href="index.jsp"><input type="button" value="主页" size="25"></a></center>

    </form>
</div>

</body>
</html>