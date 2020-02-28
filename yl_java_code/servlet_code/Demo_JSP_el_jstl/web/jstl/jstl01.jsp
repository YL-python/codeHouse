<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.List" %><%-- Date: 2019/11/11 0011 16:25 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Title</title>
</head>
<body>

<c:if test="${empty requestScope.name}">
<h1>requestScope.name为空</h1>
</c:if>

<%
    List list = new ArrayList();
    list.add("aaa");
    request.setAttribute("list",list);
    request.setAttribute("number",3);
%>

<c:if test="${not empty requestScope.list}">
    遍历集合
</c:if>
<c:if test="${requestScope.number mod 2 != 0}">
    ${number}为奇数
</c:if>
<c:if test="${requestScope.number mod 2 == 0}">
    ${number}为偶数
</c:if>

</body>
</html>
