package code_File.day03_缓冲流.字符输入流;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class demo01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\字符输入流\\abc.txt"));
        String line = "";
//        while ((line = br.readLine())!=null){
//            System.out.println(line);
//        }
        char[] cs = new char[1024];
        int len = 0;
        while ((len = br.read(cs)) != -1){
            System.out.println(new String(cs,0,len));
        }
        br.close();
    }
}
