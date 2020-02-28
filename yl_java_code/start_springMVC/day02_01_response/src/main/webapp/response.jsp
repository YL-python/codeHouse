<%-- Date: 2020/1/18 0018 16:19 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>

    <script src="js/jquery-3.3.1.min.js"></script>

    <script>
        $(function () {
            $("#btn").click(function () {
                // alert("hello");
                $.ajax({
                    url:"user/testAjax",
                    contentType:"application/json;charset=UTF-8",
                    data:'{"username":"美美","password":"123","age":30}',
                    dataType:"json",
                    type:"POST",
                    success:function (data) {
                        alert(data);
                        alert(data.username);
                        alert(data.password);
                        alert(data.age);
                    }
                });
            });
        });

    </script>
</head>
<body>

<a href="user/testString">testString</a>
<br>
<a href="user/testVoid">testVoid</a>
<br>
<a href="user/testModelAndView">testModelAndView</a>
<br>
<a href="user/testForwardOrRedirect">testForwardOrRedirect</a>

<br>
<button id="btn"> 发送ajax请求</button>


</body>
</html>
