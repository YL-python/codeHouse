<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" isELIgnored="false" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <!-- 页面meta -->
    <meta charset="utf-8">
    <title>猿创工作室</title>
    <!-- Tell the browser to be responsive to screen width -->
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/ionicons/css/ionicons.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/iCheck/square/blue.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/morris/morris.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/jvectormap/jquery-jvectormap-1.2.2.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/datepicker/datepicker3.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/datatables/dataTables.bootstrap.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/treeTable/jquery.treetable.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/treeTable/jquery.treetable.theme.default.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/select2/select2.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/colorpicker/bootstrap-colorpicker.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-markdown/css/bootstrap-markdown.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/adminLTE/css/AdminLTE.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/adminLTE/css/skins/_all-skins.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/css/style.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/ionslider/ion.rangeSlider.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/ionslider/ion.rangeSlider.skinNice.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-slider/slider.css">
</head>

<body class="hold-transition skin-blue sidebar-mini">

<div class="wrapper">

    <!-- 页面头部 -->
    <jsp:include page="header.jsp"></jsp:include>
    <!-- 页面头部 /-->

    <!-- 导航侧栏 -->
    <jsp:include page="aside.jsp"></jsp:include>
    <!-- 导航侧栏 /-->

    <!-- 内容区域 -->
    <div class="content-wrapper">

        <!-- 内容头部 -->
        <section class="content-header">
            <h1>
                个人信息管理 <small>修改个人信息</small>
            </h1>
            <ol class="breadcrumb">
                <li><a href="${pageContext.request.contextPath}/index.jsp"><i
                        class="fa fa-dashboard"></i> 首页</a></li>
                <li><a
                        href="${pageContext.request.contextPath}/permission/findAll.do">资源权限管理</a></li>

                <li class="active">全部权限</li>
            </ol>
        </section>
        <!-- 内容头部 /-->
        <form action="${pageContext.request.contextPath}/user/update" method="post">
            <!-- 正文区域 -->
            <section class="content"> <!-- .box-body -->
                <!--基础控件-->
                <div class="tab-pane" id="tab-common">
                    <div class="row data-type">
                        <input type="hidden" class="form-control" placeholder="${user.id}" name="id" value="${user.id}">
<%--                        ${sessionScope.SPRING_SECURITY_CONTEXT.authentication.principal.username}  --%>
                        <div class="col-md-2 title">登录账号</div>
                        <div class="col-md-4 data">
                            <input type="text" class="form-control" placeholder="${user.username}" name="username" value="${user.username}">
                        </div>

                        <div class="col-md-2 title">登录密码</div>
                        <div class="col-md-4 data">
                            <input type="text" class="form-control" placeholder="${user.password}" name="password" value="${user.password}">
                        </div>

                        <div class="col-md-2 title">姓名</div>
                        <div class="col-md-4 data">
                            <input type="text" class="form-control" placeholder="${user.userXingMing}" name="userXingMing" value="${user.userXingMing}">
                        </div>

                        <div class="col-md-2 title">性别</div>
                        <div class="col-md-4 data">
                            <input type="text" class="form-control" placeholder="${user.userSex}" name="userSex" value="${user.userSex}">
                        </div>

                        <div id="gradeid" style="display: none">${user.grade}</div>
                        <div id="professionalid" style="display: none">${user.professional}</div>
                        <div id="class_id" style="display: none">${user.class_}</div>


                        <div class="col-md-1 title">年级</div>
                        <div class="col-md-3 data">
                            <select class="form-control" name="grade" id="select_grade">
                                <option value="未填写">未填写</option>
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
                        <div class="col-md-1 title">专业</div>
                        <div class="col-md-3 data">
                            <select class="form-control" name="professional" id="select_professional">
                                <option value="未填写" >未填写</option>
                                <option value="大数据">大数据</option>
                                <option value="计应">计应</option>
                                <option value="计网">计网</option>
                                <option value="软工">软工</option>
                                <option value="电商">电商</option>
                            </select>
                        </div>
                        <div class="col-md-1 title">班级</div>
                        <div class="col-md-3 data">
                            <select class="form-control" name="class_" id="select_class">
                                <option value="未填写" >未填写</option>
                                <option value="一班">一班</option>
                                <option value="二班">二班</option>
                                <option value="三班">三班</option>
                                <option value="四班">四班</option>
                                <option value="五班">五班</option>
                            </select>
                        </div>

                        <div class="col-md-2 title">电话号码</div>
                        <div class="col-md-4 data">
                            <input type="text" class="form-control" placeholder="${user.userPhoneNum}" name="userPhoneNum" value="${user.userPhoneNum}">
                        </div>

                        <div class="col-md-2 title">出生日期</div>
                        <div class="col-md-4 data">
                            <div class="input-group date">
                                <div class="input-group-addon">
                                    <i class="fa fa-calendar"></i>
                                </div>
                                <input type="text" class="form-control pull-right" id="datepicker" value="${user.userBirthdayStr}" name="userBirthday" placeholder="${user.userBirthdayStr}">
                            </div>
                        </div>

                        <div class="col-md-2 title"></div>
                        <div class="col-md-10 data text-center">
                            <button type="submit" class="btn bg-maroon">
                                保存
                            </button>
                            <button type="button" class="btn bg-default"
                                    onclick="history.back(-1);">返回
                            </button>
                        </div>

                    </div>
                </div>
            </section>
        </form>
    </div>
    <!-- 内容区域 /-->

    <!-- 底部导航 -->
    <footer class=" main-footer">
        <div class="pull-right hidden-xs">
            <b>Version</b> 1.0.1
        </div>
        <strong>Copyright &copy; 2014-2020 <a
                href="#">猿创工作室.版权所有</a>.
        </strong> PowerBy 18-大数据-杨龙.
    </footer>
    <!-- 底部导航 /-->

