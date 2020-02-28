<%@ page import="main.java.User" %>
<%@ page import="java.util.Date" %><%-- Date: 2019/11/11 0011 11:58 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    User user = new User();
    user.setName("zhangsan");
    user.setAge(24);
    user.setBirthday(new Date());
    request.setAttribute("u",user);
%>

${requestScope.u.name}<br>
${requestScope.u.age}<br>
${requestScope.u.birthday}<br>
${requestScope.u.birStr}<br>

</body>
</html>
