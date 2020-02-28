<%-- Date: 2020/1/17 0017 13:35 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>参数</title>
</head>
<body>

<h3>参数</h3>

<a href="param/nameAndpassword?username=lisi&password=123">用户和密码</a>

<br>
<br>
<br>
<br>
<form action="param/saveAccount" method="post">
    姓名：<input type="text" name="username"/><br>
    密码：<input type="text" name="password"/><br>
    金额：<input type="text" name="money"/><br>
    用户姓名：<input type="text" name="user.uname"/><br>
    用户年龄：<input type="text" name="user.uage"/><br>
    <input type="submit" value="提交"/><br>
</form>

<br>
<br>
<br>
<br>
<form action="param/saveAccount" method="post">
    姓名：<input type="text" name="username"/><br>
    密码：<input type="text" name="password"/><br>
    金额：<input type="text" name="money"/><br>

    用户姓名：<input type="text" name="list[0].uname"/><br>
    用户年龄：<input type="text" name="list[0].uage"/><br>

    用户姓名：<input type="text" name="map['one'].uname"/><br>
    用户年龄：<input type="text" name="map['one'].uage"/><br>

    <input type="submit" value="提交"/><br>
</form>

<br>
<br>
<br>
<br>
<form action="param/saveUser" method="post">
    用户姓名：<input type="text" name="uname"/><br>
    用户年龄：<input type="text" name="uage"/><br>
    用户生日：<input type="text" name="udate"/><br>
    <input type="submit" value="提交"/><br>
</form>

<a href="param/testServlet">servlet原生API</a>

</body>
</html>
