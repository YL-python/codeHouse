<%-- Date: 2019/11/11 0011 11:21 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
// 在域中存储数据
    request.setAttribute("name","zhangsan");
    session.setAttribute("msg","sessionData");

%>

${requestScope.name}
${sessionScope.msg}
${sessionScope.haha}

</body>
</html>
