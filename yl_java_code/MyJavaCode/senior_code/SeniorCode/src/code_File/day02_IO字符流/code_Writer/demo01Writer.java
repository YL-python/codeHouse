package code_File.day02_IO字符流.code_Writer;

import java.io.FileWriter;
import java.io.IOException;

public class demo01Writer {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IOString\\code_Writer\\text.txt",true);
        fw.write("as你好\nnihao ");
        fw.flush();
        fw.close();
}
}
