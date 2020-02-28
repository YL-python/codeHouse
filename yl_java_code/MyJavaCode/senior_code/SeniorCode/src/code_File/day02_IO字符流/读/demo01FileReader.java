package code_File.day02_IO字符流.读;

import java.io.FileReader;
import java.io.IOException;

public class demo01FileReader {
    public static void main(String[] args) throws IOException {
        FileReader fr = new FileReader("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IOString\\读\\abc.txt");

//        int len = 0;
//        while ((len = fr.read()) != -1){
//            System.out.print((char) len);
//        }
        char[] cs = new char[1024];
        int len = 0;
        while ((len = fr.read(cs)) != -1){
            System.out.println(new String(cs,0,len));
        }

        fr.close();
    }
}
