<%-- Date: 2020/1/20 0020 21:06 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>index</title>
</head>
<body>

    <a href="account/findAll"> 测试 findAll </a>

    <h3>测试保存</h3>

    <form action="account/save" method="post">
        姓名：<input type="text" name="name" /><br/>
        金额：<input type="text" name="money" /><br/>
        <input type="submit" value="保存"/><br/>
    </form>


</body>
</html>
