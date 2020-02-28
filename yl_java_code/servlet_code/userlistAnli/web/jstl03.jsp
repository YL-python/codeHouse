<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.List" %>
<%-- Date: 2019/11/11 0011 16:25 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Title</title>
</head>
<body>

<%
    String citystr = "北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区";
    String[] citys = citystr.split("，");
    request.setAttribute("citys",citys);
%>

<c:forEach begin="1" end="10" var="i" step="1">
    ${i} <br>
</c:forEach>

<hr>
<select class="form-control" name="address">
    <c:forEach items="${requestScope.citys}" var="city">
        <option>${city}</option>
    </c:forEach>
</select>
<c:forEach items="${requestScope.citys}" var="city" varStatus="s">
    ${s.index} ${s.count} ${city} <br>
</c:forEach>


</body>
</html>
