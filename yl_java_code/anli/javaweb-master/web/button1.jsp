<%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2018/7/10
  Time: 12:31
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

<head>

    <meta charset="utf-8">

    <title>按钮</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="font-awesome/css/font-awesome.css" rel="stylesheet">

    <link href="css/animate.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
    <style>
        #test {
            position: absolute;
            left: 42%;
            top: 300px;

        }
    </style>
</head>
<body>

<div id="test">
    <form method="post" action="/DeleteServlet">


        <button type="button" class="btn btn-default btn-lg">点击清空当前选课记录</button>
    </form>

</div>
</body>
</html>
