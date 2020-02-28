package code_File.day04_转换流.demo01Writer;

import java.io.*;

public class demo01 {
    public static void main(String[] args) throws IOException {
        OutputStreamWriter osw_gbk = new OutputStreamWriter(new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\day04_转换流\\demo01Writer\\text_gbk.txt"),"gbk");
        OutputStreamWriter osw_utf8 = new OutputStreamWriter(new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\day04_转换流\\demo01Writer\\text_utf8.txt"));

        osw_gbk.write("你好");
        osw_gbk.close();

        osw_utf8.write("你好");
        osw_utf8.close();
        // 文件编码不一样  --》 文件大小不一样
    }
}
