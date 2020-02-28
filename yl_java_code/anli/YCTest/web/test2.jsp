<%-- Date: 2019/11/20 0020 23:29 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>猿创第一次选拔考试</title>
    <link href="css/考试页面1.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div id="main">
    <h1 style="text-align: center;">${student.name}欢迎你</h1>
    <form action="${pageContext.request.contextPath}/ansServlet?id=${student.id}&name=${student.name}" method="post" id="form" onsubmit="return validateForm()" >
    <table width=" 100%" border="0">
    <tr>
        <td width="436"> 第二套测试试题</td>
        <td width="80"><input id="tijiaoans" type="submit" value="提交试卷"/></td>
    </tr>

    </table>
    <table width="80%" border="0" align="center">
        <tr>
            <td width="496">1.运算符 +、<=、=、%中，优先级最低的运算符是____</u>.<br/>
                <input name="ans1" type="radio" value="A"/>
                A.+<br/>
                <input name="ans1" type="radio" value="B"/>
                B.<=<br/>
                <input name="ans1" type="radio" value="C"/>
                C.=<br/>
                <input name="ans1" type="radio" value="D"/>
                D.%
            </td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td height="155">2.字符串""EOF= -\61\""的长度是____ <br/>
                <input name="ans2" type="radio" value="A"/>
                A.8<br/>
                <input name="ans2" type="radio" value="B"/>
                B.9<br/>
                <input name="ans2" type="radio" value="C"/>
                C.12<br/>
                <input name="ans2" type="radio" value="D"/>
                D.非法字符串
            </td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td>3.下列_____是C语言的有效标识符？  <br/>
                <input name="ans3" type="radio" value="A"/>
                A.$int<br/>
                <input name="ans3" type="radio" value="B"/>
                B.No.1 <br/>
                <input name="ans3" type="radio" value="C"/>
                C.12345<br/>
                <input name="ans3" type="radio" value="D"/>
                D._No1<br/></td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td><p>4.int k=10;
                while(k=0)k=k-1;
                则下面描述正确的是____.<br/>
                <input name="ans4" type="radio" value="A"/>
                A.while循环执行10次
                <input name="ans4" type="radio" value="B"/>
                B.循环是无限循环
                <input name="ans4" type="radio" value="C"/>
                C.循环体语句一次也不执行
                <input name="ans4" type="radio" value="D"/>
                D.循环体语句执行一次
            </p></td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td>5.若x、y、z均为int型变量，则描述"x或y中有一个小于z"的表达式是____</p>
                <p>
                    <input type="text" name="ans5" id="textfield"/>
                </p>
            </td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td>6.设a、b均为int型变量且a=2，b=4，则表达式!(x=a) || (y=b) && 0的值是
                <p>
                    <label for="textfield2"></label>
                    <input type="text" name="ans6" id="textfield2"/>
                </p></td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td>7.如果需要从被调函数返回一个函数值，被调函数必须包含
                <label for="textfield3"></label>
                <input type="text" name="ans7" id="textfield3"/>语句。

                </p></td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td>8.在函数中使用else总是
                <label for="textfield4"></label>
                <input type="text" name="ans8" id="textfield4"/>_的if配对，而不管程序的书写格式如何。

                </p></td>
        </tr>
        <tr>
            <td height="16">
                <hr/>
            </td>
        </tr>
        <tr>
            <td height="515"><p>9.随机输入十个整数，编程实现从大到小的排序。（冒泡排序）</p>
                <p><label for="dati1"></label>
                    <textarea name="ans9" id="dati1" cols="45" rows="30"></textarea>
                </p></td>
        </tr>
        <tr>
            <td height="20">
                <hr/>
            </td>
        </tr>
        <tr>
            <td><p><img src="img/untitled.jpg" width="209" height="337"/></p>
                <p>
                    <label for="dati2"></label>
                    <textarea name="ans10" id="dati2" cols="45" rows="30"></textarea>
                </p></td>
        </tr>
    </table>
    </form>
</div>
<p style="text-align: center;"> © 南昌理工学院 猿创工作室</p>
<script>
    function validateForm() {
        if (confirm("是否确认答题结束并交卷！")) {
            return true;
        } else {
            return false
        }
    }
</script>
</body>
</html>
