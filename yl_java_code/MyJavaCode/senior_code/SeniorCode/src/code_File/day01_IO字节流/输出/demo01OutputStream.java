package code_File.day01_IO字节流.输出;

import java.io.FileOutputStream;
import java.io.IOException;

public class demo01OutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\" +
                "SeniorCode\\src\\code_File\\IO字节流\\输出\\text.txt");
        fos.write(97);
        for(int i = 0 ;i<=100;i++){
            fos.write(i);
        }
        fos.close();
    }
}
