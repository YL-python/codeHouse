<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>register</title>
    <meta content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no" name="viewport">
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/ionicons/css/ionicons.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/adminLTE/css/AdminLTE.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/iCheck/square/blue.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/datepicker/datepicker3.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/datatables/dataTables.bootstrap.css">
</head>

<body class="hold-transition register-page">
<div class="register-box">
    <div id="warning_div" class="alert alert-warning alert-dismissible" style="display: none">
        <h4>
            <i class="icon fa fa-warning"></i>
                警报！
            </h4>
        <span id="warning_i">此警报是可忽略的。</span>
    </div>

    <div class="register-logo">
        <a href="${pageContext.request.contextPath}/login.jsp"><b>猿创</b>人员管理系统</a>
    </div>

    <div class="register-box-body">
        <p class="login-box-msg">新用户注册</p>

        <form action="${pageContext.request.contextPath}/user/register" method="post" onsubmit="return sub()">
            <div class="form-group has-feedback">
                <input type="text" class="form-control" id="username" name="username" placeholder="自定义用于登录的账号">
                <span class="glyphicon glyphicon-user form-control-feedback"></span>
            </div>

            <div class="form-group has-feedback">
                <input type="password" class="form-control" id="password_1" placeholder="登录密码">
                <span class="glyphicon glyphicon-lock form-control-feedback"></span>
            </div>
            <div class="form-group has-feedback">
                <input type="password" class="form-control" id="password_2" name="password" placeholder="确认密码">
                <span class="glyphicon glyphicon-log-in form-control-feedback"></span>
            </div>
            <div class="form-group has-feedback">
                <input type="text" class="form-control" id="invite_code" placeholder="邀请码">
                <span class="glyphicon glyphicon-tags form-control-feedback"></span>
            </div>

            <div class="form-group has-feedback">
                <input type="text" class="form-control" id="userXingMing" name="userXingMing" placeholder="您的姓名">
                <span class="glyphicon glyphicon-star form-control-feedback"></span>
            </div>

            <div class="form-group">
                <select class="form-control" id="userSex" name="userSex">
                    <option value="未填写"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">性别</font></font></option>
                    <option value="男"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">人家这么可爱当然是男孩子</font></font></option>
                    <option value="女"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">我是需要多喝热水的女孩子</font></font></option>
                </select>
            </div>

            <div class="form-group has-feedback">
                <input type="text" class="form-control" id="userPhoneNum" name="userPhoneNum" placeholder="您的电话">
                <span class="glyphicon glyphicon-phone-alt form-control-feedback"></span>
            </div>
            <div class="form-group ">
                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
                    <select class="form-control" id="grade" name="grade">
                        <option value="未填写">年级</option>
                        <option value="2015">2015</option>
                        <option value="2016">2016</option>
                        <option value="2017">2017</option>
                        <option value="2017">2018</option>
                        <option value="2019">2019</option>
                        <option value="2020">2020</option>
                        <option value="2021">2021</option>
                        <option value="2022">2022</option>
                    </select>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
                    <select class="form-control" id="professional" name="professional">
                        <option value="未填写">专业</option>
                        <option value="大数据">大数据</option>
                        <option value="计应">计应</option>
                        <option value="计网">计网</option>
                        <option value="软工">软工</option>
                        <option value="电商">电商</option>
                    </select>
                </div>
                <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
                    <select class="form-control" id="class_" name="class_">
                        <option value="未填写">班级</option>
                        <option value="一班">一班</option>
                        <option value="二班">二班</option>
                        <option value="三班">三班</option>
                        <option value="四班">四班</option>
                        <option value="五班">五班</option>
                    </select>
                </div>
            </div>

            <div class="form-group col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <label><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">出生日期：</font></font></label>
                <div class="input-group date ">
                    <div class="input-group-addon">
                        <i class="fa fa-calendar"></i>
                    </div>
                    <input type="text" class="form-control pull-right" id="datepicker" name="userBirthday" placeholder="yyyy/mm/dd">
                </div>
                <!-- /.input group -->
            </div>

            <div class="row">
                <div class="col-xs-8">
                    <div class="checkbox icheck">
                        <label>
                            <input type="checkbox"> 我同意 <a href="#">协议</a>
                        </label>
                    </div>
                </div>
                <div class="col-xs-4">
                    <button type="submit" id="submit_btn" class="btn btn-primary btn-block btn-flat" >注册</button>
                </div>
            </div>
        </form>
        <div class="social-auth-links text-center">
            <p>- 或者 -</p>
            <a href="${pageContext.request.contextPath}/login.jsp" class="text-center">我有账号，现在就去登录</a>
        </div>
    </div>
</div>
<script src="${pageContext.request.contextPath}/plugins/jQuery/jquery-2.2.3.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap/js/bootstrap.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/iCheck/icheck.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datatables/jquery.dataTables.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datatables/dataTables.bootstrap.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/moment.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.zh-CN.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datepicker/bootstrap-datepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datepicker/locales/bootstrap-datepicker.zh-CN.js"></script>
<script>
    $(function () {
        $('input').iCheck({
            checkboxClass: 'icheckbox_square-blue',
            radioClass: 'iradio_square-blue',
            increaseArea: '20%' // optional
        });
    });
    //Date picker
    $('#datepicker').datepicker({
        autoclose: true,
        format: 'yyyy/mm/dd'
    });
