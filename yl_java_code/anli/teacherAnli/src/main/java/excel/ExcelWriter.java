package main.java.excel;

import main.java.domain.User;
import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

public class ExcelWriter {
    public String writeExcel(String path, List<User> users){
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月");
        String s = sdf.format(date);
        String fileName = path+"\\"+s+"老师监考情况表.xlsx";
//        System.out.println(fileName);

        //第一步，创建一个workbook对应一个excel文件
        XSSFWorkbook workBook = new XSSFWorkbook();
        //第二部，在workbook中创建一个sheet对应excel中的sheet
        XSSFSheet sheet = workBook.createSheet("老师监考情况");
        //第三部，在sheet表中添加表头第0行，老版本的poi对sheet的行列有限制
        XSSFRow row = sheet.createRow(0);
        XSSFCell cell = row.createCell(0);
        cell.setCellValue("id");
        cell = row.createCell(1);
        cell.setCellValue("name");
        cell = row.createCell(2);
        cell.setCellValue("tel");
        cell = row.createCell(3);
        cell.setCellValue("teacher_home");
        cell = row.createCell(4);
        cell.setCellValue("count");

        for (int i = 0; i < users.size(); i++) {
            XSSFRow row1 = sheet.createRow(i + 1);
            User user = users.get(i);
            //创建单元格设值
            row1.createCell(0).setCellValue(user.getId());
            row1.createCell(1).setCellValue(user.getName());
            row1.createCell(2).setCellValue(user.getTel());
            row1.createCell(3).setCellValue(user.getTeacher_home());
            row1.createCell(4).setCellValue(user.getCount());
        }

        //将文件保存到指定的位置
        try {
            FileOutputStream fos = new FileOutputStream(fileName);
            workBook.write(fos);
            System.out.println("写入成功");
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("文件写道本地时失败");
        }
        return fileName;
    }
}