</div>

<script src="${pageContext.request.contextPath}/plugins/jQuery/jquery-2.2.3.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/jQueryUI/jquery-ui.min.js"></script>
<script>
    $.widget.bridge('uibutton', $.ui.button);
</script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap/js/bootstrap.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/raphael/raphael-min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/morris/morris.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/sparkline/jquery.sparkline.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/jvectormap/jquery-jvectormap-1.2.2.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/jvectormap/jquery-jvectormap-world-mill-en.js"></script>
<script src="${pageContext.request.contextPath}/plugins/knob/jquery.knob.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/moment.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.zh-CN.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datepicker/bootstrap-datepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datepicker/locales/bootstrap-datepicker.zh-CN.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/slimScroll/jquery.slimscroll.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/fastclick/fastclick.js"></script>
<script src="${pageContext.request.contextPath}/plugins/iCheck/icheck.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/adminLTE/js/app.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/treeTable/jquery.treetable.js"></script>
<script src="${pageContext.request.contextPath}/plugins/select2/select2.full.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/colorpicker/bootstrap-colorpicker.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-wysihtml5/bootstrap-wysihtml5.zh-CN.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-markdown/js/bootstrap-markdown.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-markdown/locale/bootstrap-markdown.zh.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-markdown/js/markdown.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-markdown/js/to-markdown.js"></script>
<script src="${pageContext.request.contextPath}/plugins/ckeditor/ckeditor.js"></script>
<script src="${pageContext.request.contextPath}/plugins/input-mask/jquery.inputmask.js"></script>
<script src="${pageContext.request.contextPath}/plugins/input-mask/jquery.inputmask.date.extensions.js"></script>
<script src="${pageContext.request.contextPath}/plugins/input-mask/jquery.inputmask.extensions.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datatables/jquery.dataTables.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/datatables/dataTables.bootstrap.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/chartjs/Chart.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/flot/jquery.flot.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/flot/jquery.flot.resize.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/flot/jquery.flot.pie.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/flot/jquery.flot.categories.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/ionslider/ion.rangeSlider.min.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-slider/bootstrap-slider.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-datetimepicker/bootstrap-datetimepicker.js"></script>
<script src="${pageContext.request.contextPath}/plugins/bootstrap-datetimepicker/locales/bootstrap-datetimepicker.zh-CN.js"></script>
<script>
    $(document).ready(function () {
        // 选择框
        $(".select2").select2();

        // WYSIHTML5编辑器
        $(".textarea").wysihtml5({
            locale: 'zh-CN'
        });
    });

    $(function () {
        var os_grade = $("#select_grade > option");
        $.each(os_grade,function(){
            var value_grade = $(this).html();
            var ans_grade = $("#gradeid").html()
            if(value_grade == ans_grade){
                $(this).attr("selected","selected");
            }
        })

        var os_professional = $("#select_professional > option");
        $.each(os_professional,function(){
            var value_professional = $(this).html();
            var ans_professional = $("#professionalid").html()
            if(value_professional == ans_professional){
                $(this).attr("selected","selected");
            }
        })

        var os_class = $("#select_class > option");
        $.each(os_class,function(){
            var value_class =$(this).html()
            var ans_class =$("#class_id").html()
            if(value_class == ans_class){
                $(this).attr("selected","selected");
            }
        })
    });


    // 设置激活菜单
    function setSidebarActive(tagUri) {
        var liObj = $("#" + tagUri);
        if (liObj.length > 0) {
            liObj.parent().parent().addClass("active");
            liObj.addClass("active");
        }
    }

    $(document).ready(function () {
        //Date picker
        $('#datepicker').datepicker({
            autoclose: true,
            language: 'zh-CN',
            format: 'yyyy/mm/dd'
        });
    });

    $(document)
        .ready(
            function () {

                // 激活导航位置
                setSidebarActive("admin-datalist");

                // 列表按钮
                $("#dataList td input[type='checkbox']")
                    .iCheck(
                        {
                            checkboxClass: 'icheckbox_square-blue',
                            increaseArea: '20%'
                        });
                // 全选操作
                $("#selall")
                    .click(
                        function () {
                            var clicks = $(this).is(
                                ':checked');
                            if (!clicks) {
                                $(
                                    "#dataList td input[type='checkbox']")
                                    .iCheck(
                                        "uncheck");
                            } else {
                                $(
                                    "#dataList td input[type='checkbox']")
                                    .iCheck("check");
                            }
                            $(this).data("clicks",
                                !clicks);
                        });
            });
</script>
</body>

</html>