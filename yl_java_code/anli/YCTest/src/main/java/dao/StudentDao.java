package main.java.dao;

import main.java.domain.Student;
import main.java.utils.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class StudentDao {
    // 获取一个JDBCTemlate对象，是一个简化数据库操作的框架对象
    public static JdbcTemplate jdbcTemplate = new JdbcTemplate(JDBCUtils.getDataSource());

    // 添加学生信息
    public int addStudent(Student student){
        Integer max = jdbcTemplate.queryForObject("select max(id) from student", Integer.class);
        if(max == null){
            String sql = "insert into student(id,name,classroom,tel,test) values(?,?,?,?,?)";
            jdbcTemplate.update(sql,1,student.getName(),student.getClassroom(),student.getTel(),2);
            return 1;
        }else {
            String sql = "insert into student(id,name,classroom,tel,test) values(?,?,?,?,?)";
            jdbcTemplate.update(sql,max+1,student.getName(),student.getClassroom(),student.getTel(),(max+1)%3+1);
            return max+1;
        }
    }

    // 定义修改学生数据的方法
    public void upDataForAns(Student student){
        System.out.println(student);
        String sql = "update student set ans1=?,ans2=?,ans3=?,ans4=?,ans5=?,ans6=?,ans7=?,ans8=?,ans9=?,ans10=? where id=?";
        jdbcTemplate.update(sql,student.getAns1(),student.getAns2(),student.getAns3(),student.getAns4(),student.getAns5(),student.getAns6(),student.getAns7(),student.getAns8(),student.getAns9(),student.getAns10(),student.getId());
    }

    // 查找所有学生的方法
    public List<Student> findAll(){
        List<Student> students = jdbcTemplate.query("select * from student", new BeanPropertyRowMapper<Student>(Student.class));
        return students;
    }

}
