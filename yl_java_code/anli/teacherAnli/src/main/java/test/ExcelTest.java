package main.java.test;

import main.java.domain.User;
import main.java.excel.ExcelReader;
import main.java.excel.ExcelWriter;
import org.junit.Test;

import javax.xml.crypto.Data;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class ExcelTest {
    @Test
    public void readexcelTest(){
        new ExcelReader().readexcel("D:\\Intellij_IDEA\\teacherAnli\\src\\teacher.xlsx");
    }

    @Test
    public void aaa(){
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月");
        String s = sdf.format(date);
        System.out.println(s);
    }

    @Test
    public void writeExcelTest(){
        User user = new User(1,"111","222","333",0);
        List<User> users = new ArrayList<>();
        users.add(user);
        new ExcelWriter().writeExcel("E:\\",users);
    }
}
