package code_File.day02_IO字符流.code_Writer;

import java.io.FileWriter;
import java.io.IOException;

public class demo03 {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IOString\\code_Writer\\text.txt",true);
        try(fw){
            fw.write("as你好\nnihao ");
        }catch (IOException e){
            System.out.println(e);
        }
    }
}
