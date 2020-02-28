<%-- Date: 2019/11/20 0020 19:01 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>猿创第一次选拔考试</title>
  <link rel="stylesheet" type="text/css" href="css/登录页面.css" />
</head>
<body>
<div class="music-lgin">
  <div class="music-lgin-all">
    <!--左手-->
    <div class="music-lgin-left ovhd">
      <div class="music-hand">
        <div class="music-lgin-hara"></div>
        <div class="music-lgin-hars"></div>
      </div>
    </div>
    <!--脑袋-->
    <div class="music-lgin-dh">
      <div class="music-lgin-alls">
        <div class="music-lgin-eyeleft">
          <div class="music-left-eyeball yeball-l"></div>
        </div>
        <div class="music-lgin-eyeright">
          <div class="music-right-eyeball yeball-r"></div>
        </div>
        <div class="music-lgin-cl"></div>
      </div>
      <!--鼻子-->
      <div class="music-nose"></div>
      <!--嘴-->
      <div class="music-mouth music-mouth-ds"></div>
      <!--肩-->
      <div class="music-shoulder-l">
        <div class="music-shoulder"></div>
      </div>
      <div class="music-shoulder-r">
        <div class="music-shoulder"></div>
      </div>
      <!--消息框-->
      <div class="music-news">Welcome to "YC猿创工作室"</div>
    </div>
    <div class="music-lgin-right ovhd">
      <div class="music-hand">
        <div class="music-lgin-hara"></div>
        <div class="music-lgin-hars"></div>
      </div>
    </div>
  </div>
  <form action="${pageContext.request.contextPath}/loginServlet" method="post" onsubmit="return validateForm()">
    <!--1-->
    <div class="music-lgin-text">
      <input class="inputname inputs" id="name" name="name" type="text" placeholder="姓名" />
    </div>
    <div class="music-lgin-text">
      <select class="inputname inputs" type="text" placeholder="姓名" name="classroom">
        <option value="19-大数据1班">19-大数据1班</option>
        <option value="19-大数据2班">19-大数据2班</option>
        <option value="19-电商1班">19-电商1班</option>
        <option value="19-软工1班">19-软工1班</option>
        <option value="19-软工2班">19-软工2班</option>
        <option value="19-软工3班">19-软工3班</option>
        <option value="19-软工4班">19-软工4班</option>
        <option value="19-计算机科学与技术1班">19-计算机科学与技术1班</option>
        <option value="19-计算机科学与技术2班">19-计算机科学与技术2班</option>
        <option value="19-计算机科学与技术3班">19-计算机科学与技术3班</option>
        <option value="19-计算机科学与技术4班">19-计算机科学与技术4班</option>
        <option value="19-计算机科学与技术5班">19-计算机科学与技术5班</option>
        <option value="19-计算机应用1班">19-计算机应用1班</option>
        <option value="其他班级">其他班级</option>
      </select>
    </div >
    <div class="music-lgin-text">
      <input id="tel" name="tel" class="mima inputs" placeholder="电话" />
    </div>
    <div class="music-lgin-text">
      <input class="music-qd inputs" type="submit" value="登录" />
    </div>
  </form>
</div>

<script src="js/登录页面.js"></script>
<script type="text/javascript">
  //眼睛 密码部分
  $(".mima").focus(function () {
    $(".music-lgin-left").addClass("left-dh").removeClass("rmleft-dh");
    $(".music-lgin-right").addClass("right-dh").removeClass("right-rmdh");
    $(".music-hand").addClass("no");
  }).blur(function () {
    $(".music-lgin-left").removeClass("left-dh").addClass("rmleft-dh");
    $(".music-lgin-right").removeClass("right-dh").addClass("right-rmdh");
    $(".music-hand").removeClass("no");

  })
  //点击小人出来
  $(".inputname").focus(function () {
    $(".music-lgin-all").addClass("block");
  })

  function validateForm()
  {
    var name=document.getElementById("name").value;
    if (name==null || name=="")
    {
      alert("姓名必须填写");
      return false;
    }
    var tel=document.getElementById("tel").value;
    if (tel==null || tel=="")
    {
      alert("电话必须填写");
      return false;
    }
  }
</script>
<p style="text-align: center;"> © 南昌理工学院 猿创工作室</p>
</body>
</html>
