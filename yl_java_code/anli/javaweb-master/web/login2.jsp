<%--登陆页面--%>
<%@ page language="java" contentType="text/html; charset=utf-8"
         pageEncoding="utf-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>login</title>
</head>
<link href="login_css/bootstrap.min.css" rel="stylesheet">
<link href="login_css/signin.css" rel="stylesheet">

<
<script>
    function check() {
        if (far.username.value == "") {
            alert("姓名不能为空!");
            far.username.focus();
            return false;
        }
        if (far.password1.value == "") {
            alert("密码不能为空!");
            far.password1.focus();
            return false;
        }
        return true;
    }
</script>
<body>
<script src="/demos/googlegg.js"></script>

<div class="signin">
    <div class="signin-head"><img src="images/head_120.png" alt="" class="img-circle"></div>
    <form class="form-signin" method="get" action="/login1.jsp" onsubmit="return check()" name="far">
        <input type="text" name="username" class="form-control" placeholder="用户名" autofocus/>
        <input type="password" name="password1" class="form-control" placeholder="密码"/>
        <input class="btn btn-lg btn-warning btn-block" type="submit" value="登录">
        <br>

        <%--<a herf="regist.jsp"><button>没有账号，请注册</button></a>--%>
        <a href="regist2.jsp"> 没有账号，请注册 </a>

    </form>

</div>

<div style="text-align:center;margin:50px 0; font:normal 14px/24px 'MicroSoft YaHei';">


</div>
</body>
</html>