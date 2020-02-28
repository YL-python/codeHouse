package main.java.demo01;

import main.java.demain.Test;
import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class testWriter2 {
    // 产生要储存的集合
    protected static List<Test> getUsers() {
        List<Test> users = new ArrayList<>();
        Test user1 = new Test("admin", "123456");
        Test user2 = new Test("staff1", "141242");
        Test user3 = new Test("staff2", "386002");
        users.add(user1);
        users.add(user2);
        users.add(user3);
        return users;
    }

    public static void main(String[] args) {
        //第一步，创建一个workbook对应一个excel文件
        XSSFWorkbook workBook = new XSSFWorkbook();
        //第二部，在workbook中创建一个sheet对应excel中的sheet
        XSSFSheet sheet = workBook.createSheet("用户数据");
        //第三部，在sheet表中添加表头第0行，老版本的poi对sheet的行列有限制
        XSSFRow row = sheet.createRow(0);

        XSSFCell cell = row.createCell(0);
        cell.setCellValue("用户名");
        cell = row.createCell(1);
        cell.setCellValue("密码");

        //第五步，写入实体数据，实际应用中这些数据从数据库得到,对象封装数据，集合包对象。对象的属性值对应表的每行的值
        List<Test> users = getUsers();
        for (int i = 0; i < users.size(); i++) {
            XSSFRow row1 = sheet.createRow(i + 1);
            Test user = users.get(i);
            //创建单元格设值
            row1.createCell(0).setCellValue(user.getUsername());
            row1.createCell(1).setCellValue(user.getPassword());
        }
        //将文件保存到指定的位置
        try {
            FileOutputStream fos = new FileOutputStream("E:\\user2.xlsx");
            workBook.write(fos);
            System.out.println("写入成功");
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
