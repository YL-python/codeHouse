package code_File.day04_转换流.demo02Reader;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

public class demo01 {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\day04_转换流\\demo01Writer\\text_gbk.txt"));
        // 用 utf-8读gbk格式文件
        int len ;
        while ((len = isr.read()) != -1){
            System.out.println((char) len);
        }
        isr.close();
    }
}
