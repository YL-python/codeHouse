package code_File.day03_缓冲流.字符输出流;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class demo01 {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\字符输出流\\abc.txt"));
        bw.write("你好你好111");
        bw.newLine();
        bw.newLine();
        bw.write("你好你好222");
        bw.flush();
        bw.close();
    }
}
