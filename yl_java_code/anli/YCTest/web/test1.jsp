<%-- Date: 2019/11/20 0020 23:28 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="css/text1.css"/>
    <title>猿创第一次选拔考试</title>
</head>
<body>
<h1 style="text-align: center;">${student.name}欢迎你</h1>
<form action="${pageContext.request.contextPath}/ansServlet?id=${student.id}&name=${student.name}" method="post" id="form" onsubmit="return validateForm()">
    <div id="header">
        <table width="100%" border="0">
            <tr>
                <td width="149" height="65">&nbsp;</td>
                <td width="365"><h1>第一套试题</h1></td>
                <td width="237">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="submit" id="tijiaoans" value="提交"/></td>
            </tr>
        </table>
    </div>
    <div id="center">
        <div id="timu">
            <div id="choose">
                <p>1.下列合法的标识符为_____。</p>
                <br />
                <input name="ans1" type="radio" value="A" />
                A.abcd+ <br />
                <br />
                <input name="ans1" type="radio" value="B" />
                B.#KDJF <br />
                <br />
                <input name="ans1" type="radio" value="C" />
                C.67KDJ <br />
                <br />
                <input name="ans1" type="radio" value="D" />
                D.DK3_
                <div id="jiange">
                    <hr />
                </div>
                <p>2.下面程序的输出是________。</p>
                <p> #include&lt;stdio.h&gt;</p>
                <p>  #include&lt;string.h&gt;</p>
                <p> Main()</p>
                <p> {char p1[10]="abc"，p2[]="ABC"，str[50]="xyz"；</p>
                <p> strcpy(str，strcat(p1，p2));</p>
                <p>printf("%s\n"，str)；
                    }</p>
                <br />
                <input name="ans2" type="radio" value="A" />
                A. xyzABCabc <br />
                <br />
                <input name="ans2" type="radio" value="B" />
                B.abcABC<br />
                <br />
                <input name="ans2" type="radio" value="C" />
                C.xyabcABC<br />
                <br />
                <input name="ans2" type="radio" value="D" />
                D.xyzabcABC
                <div id="jiange">
                    <hr />
                </div>
                <p>3.对for（表达式1; ;表达式3）可理解为_____。</p>
                <br />
                <input name="ans3" type="radio" value="A" />
                A.for（表达式1;  ;表达式3）<br />
                <br />
                <input name="ans3" type="radio" value="B" />
                B.for（表达式1; 1 ;表达式3）<br />
                <br />
                <input name="ans3" type="radio" value="C" />
                C.for（表达式1;表达式1 ;表达式3）<br />
                <br />
                <input name="ans3" type="radio" value="D" />
                D.for（表达式1;表达式3 ;表达式3）
                <div id="jiange">
                    <hr />
                </div>
                <p>4.若有代数式3ae/bc,则不正确的C语言表达式是_____。</p>
                <br />
                <input name="ans4" type="radio" value="A" />
                A.a/b/c*e*3<br />
                <br />
                <input name="ans4" type="radio" value="B" />
                B.3*a*e/b/c<br />
                <br />
                <input name="ans4" type="radio" value="C" />
                C.3*a*e/b*c<br />
                <br />
                <input name="ans4" type="radio" value="D" />
                D.a*e/c/b*3
                <hr />
            </div>
            <div id="tiankong">
                <p>5.已知int a[3][2]={3,2,1};则表达式“a[0][0]/a[0][1]”的值是
                    <input name="ans5" type="text" />
                </p>
                <div id="jiange">
                    <hr />
                </div>
                <p>6.下面程序段的运行结果为
                    <input name="ans6" type="text" />
                    。
                    x=2;
                    do{printf("*");x--;}while(!x==0);</p>
                <div id="jiange">
                    <hr />
                </div>
                <p>7.设a、b、c均为int型变量且a=6,b=4,c=2,则表达式！(a-b)+c-1 && b+c/2的值是
                    <input name="ans7" type="text" />
                </p>
                <div id="jiange">
                    <hr />
                </div>
                <p>8.若有条件"2&lt;x&lt;3或"x&lt;-10",其对应的C语言表达式是
                    <input name="ans8" type="text" />
                </p>
                <div id="jiange">
                    <hr />
                </div>
            </div>
            <div id="biancheng">
                <p>9.随机输入十个数，编程实现排序。（用冒泡排序）</p>
                <textarea cols="40" rows="30" name="ans9"></textarea>
                <div id="jiange">
                    <hr />
                </div>
                <p>10.打印杨辉三角。</p>
                <textarea cols="40" rows="30" name="ans10"></textarea>
                <div id="jiange"></div>
            </div>
        </div>
    </div>
</form>
<p style="text-align: center;"> © 南昌理工学院 猿创工作室</p>
<script>
    function validateForm(){
        if(confirm("是否确认答题结束并交卷！")){
            return true;
        }else {return false}
    }
</script>
</body>
</html>
