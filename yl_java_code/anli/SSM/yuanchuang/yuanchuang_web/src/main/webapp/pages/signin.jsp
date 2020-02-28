<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" isELIgnored="false" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <!-- 页面meta -->
    <meta charset="utf-8">
    <title>猿创工作室</title>
    <!-- Tell the browser to be responsive to screen width -->
    <script>
        var t = null;
        t = setTimeout(time, 1000);
        function time() {
            clearTimeout(t);
            var dt = new Date();
            var yyyy = dt.getFullYear();
            var mm = dt.getMonth() + 1;
            var dd = dt.getDate();
            mm = mm >= 10 ? mm : "0" + mm;
            dd = dd >= 10 ? dd : "0" + dd;
            document.getElementById("qdtitle").innerHTML = yyyy + "年" + mm + "月" + dd + "日-签到";
            $("#todaydate").attr("value",yyyy+"/"+mm+"/"+dd);
            t = setTimeout(time, 1000); //设定定时器，循环运行
        }
    </script>
    <style>
        .qdsmilea{padding:3px;margin:auto;float:left;list-style:none;float:left}
        .qdsmilea li{float: left;padding:5px .4em;border:2px #fff solid;}
        .qdsmilea li img{margin-bottom:5px;}
        .qdsmilea li:hover{cursor:pointer;}
    </style>
    <script>
        function Icon_selected(sId) {
            $("#qdsmilea").css("border", "");
            $("#error_msg").html("");
            var oImg = document.getElementsByTagName('li');
            for (var i = 0; i < oImg.length; i++) {
                if (oImg[i].id == sId) {
                    var selectname = document.getElementById(oImg[i].id + "_s");
                    selectname.checked = true;
                    oImg[i].style. background = '#EFEFEF';
                } else {
                    oImg[i].style. background = '';
                }
            }
        }
    </script>
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

    <div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <section class="content-header">
            <h1>
                签到/打卡
                <small>页面</small>
            </h1>
        </section>

        <!-- Main content -->
        <section class="content">
            <div class="callout callout-info">
                <h4>奋斗吧!</h4>
                问道有先后，术业有专攻！加油！<span id="error_msg" style="font-size: 25px;color: red"></span>
            </div>
            <form action="${pageContext.request.contextPath}/qd/signin" method="post" onsubmit="return signinSub()">
            <div class="box-body">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 id="qdtitle" class="modal-title">yyyy年mm月dd日-签到</h4>
                    </div>
                    <div class="modal-body">
                        <div class="form-group">
                            <label class="control-label">今天心情怎么样:</label>
                                <div class="box-body table-responsive no-padding">
                                    <table class="table table-hover" width="100%" cellpadding="0" cellspacing="0" align="center">
                                        <tbody><tr>
                                                <ul class="qdsmilea" id="qdsmilea">
                                                    <input id="kx_s" type="radio" name="qdMood" value="开心" style="display:none" fwin="dsu_paulsign">
                                                    <li id="kx" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/kx.gif"><br>开心<br></center>
                                                    </li>
                                                    <input id="ng_s" type="radio" name="qdMood" value="难过" style="display:none" fwin="dsu_paulsign">
                                                    <li id="ng" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/ng.gif"><br>难过<br></center>
                                                    </li>
                                                    <input id="ym_s" type="radio" name="qdMood" value="郁闷" style="display:none" fwin="dsu_paulsign">
                                                    <li id="ym" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/ym.gif"><br>郁闷<br></center>
                                                    </li>
                                                    <input id="wl_s" type="radio" name="qdMood" value="无聊" style="display:none" fwin="dsu_paulsign">
                                                    <li id="wl" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/wl.gif"><br>无聊<br></center>
                                                    </li>
                                                    <input id="ch_s" type="radio" name="qdMood" value="擦汗" style="display:none" fwin="dsu_paulsign">
                                                    <li id="ch" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/ch.gif"><br>擦汗<br></center>
                                                    </li>
                                                    <input id="nu_s" type="radio" name="qdMood" value="怒" style="display:none" fwin="dsu_paulsign">
                                                    <li id="nu" onclick="Icon_selected(this.id)" fwin="dsu_paulsign" style=""><center>
                                                        <img src="${pageContext.request.contextPath}/images/nu.gif"><br>怒<br></center>
                                                    </li>
                                                    <input id="fd_s" type="radio" name="qdMood" value="奋斗" style="display:none" fwin="dsu_paulsign">
                                                    <li id="fd" onclick="Icon_selected(this.id)" fwin="dsu_paulsign"><center>
                                                        <img src="${pageContext.request.contextPath}/images/fd.gif"><br>奋斗<br></center>
                                                    </li>
                                                    <input id="yl_s" type="radio" name="qdMood" value="慵懒" style="display:none" fwin="dsu_paulsign">
                                                    <li id="yl" onclick="Icon_selected(this.id)" fwin="dsu_paulsign"><center>
                                                        <img src="${pageContext.request.contextPath}/images/yl.gif"><br>慵懒<br></center>
                                                    </li>
                                                    <input id="shuai_s" type="radio" name="qdMood" value="衰" style="display:none" fwin="dsu_paulsign">
                                                    <li id="shuai" onclick="Icon_selected(this.id)" fwin="dsu_paulsign"><center>
                                                        <img src="${pageContext.request.contextPath}/images/shuai.gif"><br>衰<br></center>
                                                    </li>
                                                </ul>
                                        </tr>
                                        </tbody>
                                    </table>
                                <!-- /.box-body -->
                            </div>
                        </div>
                        <div class="form-group">
                            <label>今天的学习时间:</label>
                            <input id="todaydate" type="hidden" name="qdDateStr" value="">
                            <div class="tab-pane active" id="tab-select">
                                <div class="row data-type">
                                    <div class="col-md-2 title">开始时间</div>
                                    <div class="col-md-2 data">
                                        <select class="form-control" id="qdStartTimehh" name="qdStartTimehh">
                                            <option value="08">8点</option>
                                            <option value="09">9点</option>
                                            <option value="10">10点</option>
                                            <option value="11">11点</option>
                                            <option value="12">12点</option>
                                            <option value="13">13点</option>
                                            <option value="14">14点</option>
                                            <option value="15">15点</option>
                                            <option value="16">16点</option>
                                            <option value="17">17点</option>
                                            <option value="18">18点</option>
                                            <option value="19">19点</option>
                                            <option value="20">20点</option>
                                            <option value="21">21点</option>
                                            <option value="22">22点</option>
                                            <option value="23">23点</option>
                                            <option value="24">24点</option>
                                            <option value="01">1点</option>
                                            <option value="02">2点</option>
                                            <option value="03">3点</option>
                                            <option value="04">4点</option>
                                            <option value="05">5点</option>
                                            <option value="06">6点</option>
                                            <option value="07">7点</option>
                                        </select>
                                    </div>
                                    <div class="col-md-2 data">
                                        <select class="form-control" id="qdStartTimemm" name="qdStartTimemm">
                                            <option value="00">00分</option>
                                            <option value="05">05分</option>
                                            <option value="10">10分</option>
                                            <option value="15">15分</option>
                                            <option value="20">20分</option>
                                            <option value="25">25分</option>
                                            <option value="30">30分</option>
                                            <option value="35">35分</option>
                                            <option value="40">40分</option>
                                            <option value="45">45分</option>
                                            <option value="50">50分</option>
                                            <option value="55">55分</option>
                                        </select>
                                    </div>

                                    <div class="col-md-2 title">结束时间</div>
                                    <div class="col-md-2 data">
                                        <select class="form-control" id="qdEndTimehh" name="qdEndTimehh">
                                            <option value="08">8点</option>
                                            <option value="09">9点</option>
                                            <option value="10">10点</option>
                                            <option value="11">11点</option>
                                            <option value="12">12点</option>
                                            <option value="13">13点</option>
                                            <option value="14">14点</option>
                                            <option value="15">15点</option>
                                            <option value="16">16点</option>
                                            <option value="17">17点</option>
                                            <option value="18">18点</option>
                                            <option value="19">19点</option>
                                            <option value="20">20点</option>
                                            <option value="21">21点</option>
                                            <option value="22">22点</option>
                                            <option value="23">23点</option>
                                            <option value="24">24点</option>
                                            <option value="01">1点</option>
                                            <option value="02">2点</option>
                                            <option value="03">3点</option>
                                            <option value="04">4点</option>
                                            <option value="05">5点</option>
                                            <option value="06">6点</option>
                                            <option value="07">7点</option>
                                        </select>
                                    </div>
                                    <div class="col-md-2 data">
                                        <select class="form-control" id="qdEndTimemm" name="qdEndTimemm">
                                            <option value="00">00分</option>
                                            <option value="05">05分</option>
                                            <option value="10">10分</option>
                                            <option value="15">15分</option>
                                            <option value="20">20分</option>
                                            <option value="25">25分</option>
                                            <option value="30">30分</option>
                                            <option value="35">35分</option>
                                            <option value="40">40分</option>
                                            <option value="45">45分</option>
                                            <option value="50">50分</option>
                                            <option value="55">55分</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label>今天学到了什么:</label>
                            <textarea name="qdTodayContent" id="qdTodayContent" class="form-control" rows="3" placeholder="Enter ..."></textarea>
                        </div>
                        <div class="form-group">
                            <label>明天打算学什么:</label>
                            <textarea name="qdTomorrowContent" id="qdTomorrowContent" class="form-control" rows="3" placeholder="Enter ..."></textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default pull-left"
                                data-dismiss="modal" onclick="history.back(-1);">返回</button>
                        <button type="submit" class="btn btn-primary">发表</button>
                    </div>
                </div>
                <!-- /.modal-content -->
            </div>
            <!-- /.modal-dialog -->
            </form>


        </section>
        <!-- /.content -->
    </div>

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

    function checkqdTodayContent() {
        // 检查心情有没有被选择
        var qdmood =  $(":radio:checked").length
        if(qdmood == 0){
            $("#qdsmilea").css("border", "2px solid red");
            $("#error_msg").html("请选择心情");
            return false;
        }
        // 检查时间
        var starthh = $("#qdStartTimehh").val();
        var startmm = $("#qdStartTimemm").val();
        var endhh = $("#qdEndTimehh").val();
        var endmm = $("#qdEndTimemm").val();
        var ans = endhh*3600+endmm*60-starthh*3600-startmm*60;
        if(ans <= 0){
            $("#tab-select").css("border", "2px solid red");
            $("#error_msg").html("时间有误");
            return false;
        }
        // 检查今天输入的内容
        var qdTodayContent_len = $("#qdTodayContent").val().length;
        if(qdTodayContent_len < 30 || qdTomorrowContent_len > 300){
            $("#qdTodayContent").css("border", "2px solid red");
            $("#error_msg").html("今天学习内容需要求字符长度在30-300之间");
            return false;
        }else{
            $("#qdTodayContent").css("border", "");
            $("#error_msg").html("");
            return true;
        }
    }

    function checkqdTomorrowContent() {
        // 检查明天输入的内容
        var qdTomorrowContent_len = $("#qdTomorrowContent").val().length;
        if(qdTomorrowContent_len < 20 || qdTomorrowContent_len > 300){
            $("#qdTomorrowContent").css("border", "2px solid red");
            $("#error_msg").html("明天学习内容要求字符长度在20-300之间");
            return false;
        }else{
            $("#qdTomorrowContent").css("border", "");
            $("#error_msg").html("");
            return true;
        }
    }

    function checktab_select() {
        var starthh = $("#qdStartTimehh").val();
        var startmm = $("#qdStartTimemm").val();
        var endhh = $("#qdEndTimehh").val();
        var endmm = $("#qdEndTimemm").val();
        var ans = endhh*3600+endmm*60-starthh*3600-startmm*60;
        if(ans <= 0){
            $("#tab-select").css("border", "2px solid red");
            $("#error_msg").html("时间有误");
        }else{
            $("#tab-select").css("border", "");
            $("#error_msg").html("");
        }

    }
    function signinSub(){
        if(checkqdTodayContent() && checkqdTomorrowContent()){
            return true;
        }else{
            alert("表单没有全部填写正确哦");
            return false;
        }
    }

    $(function () {
        $("#qdTodayContent").blur(checkqdTodayContent);
        $("#qdTomorrowContent").blur(checkqdTomorrowContent);
        $("#tab-select").click(checktab_select);
    });
</script>
</body>

</html>