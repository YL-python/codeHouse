<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" isELIgnored="false" %>
<%@ taglib prefix="security" uri="http://www.springframework.org/security/tags" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <!-- 页面meta -->
    <meta charset="utf-8">

    <title>猿创工作室</title>
    <script>
        var t = null;
        t = setTimeout(time, 1000);
        function time() {
            clearTimeout(t);
            var dt = new Date();
            var h = dt.getHours();
            var m = dt.getMinutes();
            var s = dt.getSeconds();
            s = s >= 10 ? s : "0" + s;
            h = h >= 10 ? h : "0" + h;
            m = m >= 10 ? m : "0" + m;
            var yyyy = dt.getFullYear();
            var mm = dt.getMonth() + 1;
            var dd = dt.getDate();
            // 北京时间<br>2010年12月31日
            document.getElementById("showTime1").innerHTML = "北京时间<br>" + yyyy + "年" + mm + "月" + dd + "日";
            document.getElementById("showTime2").innerHTML = h + ":" + m + ":" + s;
            t = setTimeout(time, 1000); //设定定时器，循环运行
        }
    </script>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/font-awesome/css/font-awesome.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/ionicons/css/ionicons.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/iCheck/square/blue.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/morris/morris.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/jvectormap/jquery-jvectormap-1.2.2.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/datepicker/datepicker3.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/daterangepicker/daterangepicker.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/datatables/dataTables.bootstrap.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/treeTable/jquery.treetable.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/treeTable/jquery.treetable.theme.default.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/select2/select2.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/colorpicker/bootstrap-colorpicker.min.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-markdown/css/bootstrap-markdown.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/adminLTE/css/AdminLTE.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/adminLTE/css/skins/_all-skins.min.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/css/style.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/ionslider/ion.rangeSlider.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/ionslider/ion.rangeSlider.skinNice.css">
    <link rel="stylesheet" href="${pageContext.request.contextPath}/plugins/bootstrap-slider/slider.css">
    <link rel="stylesheet"
          href="${pageContext.request.contextPath}/plugins/bootstrap-datetimepicker/bootstrap-datetimepicker.css">
    <style type="text/css">
        .setbg {
            background: url("${pageContext.request.contextPath}/images/yuanchuang.jpg");
            background-attachment: fixed;
            background-size: cover;
        }
    </style>
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


    <div class="content-wrapper setbg">
        <section class="content">
            <div class="row">
                <div class="col-lg-4 col-xs-6">
                    <!-- small box -->
                    <div class="small-box bg-aqua">
                        <div class="inner">
                            <p id="showTime1"></p>
                            <h3 id="showTime2"></h3>

                        </div>
                        <div class="icon">
                            <i class="fa fa-tv"></i>
                        </div>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-4 col-xs-6">
                    <!-- small box -->
                    <div class="small-box bg-green">
                        <div class="inner">
                            <p>打卡时间</p>
                            <h3>排行榜</h3>
                        </div>
                        <div class="icon">
                            <i class="ion ion-stats-bars"></i>
                        </div>
                        <a href="#" class="small-box-footer">
                            点击查看 <i class="fa fa-arrow-circle-right"></i>
                        </a>
                    </div>

                </div>
                <!-- ./col -->
                <div class="col-lg-4 col-xs-6">
                    <div class="box box-warning">
                        <div class="box-header with-border">
                            <h3 class="box-title">其他功能</h3>

                            <div class="box-tools pull-right">
                                <button type="button" class="btn btn-box-tool" data-widget="collapse">
                                    <i class="fa fa-minus"></i>
                                </button>
                            </div>
                            <!-- /.box-tools -->
                        </div>
                        <!-- /.box-header -->
                        <div class="box-body">
                            <div class="box-body">
                                研发中...
                                <br><br>
                            </div>
                            <div class="overlay">
                                <i class="fa fa-refresh fa-spin"></i>
                            </div>
                        </div>
                    </div>
                </div>
                <!--/.direct-chat -->

                <div class="row">
                    <div class="col-lg-6 col-xs-12">
                        <!-- DIRECT CHAT SUCCESS -->
                        <div class="box box-success direct-chat direct-chat-success">
                            <div class="box-header with-border">
                                <h3 class="box-title">版本介绍</h3>
                                <div class="box-tools pull-right">
                                    <button type="button" class="btn btn-box-tool" data-widget="collapse"><i
                                            class="fa fa-minus"></i>
                                    </button>
                                    <button type="button" class="btn btn-box-tool" data-widget="remove"><i
                                            class="fa fa-times"></i></button>
                                </div>
                            </div>
                            <!-- /.box-header -->
                            <div class="box-body">
                                <!-- Conversations are loaded here -->
                                <div class="direct-chat-messages">
                                    <div class="direct-chat-msg right">
                                        <div class="direct-chat-info clearfix">
                                            <span class="direct-chat-name pull-right">
                                                <security:authorize access="isAuthenticated()">
                                                    <security:authentication property="principal.username"/>
                                                </security:authorize>
                                            </span>
                                            <span class="direct-chat-timestamp pull-left">2020年2月3日13:00</span>
                                        </div>
                                        <img class="direct-chat-img"
                                             src="${pageContext.request.contextPath}/images/user2-160x160.jpg"
                                             alt="Message User Image">
                                        <div class="direct-chat-text">
                                            这个系统有哪些功能呢？
                                        </div>
                                    </div>

                                    <div class="direct-chat-msg">
                                        <div class="direct-chat-info clearfix">
                                            <span class="direct-chat-name pull-left">猿创</span>
                                            <span class="direct-chat-timestamp pull-right">2020年2月3日13:01</span>
                                        </div>
                                        <!-- /.direct-chat-info -->
                                        <img class="direct-chat-img"
                                             src="${pageContext.request.contextPath}/images/yuanchuang-160x160.jpg"
                                             alt="Message User Image">
                                        <!-- /.direct-chat-img -->
                                        <div class="direct-chat-text" id="nowVersion">
                                            加载中...
                                        </div>
                                    </div>

                                    <div class="direct-chat-msg right">
                                        <div class="direct-chat-info clearfix">
                                            <span class="direct-chat-name pull-right">
                                                <security:authorize
                                                        access="isAuthenticated()">
                                                    <security:authentication property="principal.username"/>
                                                </security:authorize></span>
                                            <span class="direct-chat-timestamp pull-left">2020年2月3日13:00</span>
                                        </div>
                                        <img class="direct-chat-img"
                                             src="${pageContext.request.contextPath}/images/user2-160x160.jpg"
                                             alt="Message User Image">
                                        <div class="direct-chat-text">
                                            之后会增加哪些功能呢？
                                        </div>
                                    </div>

                                    <div class="direct-chat-msg">
                                        <div class="direct-chat-info clearfix">
                                            <span class="direct-chat-name pull-left">猿创</span>
                                            <span class="direct-chat-timestamp pull-right">2020年2月3日13:01</span>
                                        </div>
                                        <!-- /.direct-chat-info -->
                                        <img class="direct-chat-img"
                                             src="${pageContext.request.contextPath}/images/yuanchuang-160x160.jpg"
                                             alt="Message User Image">
                                        <!-- /.direct-chat-img -->
                                        <div class="direct-chat-text" id="nextVersion">
                                            加载中...
                                        </div>
                                    </div>

                                    <div class="direct-chat-msg right">
                                        <div class="direct-chat-info clearfix">
                                            <span class="direct-chat-name pull-right">
                                                <security:authorize access="isAuthenticated()">
                                                    <security:authentication property="principal.username"/>
                                                </security:authorize>
                                            </span>
                                            <span class="direct-chat-timestamp pull-left">2020年2月3日13:00</span>
                                        </div>
                                        <img class="direct-chat-img"
                                             src="${pageContext.request.contextPath}/images/user2-160x160.jpg"
                                             alt="Message User Image">
                                        <div class="direct-chat-text">
                                            太棒了！
                                        </div>
                                    </div>

                                </div>
                            </div>
                            <!-- /.box-body -->
                            <div class="box-footer">
                                <div class="input-group">
                                    <input type="text" name="message" placeholder="说点什么..."
                                           class="form-control">
                                    <span class="input-group-btn">
                        <button class="btn btn-success btn-flat">发送</button>
                      </span>
                                </div>
                            </div>
                            <!-- /.box-footer-->
                        </div>
                    </div>
                </div>
            </div>
        </section>


        <%--			${sessionScope}<br><br><br><br><br>--%>
        <%--			${requestScope}--%>

    </div>
    <!-- 内容区域 /-->

    <!-- 底部导航 -->
    <footer class="main-footer">
        <div class="pull-right hidden-xs">
            <b>Version</b> 1.0.1
        </div>
        <strong>Copyright &copy; 2014-2020 <a
                href="#">猿创工作室.版权所有</a>.
        </strong> PowerBy:18-大数据-杨龙.
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

    // 设置激活菜单
    function setSidebarActive(tagUri) {
        var liObj = $("#" + tagUri);
        if (liObj.length > 0) {
            liObj.parent().parent().addClass("active");
            liObj.addClass("active");
        }
    }
    $(document).ready(function () {
        // 激活导航位置
        setSidebarActive("admin-index");
    });
    $(function () {
        // 当前版本介绍
        $("#nowVersion").html("0:注册功能<br>1:个人信息管理<br>2:当日签到<br>3:用户的所有签到信息查询");
        // 后期版本开发的功能
        $("#nextVersion").html("1:签到时间排行榜功能<br>2:签到信息的搜索功能<br>3:个别页面的美化");
    })

</script>

</body>

</html>