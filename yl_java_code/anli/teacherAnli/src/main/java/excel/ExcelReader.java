package main.java.excel;

import main.java.domain.User;
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

public class ExcelReader {
    public List<User> readexcel(String path){
        List<User> userList = new ArrayList<>();
        Workbook workbook = null;
        try {
            workbook = new XSSFWorkbook(new FileInputStream(path));
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("读取文件的时候出现了一点小意外  (￣_￣|||) ");
        }
        Sheet sheet = workbook.getSheetAt(0);  // 获取第一个工作表
        for (int rowNum = 1; rowNum <= sheet.getLastRowNum(); rowNum++){  // 读取每一行
            User user = new User();
            Row row = sheet.getRow(rowNum);
            for (int cellNum = 0; cellNum < row.getLastCellNum(); cellNum++) {
                Cell cell = row.getCell(cellNum);
                setUserValue(user,cell,cellNum);
            }
            userList.add(user);
        }
        return userList;
    }

    private void setUserValue(User user , Cell cell, int num){
        switch(num){
            case 0: user.setId(Integer.parseInt(getCellValue(cell)));
                break;
            case 1:user.setName(getCellValue(cell));
                break;
            case 2:user.setTel(getCellValue(cell));
                break;
            case 3:user.setTeacher_home(getCellValue(cell));
                break;
            case 4:user.setCount(Integer.parseInt(getCellValue(cell)));
                break;
        }
    }
    private String getCellValue(Cell cell ){
        DecimalFormat format = new DecimalFormat("#");
        if(cell == null){
            return "";
        }else {
            switch (cell.getCellType()){
                case HSSFCell.CELL_TYPE_STRING:
                    return cell.getStringCellValue();
                case HSSFCell.CELL_TYPE_NUMERIC:
                    return format.format(cell.getNumericCellValue());
            }
        }
        return "";
    }
}

