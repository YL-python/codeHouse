<%-- Date: 2019/11/13 0013 14:49 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<html>
<head>
    <title>添加用户</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
    <center><h1>添加用户</h1></center>
    <form action="${pageContext.request.contextPath}/addUserServlet" method="post">
        <div class="form-group">
            <label for="name">姓名：</label>
            <input class="form-control" id="name" placeholder="请输入姓名" name="name">
        </div>
        <div class="checkbox">
            性别：
            <label>
                <input type="radio" name="gender" value="男" checked="checked"> 男
            </label>
            <label>
                <input type="radio" name="gender" value="女"> 女
            </label>
        </div>
        <div class="form-group">
            <label for="age">年龄：</label>
            <input class="form-control" id="age" placeholder="请输入年龄" name="age">
        </div>
        <label>籍贯：</label>
        <select class="form-control" name="address">
            <c:forEach items="${sessionScope.citys}" var="city">
                <option value="${city}">${city}</option>
            </c:forEach>
        </select>
        <div class="form-group">
            <label for="QQ">QQ</label>
            <input class="form-control" id="QQ" placeholder="请输入QQ" name="qq">
        </div>
        <div class="form-group">
            <label for="email">Email：</label>
            <input type="email" class="form-control" id="email" placeholder="请输入Email" name="email">
        </div>
        <div style="text-align: center">
            <input type="submit" class="btn btn-primary" value="提交">
            <input type="reset" class="btn btn-default" value="重置">
            <a class="btn btn-default" type="button" href="${pageContext.request.contextPath}/userListServlet"> 返回</a>
        </div>

    </form>
</div>
</body>
</html>
