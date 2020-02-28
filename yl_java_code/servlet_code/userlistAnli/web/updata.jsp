<%-- Date: 2019/11/13 0013 14:49 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<html>
<head>
    <title>修改用户</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
</head>
<body >
<div class="container" style="width: 600PX">
    <center><h1>修改用户</h1></center>
    <form action="${pageContext.request.contextPath}/updataServlet" method="post">
        <input type="hidden" name="id" value="${userbyid.id}">
        <div class="form-group">
            <label for="name">姓名：</label>
            <input class="form-control" id="name" name="name" value="${userbyid.name}">
        </div>
        <div class="checkbox">
            <label>性别：</label>
                <c:if test="${userbyid.gender == '男'}">
                    <input type="radio" name="gender" value="男" checked="checked"> 男
                    <input type="radio" name="gender" value="女"> 女
                </c:if>
            <c:if test="${userbyid.gender == '女'}">
                <input type="radio" name="gender" value="男"> 男
                <input type="radio" name="gender" value="女" checked="checked"> 女
            </c:if>
        </div>
        <div class="form-group">
            <label for="age">年龄：</label>
            <input class="form-control" id="age" name="age" value="${userbyid.age}">
        </div>
        <label>籍贯：</label>
        <select class="form-control" name="address">
            <c:forEach items="${sessionScope.citys}" var="city">
                <c:if test="${userbyid.address == city}">
                    <option value="${city}" selected="selected">${city}</option>
                </c:if>
                <c:if  test="${userbyid.address != city}">
                    <option value="${city}">${city}</option>
                </c:if>
            </c:forEach>
        </select>
        <div class="form-group">
            <label for="QQ">QQ</label>
            <input class="form-control" id="QQ" value="${userbyid.qq}" name="qq">
        </div>
        <div class="form-group">
            <label for="email">Email：</label>
            <input type="email" class="form-control" id="email" value="${userbyid.email}" name="email">
        </div>
        <div style="text-align: center">
            <input type="submit" class="btn btn-primary" value="修改">
            <input type="reset" class="btn btn-default" value="重置">
            <a class="btn btn-default" type="button" href="${pageContext.request.contextPath}/userListServlet"> 返回</a>
        </div>

    </form>
</div>
</body>
</html>
