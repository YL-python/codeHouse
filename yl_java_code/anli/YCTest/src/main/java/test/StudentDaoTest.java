package main.java.test;

import main.java.dao.StudentDao;
import main.java.domain.Student;
import main.java.excel.ExcelWriter;
import org.junit.Test;

import java.util.List;

public class StudentDaoTest {
    @Test
    public void addStudentTest(){
        Student student = new Student(1, "www", "dashuju ", "13131",1,null,null,null,null,null,null,null,null,null,null);
        new StudentDao().addStudent(student);
    }

    @Test
    public void upDataForAnsTest(){
        Student student = new Student(10, null, null, null,2,"D","D","D","D","5555","666","777","888","999","10101");
        new StudentDao().upDataForAns(student);
    }

    @Test
    public void test(){
        ExcelWriter excelWriter = new ExcelWriter();
        List<Student> studentList = new StudentDao().findAll();
        excelWriter.writeExcel("D:",studentList);
    }
}
