<%@ page import="main.java.User" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.Date" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Title</title>
</head>
<body>


    <%--
    User u1 = new User();
    u1.setName("zhangsan");
    u1.setAge(25);
    u1.setBirthday(new Date());
    --%>
    <%
        List list = new ArrayList();
        list.add(new User("zhangsan", 12, new Date()));
        list.add(new User("lisi", 13, new Date()));
        list.add(new User("wangwu", 14, new Date()));
        request.setAttribute("list",list);
    %>

<table border="1" width="500" align="center">
    <tr>
        <th>编号</th>
        <th>姓名</th>
        <th>年龄</th>
        <th>生日</th>
    </tr>
    <c:forEach items="${list}" var="uesr" varStatus="s" >
        <c:if test="${s.count mod 2 == 0}">
            <tr bgcolor="aqua">
                <td>${s.count}</td>
                <td>${uesr.name}</td>
                <td>${uesr.age}</td>
                <td>${uesr.birStr}</td>
            </tr><br>
        </c:if>
        <c:if test="${s.count mod 2 == 0}">
            <tr bgcolor="#7fffd4">
                <td>${s.count}</td>
                <td>${uesr.name}</td>
                <td>${uesr.age}</td>
                <td>${uesr.birStr}</td>
            </tr><br>
        </c:if>

    </c:forEach>

</table>

</body>
</html>













