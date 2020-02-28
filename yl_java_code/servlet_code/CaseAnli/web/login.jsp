<%-- Date: 2019/11/11 0011 21:37 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>管理员登陆</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script type="text/javascript">
        function refreshCode() {
            var code = document.getElementById("vcode");
            code.onclick = function (ev) {
                code.src = "${pageContext.request.contextPath}/checkCodeServlet?time=" + new Date().getTime();
            }
        }
    </script>

</head>
<body>
<div class="container" style="width:400px;">
    <h2 style="text-align: center">管理员登录</h2>
    <hr>
    <form action="${pageContext.request.contextPath}/loginServlet"
          method="post">
        <div class="form-group">
            <label for="exampleInputEmail1">用户名</label>
            <input type="text" class="form-control" id="exampleInputEmail1"
                   placeholder="请输入用户名" name="username">
        </div>
        <div class="form-group">
            <label for="exampleInputPassword1">密码</label>
            <input type="password" class="form-control"
                   id="exampleInputPassword1" placeholder="请输入密码"
                   name="password">
        </div>
        <div class="form-inline">
            <label for="exampleInputName3">验证码</label>
            <input type="text" class="form-control" id="exampleInputName3"
                   placeholder="请输入验证码" name="vcode">
            <a href="javascript:refreshCode();">
                <img src="${pageContext.request.contextPath}/checkCodeServlet"
                     title="看不清点击刷新" id="vcode"/>
            </a>
        </div>
        <hr/>
        <div class="form-group" style="text-align: center">
            <input type="submit" class="btn btn-primary" value="登录">
        </div>
    </form>
    <div class="alert alert-warning alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <strong>${login_msg}</strong>
    </div>
</div>
</body>
</html>