</script>
<script>
    function checkUsername(){
        var flag;
        // 获取账号
        var username = $("#username").val();
        // 定义正则
        var re_username = /^.{3,16}$/;
        if (re_username.test(username)) {
            $.ajax({
                type:"post",
                url:"${pageContext.request.contextPath}/user/findUserName",
                contentType:"application/json;charset=utf-8",
                data:JSON.stringify({"username": username}),
                dataType:"json",
                success:function(data){
                    if(!data['flag']){
                        // 用户不存 在可用
                        $("#username").css("border", "");
                        $("#warning_div").css("display", "none");
                        flag = true;
                    }else{
                        // 校验失败，账号不合法
                        $("#username").css("border", "2px solid red");
                        $("#warning_div").css("display", "block");
                        $("#warning_i").html("该用户已存在,换一个名称在试试把")
                        flag = false;
                    }
                }
            });
        } else {
            // 校验失败，账号不合法
            $("#username").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("用户名的长度在3 - 16个字符之间")
            flag = false;
        }
        return flag.valueOf();
    }
    // 校验密码的方法   单词字符，长度8到20位
    function checkPassword1() {
        // 获取密码
        var password1 = $("#password_1").val();
        // 定义正则
        var re_password = /^.*(?=.{8,16})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&*?\(\)+=\[\]\{\}_<>,.;:'"-]).*$/;
        // 判断 给出提示信息
        var flag = re_password.test(password1);
        if (flag) {
            // 校验成功，账号合法
            $("#password_1").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            // 校验失败，账号不合法
            $("#password_1").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("密码需要至少一个数字一个字母和一个特殊符号,长度8 - 16位之间");
        }
        return flag;
    }
    function checkPassword2(){
        var password1 = $("#password_1").val();
        var password2 = $("#password_2").val();
        var flag = password1 == password2;
        if (flag) {
            // 校验成功，账号合法
            $("#password_2").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            // 校验失败，账号不合法
            $("#password_2").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("两次输入的密码不一致");
        }
        return flag;
    }
    function checkInvite_code(){
        var invite_code = $("#invite_code").val();
        var flag = invite_code == "yuanchuang";
        if (flag) {
            // 校验成功，账号合法
            $("#invite_code").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            // 校验失败，账号不合法
            $("#invite_code").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("邀请码错误");
        }
        return flag;
    }

    function checkUserXingMing(){
        var userXingMing = $("#userXingMing").val();
        // 定义正则
        var re_userXingMing = /^.{2,15}$/;
        // 判断 给出提示信息
        var flag = re_userXingMing.test(userXingMing);
        if (flag) {
            // 校验成功，账号合法
            $("#userXingMing").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            // 校验失败，账号不合法
            $("#userXingMing").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("名称格式有误，长度在2-15个字符之间");
        }
        return flag;
    }
    function checkUserSex(){
        var userSex = $("#userSex").val();
        var flag = userSex != "未填写";
        if (flag) {
            $("#userSex").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#userSex").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请选择性别");
        }
        return flag;
    }
    function checkUserPhoneNum(){
        var userPhoneNum = $("#userPhoneNum").val();
        // 定义正则
        var re_userPhoneNum = /^1(?:3\d|4[4-9]|5[0-35-9]|6[67]|7[013-8]|8\d|9\d)\d{8}$/;
        // 判断 给出提示信息
        var flag = re_userPhoneNum.test(userPhoneNum);
        if (flag) {
            $("#userPhoneNum").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#userPhoneNum").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请输入正确的手机号码");
        }
        return flag;
    }

    function checkDatepicker(){
        var datepicker = $("#datepicker").val();
        // 定义正则
        var re_datepicker = /^\d\d\d\d\/\d\d\/\d\d$/;
        // 判断 给出提示信息
        var flag = re_datepicker.test(datepicker);
        if (flag) {
            $("#datepicker").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#datepicker").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请正确的生日格式 yyyy/MM/dd");
        }
        return flag;
    }

    function checkgrade(){
        var grade = $("#grade").val();
        var flag = grade !="未填写";
        if (flag) {
            $("#grade").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#grade").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请输入完整专业信息");
        }
        return flag;
    }
    function checkprofessional(){
        var professional = $("#professional").val();
        var flag = professional !="未填写";
        if (flag) {
            $("#professional").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#professional").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请输入完整专业信息");
        }
        return flag;
    }
    function checkclass_(){
        var class_ = $("#class_").val();
        var flag = class_ !="未填写";
        if (flag) {
            $("#class_").css("border", "");
            $("#warning_div").css("display", "none");
        } else {
            $("#class_").css("border", "2px solid red");
            $("#warning_div").css("display", "block");
            $("#warning_i").html("请输入完整专业信息");
        }
        return flag;
    }

    function sub(){
        if(checkUsername() && checkPassword2() && checkInvite_code() && checkUserXingMing() && checkUserSex() && checkUserPhoneNum() && checkgrade() && checkprofessional() && checkclass_() && checkDatepicker()){
            return true;
        }else{
            alert("表单没有全部填写正确哦");
            return false;
        }
    }
    $(function () {
        $("#username").blur(checkUsername);
        $("#password_1").blur(checkPassword1);
        $("#password_2").blur(checkPassword2);
        $("#invite_code").blur(checkInvite_code);
        $("#userXingMing").blur(checkUserXingMing);
        $("#userSex").blur(checkUserSex);
        $("#userPhoneNum").blur(checkUserPhoneNum);
        $("#grade").blur(checkgrade);
        $("#professional").blur(checkprofessional);
        $("#class_").blur(checkclass_);
        $("#datepicker").blur(checkDatepicker);
    })
</script>
</body>
</html>