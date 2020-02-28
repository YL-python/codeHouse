<%-- Date: 2020/1/20 0020 21:08 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" isELIgnored="false" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>list</title>
</head>
<body>
    所有账户列表
    <br>
    <c:forEach items="${list}" var="account">
        姓名：${account.name}
        账户余额：
        ${account.money}
        <br>
    </c:forEach>



</body>
</html>
