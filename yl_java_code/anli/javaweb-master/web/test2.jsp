<%@ page import="java.sql.Statement" %>
<%@ page import="java.sql.DriverManager" %>
<%@ page import="java.sql.Connection" %>
<%@ page import="java.sql.ResultSet" %><%--
  Created by IntelliJ IDEA.
  User: hp
  Date: 2018/7/8
  Time: 20:05
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    //注册数据库驱动
    Class.forName("com.mysql.jdbc.Driver");
//获取数据库连接
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/web?user=root&password=961008&useSSL=false&serverTimezone=UTC");
//创建statement
    Statement stmt = conn.createStatement();
//执行查询

    String sql1 = "select * from coursetable where xingqi=1 AND jie=1";
    ResultSet rs1 = stmt.executeQuery(sql1);
    String sql2 = "select * from coursetable where xingqi=2 AND jie=1";
    ResultSet rs2 = stmt.executeQuery(sql2);
    String sql3 = "select * from coursetable where xingqi=3 AND jie=1";
    ResultSet rs3 = stmt.executeQuery(sql3);
    String sql4 = "select * from coursetable where xingqi=4 AND jie=1";
    ResultSet rs4 = stmt.executeQuery(sql4);
    String sql5 = "select * from coursetable where xingqi=5 AND jie=1";
    ResultSet rs5 = stmt.executeQuery(sql5);

    String sql6 = "select * from coursetable where xingqi=1 AND jie=2";
    ResultSet rs6 = stmt.executeQuery(sql6);
    String sql7 = "select * from coursetable where xingqi=2 AND jie=2";
    ResultSet rs7 = stmt.executeQuery(sql7);
    String sql8 = "select * from coursetable where xingqi=3 AND jie=2";
    ResultSet rs8 = stmt.executeQuery(sql8);
    String sql9 = "select * from coursetable where xingqi=4 AND jie=2";
    ResultSet rs9 = stmt.executeQuery(sql9);
    String sql10 = "select * from coursetable where xingqi=5 AND jie=2";
    ResultSet rs10 = stmt.executeQuery(sql10);

    String sql11 = "select * from coursetable where xingqi=1 AND jie=3";
    ResultSet rs11 = stmt.executeQuery(sql11);
    String sql12 = "select * from coursetable where xingqi=2 AND jie=3";
    ResultSet rs12 = stmt.executeQuery(sql12);
    String sql13 = "select * from coursetable where xingqi=3 AND jie=3";
    ResultSet rs13 = stmt.executeQuery(sql13);
    String sql14 = "select * from coursetable where xingqi=4 AND jie=3";
    ResultSet rs14 = stmt.executeQuery(sql14);
    String sql15 = "select * from coursetable where xingqi=5 AND jie=3";
    ResultSet rs115 = stmt.executeQuery(sql15);

    String sql16 = "select * from coursetable where xingqi=1 AND jie=4";
    ResultSet rs16 = stmt.executeQuery(sql16);
    String sql17 = "select * from coursetable where xingqi=2 AND jie=4";
    ResultSet rs17 = stmt.executeQuery(sql17);
    String sql18 = "select * from coursetable where xingqi=3 AND jie=4";
    ResultSet rs18 = stmt.executeQuery(sql18);
    String sql19 = "select * from coursetable where xingqi=4 AND jie=4";
    ResultSet rs19 = stmt.executeQuery(sql19);
    String sql20 = "select * from coursetable where xingqi=5 AND jie=4";
    ResultSet rs120 = stmt.executeQuery(sql20);


%>
<form>
    <table>
<tr>
    <td>
        <%=rs1.getString("name")%>
    </td>


</tr>
    </table>
</form>
</body>
</html>
