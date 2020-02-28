<%-- Date: 2020/1/17 0017 13:35 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>常用注解</title>
</head>
<body>

<h3>常用注解</h3>

<a href="anno/testRequestParam?name=123">RequestParam</a>
<br>
<form action="anno/testRequestBody" method="post">
    姓名：<input type="text" name="username"/><br>
    年龄：<input type="text" name="password"/><br>
    金额：<input type="text" name="money"/><br>
    <input type="submit" value="提交"/><br>
</form>
<br>
<a href="anno/testPathVariable/10">PathVariable</a>
<br>
<a href="anno/testRequestHeader">RequestHeader</a>
<br>
<a href="anno/testCookieValue">CookieValue</a>
<br>
<form action="anno/testModelAttribute" method="post">
    姓名：<input type="text" name="uname"/><br>
    年龄：<input type="text" name="uage"/><br>
    <input type="submit" value="提交"/><br>
</form>
<br>
<a href="anno/testSessionAttributes">SessionAttributes</a>
<br>
<a href="anno/getSessionAttributes">getSessionAttributes</a>
<br>

<a href="anno/delSessionAttributes">delSessionAttributes</a>
<br>
</body>
</html>
