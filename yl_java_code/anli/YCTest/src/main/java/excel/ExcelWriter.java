package main.java.excel;

import main.java.domain.Student;
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
    public String writeExcel(String path, List<Student> students){
        Date date = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月");
        String s = sdf.format(date);
        String fileName = path+"\\"+s+"第一次考核考情况表.xlsx";
//        System.out.println(fileName);

        //第一步，创建一个workbook对应一个excel文件
        XSSFWorkbook workBook = new XSSFWorkbook();
        //第二部，在workbook中创建一个sheet对应excel中的sheet
        XSSFSheet sheet = workBook.createSheet("19新生考试情况");
        //第三部，在sheet表中添加表头第0行，老版本的poi对sheet的行列有限制
        XSSFRow row = sheet.createRow(0);
        XSSFCell cell = row.createCell(0);
        cell.setCellValue("id");
        cell = row.createCell(1);
        cell.setCellValue("姓名");
        cell = row.createCell(2);
        cell.setCellValue("班级");
        cell = row.createCell(3);
        cell.setCellValue("电话");
        cell = row.createCell(4);
        cell.setCellValue("考题");
        cell = row.createCell(5);
        cell.setCellValue("第一题");
        cell = row.createCell(6);
        cell.setCellValue("第二题");
        cell = row.createCell(7);
        cell.setCellValue("第三题");
        cell = row.createCell(8);
        cell.setCellValue("第四题");
        cell = row.createCell(9);
        cell.setCellValue("第五题");
        cell = row.createCell(10);
        cell.setCellValue("第六题");
        cell = row.createCell(11);
        cell.setCellValue("第七题");
        cell = row.createCell(12);
        cell.setCellValue("第八题");
        cell = row.createCell(13);
        cell.setCellValue("第九题");
        cell = row.createCell(14);
        cell.setCellValue("第十题");
        cell = row.createCell(15);


        for (int i = 0; i < students.size(); i++) {
            XSSFRow row1 = sheet.createRow(i + 1);
            Student student = students.get(i);
            //创建单元格设值
            row1.createCell(0).setCellValue(student.getId());
            row1.createCell(1).setCellValue(student.getName());
            row1.createCell(2).setCellValue(student.getClassroom());
            row1.createCell(3).setCellValue(student.getTel());
            row1.createCell(4).setCellValue(student.getTest());
            row1.createCell(5).setCellValue(student.getAns1());
            row1.createCell(6).setCellValue(student.getAns2());
            row1.createCell(7).setCellValue(student.getAns3());
            row1.createCell(8).setCellValue(student.getAns4());
            row1.createCell(9).setCellValue(student.getAns5());
            row1.createCell(10).setCellValue(student.getAns6());
            row1.createCell(11).setCellValue(student.getAns7());
            row1.createCell(12).setCellValue(student.getAns8());
            row1.createCell(13).setCellValue(student.getAns9());
            row1.createCell(14).setCellValue(student.getAns10());
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
