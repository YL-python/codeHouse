package Exception_code.ThrowsCode;

import java.io.FileNotFoundException;
import java.io.IOException;

public class demo01 {
    public static void main(String[] args) throws Exception {
        String fileName = "C:\\\\b.txt";
        readFile(fileName);

    }

    // 定义方法找文件  “C:\\a.txt”
    public static void readFile(String fileName) throws Exception {
        if(! fileName.equals("C:\\\\a.txt")){
            throw new FileNotFoundException("文件名不对呀");
        }
        if(! fileName.endsWith(".txt")){
            throw new IOException("文件后缀名不对");
        }
        System.out.println("没问题，读取文件。。。");
    }
}
