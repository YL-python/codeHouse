<%-- Date: 2019/11/12 0012 17:06 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>用户信息</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <style>
        .container{text-align: center;}
        td, th{text-align: center;}
        #head-two-btn{
            float: right;
            margin: 5px;
        }
        #form-inline{float: left;}
    </style>
    <script>
        // 有参数传递
        function delUser( id ) {
            // 给出安全提示框
            if(confirm("是否确定删除数据")){
                // 访问数据
                location.href = "${pageContext.request.contextPath}/delUserServlet?id="+id;
            }
        }
        function upData( id ) {
            // 给出安全提示框
            if(confirm("是否确定修改数据")){
                // 访问数据
                location.href = "${pageContext.request.contextPath}/findUserServlet?id="+id;
            }
        }
        window.onload = function () {
            // 点击了删除选中就提交表单
            document.getElementById("delcheck").onclick = function () {
                // 判断是否有选中的数据
                var uids = document.getElementsByName("uid");
                var flag = false;
                for (var i = 0; i < uids.length; i++) {
                    if(uids[i].checked){
                        flag=true;
                        break
                    }
                }
                if (flag){
                    // 给提示信息
                    if(confirm("危险危险！！！是否要删除选中数据？？")){
                        document.getElementById("form").submit()
                    }
                }else {
                    alert("您未有选中的数据！")
                }

            }

            document.getElementById("allcheck").onclick = function (ev) {
                var flag = this.checked;
                var uids = document.getElementsByName("uid");
                for (var i = 0; i < uids.length; i++) {
                    uids[i].checked = flag;
                }
            }
        }
    </script>
</head>
<body>
<h2>欢迎您！${sessionScope.admin.username}</h2>
<div class="container">
    <h3 class="container">用户信息列表</h3>

    <form class="form-inline" id="form-inline" action="${pageContext.request.contextPath}/findUserByPageServlet" method="post">
        <div class="form-group">
            <label for="InputName">姓名</label>
            <input type="text" name="name" value="${parameterMap.name[0]}" class="form-control" id="InputName">
        </div>
        <div class="form-group">
            <label for="InputAge">年龄</label>
            <input type="text" name="age" value="${parameterMap.age[0]}" class="form-control" id="InputAge">
        </div>
        <div class="form-group">
            <select class="form-control" name="address">
                <c:if test="${not empty parameterMap.address[0]}">
                    <option value="">all</option>
                </c:if>
                <c:if test="${empty parameterMap.address[0]}">
                    <option selected="selected" value="">all</option>
                </c:if>
                <c:forEach items="${sessionScope.citys}" var="city">
                    <c:if test="${parameterMap.address[0] == city}">
                        <option value="${city}" selected="selected">${city}</option>
                    </c:if>
                    <c:if  test="${parameterMap.address[0] != city}">
                        <option value="${city}">${city}</option>
                    </c:if>
                </c:forEach>
            </select>
        </div>
        <button type="submit" class="btn btn-default">查询</button>
    </form>

    <div id="head-two-btn">
        <a class="btn btn-primary" href="${pageContext.request.contextPath}/add.jsp" role="button">添加联系人</a>
        <a class="btn btn-primary" href="#javascript:void(0)" id="delcheck">删除选中</a>
    </div>

    <form action="${pageContext.request.contextPath}/delCheckUserServlet" method="post" id="form">
        <table class="table table-bordered table-hover">
            <tr class="success" >
                <th> <input id="allcheck" type="checkbox"></th>
                <th>编号</th>
                <th>姓名</th>
                <th>性别</th>
                <th>年龄</th>
                <th>籍贯</th>
                <th>QQ</th>
                <th>邮箱</th>
                <th>操作</th>
            </tr>
            <c:forEach items="${pb.userList}" var="user" varStatus="s">
                <tr>
                    <td> <input type="checkbox" name="uid" value="${user.id}"></td>
                    <td>${s.count}</td>
                    <td>${user.name}</td>
                    <td>${user.gender}</td>
                    <td>${user.age}</td>
                    <td>${user.address}</td>
                    <td>${user.qq}</td>
                    <td>${user.email}</td>
                    <td>
                        <a class="btn btn-default" href="javascript:upData(${user.id});">修改</a>
                        <a class="btn btn-default" href="javascript:delUser(${user.id});">删除</a>
                    </td>
                </tr>
            </c:forEach>
        </table>
    </form>


    <nav aria-label="Page navigation">
        <ul class="pagination "style="float: left;">
            <c:if test="${pb.currentPage==1}">
                <li class="disabled">
                    <span href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${pb.currentPage-1}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </span>
                </li>
            </c:if>
            <c:if test="${pb.currentPage!=1}">
                <li>
                    <span href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${pb.currentPage-1}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </span>
                </li>
            </c:if>
            <c:forEach begin="1" end="${pb.totalPage}" step="1" var="i">
                <c:if test="${pb.currentPage == i}">
                    <li class="active"><a href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${i}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}">${i}</a></li>
                </c:if>
                <c:if test="${pb.currentPage != i}">
                    <li ><a href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${i}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}">${i}</a></li>
                </c:if>
            </c:forEach>
            <c:if test="${pb.currentPage != pb.totalPage}">
                <li>
                    <span href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${pb.currentPage+1}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </span>
                </li>
            </c:if>
            <c:if test="${pb.currentPage == pb.totalPage}">
                <li class="disabled">
                    <span href="${pageContext.request.contextPath}/findUserByPageServlet?currentPage=${pb.currentPage+1}&name=${parameterMap.name[0]}&age=${parameterMap.age[0]}&address=${parameterMap.address[0]}" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </span>
                </li>
            </c:if>

            <span style="font-size: 25px;margin: 5px"> 共${pb.totalCount}条记录，共${pb.totalPage}页</span>
        </ul>
    </nav>

</div>
</body>
</html>
