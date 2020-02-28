package code_File.day01_IO字节流.输入;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class copyFile {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IO字节流\\输入\\abc.txt");
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IO字节流\\输入\\def.txt",true);
        long s = System.currentTimeMillis();
//        int len = 0;
//        while ((len = fis.read()) != -1){
//            fos.write(len);
//        }

        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes)) != -1){
            fos.write(bytes,0,len);  // 用数组复制会快一点
        }

        fos.close();
        fis.close();
        long e = System.currentTimeMillis();
        System.out.println("复制文件用时"+(e-s)+"ms");
    }
}
