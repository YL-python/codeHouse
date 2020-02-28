<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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
</head>
<body>

<div class="container">
    <h3 class="container">用户信息列表</h3>

    <form class="form-inline" id="form-inline">
        <div class="form-group">
            <label for="exampleInputName2">姓名</label>
            <input type="text" class="form-control" id="exampleInputName2">
        </div>
        <div class="form-group">
            <label for="exampleInputName3">籍贯</label>
            <input type="text" class="form-control" id="exampleInputName3">
        </div>
        <div class="form-group">
            <label for="exampleInputEmail2">邮箱</label>
            <input type="email" class="form-control" id="exampleInputEmail2">
        </div>
        <button type="submit" class="btn btn-default">查询</button>
    </form>

    <div id="head-two-btn">
        <a class="btn btn-default" href="#" role="button">添加联系人</a>
        <a class="btn btn-default" href="#" role="button">删除选中</a>
    </div>

    <table class="table table-bordered table-hover">
        <tr class="success">
            <th> <input type="checkbox"></th>
            <th>编号</th>
            <th>姓名</th>
            <th>性别</th>
            <th>年龄</th>
            <th>籍贯</th>
            <th>QQ</th>
            <th>邮箱</th>
            <th>操作</th>
        </tr>
        <tr>
            <td> <input type="checkbox"></td>
            <td>1</td>
            <td>杨龙</td>
            <td>男</td>
            <td>19</td>
            <td>江西</td>
            <td>123456</td>
            <td>123456@qq.com</td>
            <td>
                <button class="btn btn-default" type="submit">删除</button>
                <button class="btn btn-default" type="submit">修改</button>
            </td>
        </tr>
        <tr>
            <td> <input type="checkbox"></td>
            <td>2</td>
            <td>黄猪猪</td>
            <td>女</td>
            <td>19</td>
            <td>江西</td>
            <td>123456</td>
            <td>123456@qq.com</td>
            <td>
                <button class="btn btn-default" type="submit">删除</button>
                <button class="btn btn-default" type="submit">修改</button>
            </td>
        </tr>
    </table>

    <nav aria-label="Page navigation">
        <ul class="pagination "style="float: left;">
            <li>
                <a href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            <li><a href="#">1</a></li>
            <li><a href="#">2</a></li>
            <li><a href="#">3</a></li>
            <li><a href="#">4</a></li>
            <li><a href="#">5</a></li>
            <li>
                <a href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
            <span style="font-size: 25px;margin: 5px"> 共16条记录，共四页</span>
        </ul>
    </nav>

</div>

</body>
</html>