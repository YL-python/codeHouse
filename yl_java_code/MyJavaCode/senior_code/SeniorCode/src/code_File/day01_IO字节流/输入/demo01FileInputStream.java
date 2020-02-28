package code_File.day01_IO字节流.输入;

import java.io.FileInputStream;
import java.io.IOException;

public class demo01FileInputStream {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IO字节流\\输出\\text.txt");
//        int read = fis.read();
//        System.out.println(read);
//        read = fis.read();
//        System.out.println(read);
//        read = fis.read();
//        System.out.println(read);
//        read = fis.read();
//        System.out.println(read);
//        read = fis.read();
//        System.out.println(read);

        int len = 0 ;
        while ((len = fis.read()) != -1){
            System.out.println((char)len);
        }

        fis.close();
    }
}
