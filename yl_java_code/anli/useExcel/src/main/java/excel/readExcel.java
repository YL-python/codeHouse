package main.java.excel;

import main.java.demain.User;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

public class readExcel {
    public static String getCellValue(Cell cell){
        DecimalFormat format = new DecimalFormat("#");  // 吧电话号码变成对应数字的方法
        switch (cell.getCellType()){
            case HSSFCell.CELL_TYPE_STRING:
                return cell.getStringCellValue();
            case HSSFCell.CELL_TYPE_NUMERIC:
                return format.format(cell.getNumericCellValue());
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        String excelFilPath ="D:\\Intellij_IDEA\\useExcel\\src\\teacher.xlsx";  // 文件路径
        List<User> userList = new ArrayList<>();

        FileInputStream fis = new FileInputStream(excelFilPath);  // 变成流对象
        Workbook workbook = new XSSFWorkbook(fis);  // 吧流对象变成对应的  XSSFWorkbook  对象
        Sheet sheet = workbook.getSheetAt(0);  // 获取第一个工作表

        for (int rowNum = 1; rowNum <= sheet.getLastRowNum(); rowNum++) {
            Row row = sheet.getRow(rowNum);
            User user = new User();
            String cellValue;
            for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
                Cell cell = row.getCell(cellNum);
                if(cell == null){
                    cellValue = "";
                }else {
                    switch (cellNum){
                        case 0:
                            cellValue = getCellValue(cell);
                            user.setId(Integer.parseInt(cellValue));
                            break;
                        case 1:
                            cellValue = getCellValue(cell);
                            user.setName(cellValue);
                            break;
                        case 2:
                            cellValue = getCellValue(cell);
                            user.setTel(cellValue);
                            break;
                        case 3:
                            cellValue = getCellValue(cell);
                            user.setTeacher_home(cellValue);
                            break;
                        case 4:
                            cellValue = getCellValue(cell);
                            user.setCount(Integer.parseInt(cellValue));
                            break;
                    }
                }
            }
            userList.add(user);
            System.out.println(user);
        }

    }
}
