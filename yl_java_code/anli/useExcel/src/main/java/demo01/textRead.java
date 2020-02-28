package main.java.demo01;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.text.DecimalFormat;

public class textRead {
    public static void main(String[] args) throws IOException {
        String excelFilPath = "D:\\Intellij_IDEA\\useExcel\\src\\teacher.xlsx";  // 文件路径
        FileInputStream fis = new FileInputStream(excelFilPath);  // 变成流对象
        Workbook workbook = new XSSFWorkbook(fis);  // 吧流对象变成对应的  XSSFWorkbook  对象
        Sheet sheet = workbook.getSheetAt(0);  // 获取第一个工作表
        System.out.println(sheet);
        DecimalFormat format = new DecimalFormat("#");

        String cellValue;  // 吧每个单元格的值最终变成字符串处理
        // 遍历整个sheet
        for (int rowNum = 0; rowNum <= sheet.getLastRowNum(); rowNum++){  // 循环遍历表的每一行
            Row row = sheet.getRow(rowNum);
            System.out.println("第"+rowNum+"行的值：");
            for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++){  // 循环遍历每一行中的每一个单元格
                Cell cell = row.getCell(cellNum);  // 获取每一个单元格对象
                if(cell == null){
                    cellValue = "";
                    System.out.print(cellValue + "  ");
                }else{
                    int cellType = cell.getCellType();  // 获取单元格的类型
                    if(cellType == HSSFCell.CELL_TYPE_STRING){  // 字符串类型
                        cellValue = String.valueOf(cell.getStringCellValue());  // 不同类型获取值的方法不一样
                        System.out.print(cellValue + "  ");
                    }else if (cellType == HSSFCell.CELL_TYPE_NUMERIC){  // 数字类型


                        cellValue = String.valueOf(format.format(cell.getNumericCellValue())   );  // 不同类型获取值的方法不一样

                        System.out.print(cellValue + "  ");
                    }
                }
            }
            System.out.println();
        }

    }
}
