package code_File.day03_缓冲流.字节输入流;

import java.io.*;

public class demo01 {
    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\字节输入流\\InPutStream.txt");
        BufferedInputStream bfis = new BufferedInputStream(fis);

//        int len = 0;
//        while ((len=bfis.read()) != -1){
//            System.out.println((char) len);
//        }

        byte[] bytes = new byte[1024];
        int len = 0;
        while ((len=bfis.read(bytes)) != -1){
            System.out.println(new String(bytes, 0, len));
        }

        bfis.close();
    }
}
