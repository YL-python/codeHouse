package main.java.JDBCTemplCode;

import main.java.domain.Student;
import main.java.utils.JDBCUtils;
import org.testng.annotations.Test;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public class demo02 {
    // 获取对象
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    //1.修改1号数据的math 为10000
    @Test
    public void test1(){
        // 定义sql
        String sql = "update stdent01 set math = 10000 WHERE id=1";
        // 执行sql
        int count = template.update(sql);
        System.out.println(count);
    }

    //2.添加一条记录
    @Test
    public void test2(){
        // 定义sql
        String sql = "insert into stdent01 values(?,?,?,?,?,?,?)";
        // 执行sql
        int count = template.update(sql,6, "xiaoxiao", 55, "男", "俄罗斯", 77, 88);
        System.out.println(count);
    }

    //3.删除刚才添加的记录
    @Test
    public void test3(){
        // 定义sql
        String sql = "delete from stdent01 where id=?";
        // 执行sql
        int count = template.update(sql,6);
        System.out.println(count);
    }

    //4.查询id为1的记录，将其封装为Map集合
    @Test
    public void test4(){
        // 定义sql
//        String sql = "select * from stdent01 where id = ? or id = ?";
        String sql = "select * from stdent01 where id = ?";
        // 执行sql
        // 注意  查询的结果只能是一条数据
        Map<String, Object> map = template.queryForMap(sql, 1);
        System.out.println(map);
    }

    //5.查询所有记录，将其封装为List
    @Test
    public void test5(){
        // 定义sql
        String sql = "select * from stdent01";
        // 执行sql
        List<Map<String, Object>> list = template.queryForList(sql);
        System.out.println(list);
        System.out.println("===============");
        for (Map<String, Object> map : list) {
            System.out.println(map);
        }
    }

    //6.查询所有记录，将其封装为Student对象的List集合
    @Test
    public void test6(){
        // 定义sql
        String sql = "select * from stdent01";
        // 执行sql
        List<Student> stu = template.query(sql, new RowMapper<Student>() {
            @Override
            public Student mapRow(ResultSet resultSet, int i) throws SQLException {
                Student stu = new Student();
                stu.setId(resultSet.getInt("id"));
                stu.setName(resultSet.getString("name"));
                stu.setAge(resultSet.getInt("age"));
                stu.setSex(resultSet.getString("sex"));
                stu.setAdd(resultSet.getString("address"));
                stu.setMath(resultSet.getInt("math"));
                stu.setEng(resultSet.getInt("english"));
                return stu;
            }
        });
        for (Student student : stu) {
            System.out.println(student);
        }
    }

    //6.查询所有记录，将其封装为Student对象的List集合
    @Test
    public void test6_2(){
        // 定义sql
        String sql = "select * from stdent01";
        // 执行sql
        List<Student> stu = template.query(sql,new BeanPropertyRowMapper<Student>(Student.class));
        for (Student student : stu) {
            System.out.println(student);
        }
    }

    //7.查询总记录数
    @Test
    public void test7(){
        // 定义sql
        String sql = "select count(*) from stdent01";
        // 执行sql
        // 返回值是Long类型就要传 Long.class
        Long aLong = template.queryForObject(sql, Long.class);
        System.out.println(aLong);
    }
}
