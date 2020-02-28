<%-- Date: 2019/11/18 0018 10:06 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="css/index.css">
  <script src="js/jquery-3.2.1.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
    <title>监考系统</title>
</head>
<body>
<div class="container"><h1>index监考系统</h1></div>
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
        <form class="form-inline" style="float: right">
            <div class="form-group">
                <label for="writeText">导出文件路径</label>
                <input type="text" class="form-control" id="writeText" placeholder="输入excel输出的路径">
            </div>
            <button type="submit" class="btn btn-default">导出</button>
        </form>
    </div>
</div>
<div class="center" style="margin-top: 70px">
    <form class="form-inline" style="float: left">
        <div class="form-group">
            <label for="searchText">需要监考老师人数：</label>
            <input type="text" class="form-control" id="searchText" placeholder="输入人数">
        </div>
        <button type="submit" class="btn btn-default">搜索</button>
    </form>
    <a class="btn btn-danger" href="#" style="float: right">重置</a>
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
        <tr>
            <td>1</td>
            <td>张三</td>
            <td>15111111111</td>
            <td>大数据</td>
            <td>
                <a class="btn btn-default" href="#">申请</a>
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>李四</td>
            <td>15222222222</td>
            <td>软件工程</td>
            <td>
                <a class="btn btn-default" href="#">申请</a>
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td>王五</td>
            <td>151333333333</td>
            <td>电商</td>
            <td>
                <a class="btn btn-default" href="#">申请</a>
            </td>
        </tr>
    </table>
</div>
<c:if test="${not empty requestScope.readFileMsg}">
    <div class="alert alert-warning alert-dismissible center" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>${requestScope.readFileMsg}</strong>
    </div>
</c:if>
</body>
</html>
