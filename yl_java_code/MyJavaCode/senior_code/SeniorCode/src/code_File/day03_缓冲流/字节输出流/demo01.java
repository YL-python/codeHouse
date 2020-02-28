package code_File.day03_缓冲流.字节输出流;

import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class demo01 {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\字节输出流\\OutPutStream.txt");
        BufferedOutputStream bfos = new BufferedOutputStream(fos);
        bfos.write("abc".getBytes());
        bfos.flush();
        bfos.close();
    }
}
