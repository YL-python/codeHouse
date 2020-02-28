<%-- Date: 2019/11/20 0020 23:30 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>猿创第一次选拔考试</title>
    <link href="css/考试页面1.css" rel="stylesheet" type="text/css" />
</head>
</body>
<h1 style="text-align: center;">${student.name}欢迎你</h1>
<div id="main"><form action="${pageContext.request.contextPath}/ansServlet?id=${student.id}&name=${student.name}" method="post" id="form" onsubmit="return validateForm()" >
    <table width="100%" border="0">
    <tr>
        <td width="436"> 第三套测试试题</td>
        <td width="80"><input type="submit" id="tijiaoans" value="提交试卷" /></td>
    </tr>

    </table>
    <table width="80%" border="0" align="center">
        <tr>
            <td width="496">1.C语言的程序一行写不下时，可以<u>()</u>.<br />
                <input name="ans1" type="radio" value="A" />
                A.用逗号换行<br />
                <input name="ans1" type="radio" value="B" />
                B.用分号换行<br />
                <input name="ans1" type="radio" value="C" />
                C.在任意一空格处换行<br />
                <input name="ans1" type="radio" value="D" />
                D.用回车换行</td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td height="155">2. 下列正确的标识符是（ ）。  <br />
                <input name="ans2" type="radio" value="A" />
                A.-a1<br />
                <input name="ans2" type="radio" value="B" />
                B.a[i]<br />
                <input name="ans2" type="radio" value="C" />
                C.a2_i<br />
                <input name="ans2" type="radio" value="D" />
                D.int t</td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td>3. C语言中的简单数据类型包括（ ）。  <br />
                <input name="ans3" type="radio" value="A" />
                A、整型、实型、逻辑型   <br />
                <input name="ans3" type="radio" value="B" />
                B、整型、实型、逻辑型、字符型     <br />
                <input name="ans3" type="radio" value="C" />
                C、整型、字符型、逻辑型<br />
                <input name="ans3" type="radio" value="D" />
                D、整型、实型、字符型 <br /></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td><p>4. 若int x=2,y=3,z=4 则表达式(x++)&lt;(--z)?y:z的结果是().<br />
                <input name="ans4" type="radio" value="A" />
                A)4
                <input name="ans4" type="radio" value="B" />
                B)3
                <input name="ans4" type="radio" value="C" />
                C)2
                <input name="ans4" type="radio" value="D" />
                D)0
                <input name="ans4" type="radio" value="E" />
                E)1</p></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td>5.#include &lt;stdio.h&gt; 
                <p>M a I n()<br />
                    { I nt sum = 10,n =1;<br />
                    W hile(n&lt;3)  {su m-=sum; n+ +}<br />
                    Printf(&ldquo;%d,%d&rdquo;,n,s um);<br />
                    }</p>
                <p>运行结果为:
                    <input type="text" name="ans5" id="textfield" />
                </p>
            </td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td>6.#include &lt;stdio.h&gt; 
                <p>main() <br />
                    { int num,c; <br />
                    scanf(&quot;%d&quot;,&amp;num); <br />
                    do {c=num%10;  printf(&quot;%d&quot;,c);   }while((num/=10)&gt;0); <br />
                    printf(&quot;\n&quot;); <br />
                    }</p>
                <p>从键盘输入23,则运行结果为:
                    <label for="textfield2"></label>
                    <input type="text" name="ans6" id="textfield2" />
                </p></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td>7.#include &lt;stdio.h&gt; 
                <p>Main() <br />
                    { char ch; <br />
                    Ch=getcahr(); <br />
                    Switch(ch) <br />
                    { case &lsquo;A&rsquo;:printf(&ldquo;%c&rdquo;，&lsquo;A&rsquo;)； <br />
                    Case &lsquo;B&rsquo;：printf（&ldquo;%c&rdquo;，&lsquo;B&rsquo;）；break； <br />
                    Default：printf（&ldquo;%s&rdquo;，&ldquo;other&rdquo;）； <br />
                    }}</p>
                <p>当从键盘输入字母A时，运行结果为：
                    <label for="textfield3"></label>
                    <input type="text" name="ans7" id="textfield3" />
                </p></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td>8.#include &lt;stdio.h&gt; 
                <p>Main（） <br />
                    { <br />
                    Int y=9； <br />
                    For（；y&gt;0；y--） <br />
                    If（y%3==0） <br />
                    {printf（&ldquo;%d&rdquo;，--y）}<br />
                    } </p>
                <p>运行结果为：
                    <label for="textfield4"></label>
                    <input type="text" name="ans8" id="textfield4" />
                </p></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td height="822"><p><img src="img/1.png" width="334" height="317" /></p>
                <p>
                    <label for="dati1"></label>
                    <textarea name="ans9" id="dati1" cols="45" rows="30"></textarea>
                </p></td>
        </tr>
        <tr>
            <td height="20"><hr /></td>
        </tr>
        <tr>
            <td><p><img src="img/2.png" width="334" height="238" /></p>
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
    function validateForm(){
        if(confirm("是否确认答题结束并交卷！")){
            return true;
        }else {return false}
    }
</script>
</body>
</html>
