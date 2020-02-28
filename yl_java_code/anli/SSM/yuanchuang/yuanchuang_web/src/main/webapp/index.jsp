<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<head>
    <title>猿创工作室</title>
    <link rel="stylesheet" href="css/index.css">
    <style>
        body {
            background: url(${pageContext.request.contextPath}/images/yuanchuang.jpg) no-repeat;
            background-size: cover;
            font-family: 'Helvetica Neue', 'PingFang SC', 'Myriad Pro', 'Hiragino Sans GB', 'microsoft yahei';
            -ms-user-select: none;
            -moz-user-select: none;
            -webkit-user-select: none;
            user-select: none
        }
    </style>
</head>

<body>
<div class="content">
    <h1>Hello, world !</h1>
    <p>Welcome to 猿创工作室</p>
</div>
<div class="mav-main">
    <div class="aside-nav bounceInUp animated" id="aside-nav">
        <label class="aside-menu">导航</label>
        <a title="签到" class="menu-item menu-first" target="_self" href="${pageContext.request.contextPath}/login.jsp">签到</a>

        <a title="Java教学" class="menu-item menu-second" target="_self" href="https://how2j.cn/">Java教学</a>
        <a title="GitHub中文榜单" class="menu-item menu-line menu-third" target="_self"
           href="https://github.com/kon9chunkit/GitHub-Chinese-Top-Charts">GitHub<br>中文榜单</a>
        <a href="javascript:void(0);" class="menu-item menu-line menu-fourth" title="其他" target="_self">开发中<br>. . .</a>
        <a class="menu-item menu-line menu-fifth" target="_self" href="https://www.w3school.com.cn/index.html">前端<br>教学</a>
        <a title="python3教学" class="menu-item menu-line menu-sixth" target="_self"
           href="https://www.runoob.com/python3/python3-tutorial.html">python3<br>教学</a>
    </div>
</div>
</div>
</body>

</html>