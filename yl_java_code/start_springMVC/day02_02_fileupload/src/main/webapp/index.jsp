<%-- Date: 2020/1/19 0019 20:17 --%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>index</title>
</head>
<body>
<h3>传统文件上传</h3>
<form action="user/fileupload1" method="POST" enctype="multipart/form-data">
    文件上传：<input type="file" name="upload"/>
    <input type="submit" value="上传" />

</form>


<h3>spring MVC文件上传</h3>
<form action="user/fileupload2" method="POST" enctype="multipart/form-data">
    文件上传：<input type="file" name="uploadXXX"/>
    <input type="submit" value="上传" />

</form>

<h3>跨服务器 文件上传</h3>
<form action="user/fileupload3" method="POST" enctype="multipart/form-data">
    文件上传：<input type="file" name="upload"/>
    <input type="submit" value="上传" />

</form>
</body>
</html>
