<%-- Date: 2019/11/18 0018 10:06 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/index.css">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <title>监考系统</title>
    <script>
        function resetData() {
            // 给出安全提示框
            if (confirm("是否确定重置数据")) {
                // 访问数据
                location.href = "${pageContext.request.contextPath}/resetServlet";
            }
        }
        function modifyData(id) {
            if (confirm("是否申请本次不参与监考")) {
                // 访问数据
                location.href = "${pageContext.request.contextPath}/modifyTeaServlet?id="+id;
            }
        }
    </script>
</head>
<body>
<div class="container"><h1>监考系统</h1></div>
<div class="center">
    <div id="readFile">
        <form class="form-inline" action="${pageContext.request.contextPath}/readExcelFileServlet" method="post">
            <div class="form-group">
                <label for="readText">导入文件路径</label>
                <input type="text" name="readFilePath" class="form-control" id="readText" placeholder="输入excel文件路径">
            </div>
            <button type="submit" class="btn btn-default">导入</button>
        </form>
    </div>
    <div id="writerFile">
        <form class="form-inline" style="float: right" action="${pageContext.request.contextPath}/writeExcelFileServlet"
              method="post">
            <div class="form-group">
                <label for="writeText">导出文件路径</label>
                <input type="text" name="writeFilePath" class="form-control" id="writeText" placeholder="输入excel输出的路径">
            </div>
            <button type="submit" class="btn btn-default">导出</button>
        </form>
    </div>
</div>
<div class="center" style="margin-top: 70px">
    <form class="form-inline" style="float: left" action="${pageContext.request.contextPath}/searchTeaServlet" method="post">
        <div class="form-group">
            <label for="searchText">需要监考老师人数：</label>
            <input type="text" name="tea_num" class="form-control" id="searchText" placeholder="输入人数">
        </div>
        <button type="submit" class="btn btn-default">搜索</button>
    </form>
    <a class="btn btn-danger" id="reset_a" href="javascript:resetData();" style="float: right">重置</a>
</div>
<div class="center" style="margin-top: 140px">
    <table class="table table-bordered table-hover">
        <tr class="success">
            <th>编号</th>
            <th>姓名</th>
            <th>电话</th>
            <th>教研室</th>
            <th>特殊情况</th>
        </tr>
        <c:forEach items="${sessionScope.teachers}" var="teacher" varStatus="s">
            <tr>
                <td>${s.count}</td>
                <td>${teacher.name}</td>
                <td>${teacher.tel}</td>
                <td>${teacher.teacher_home}</td>
                <td>
                    <a class="btn btn-default" href="javascript:modifyData(${teacher.id});">申请</a>
                </td>
            </tr>
        </c:forEach>
    </table>
</div>
<c:if test="${not empty requestScope.readOrWriteFileMsg}">
    <div class="alert alert-warning alert-dismissible center" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                aria-hidden="true">&times;</span></button>
        <strong>${requestScope.readOrWriteFileMsg}</strong>
    </div>
</c:if>
</body>
</html>
