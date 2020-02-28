package code_File.day02_IO字符流.code_Writer;

import java.io.FileWriter;
import java.io.IOException;

public class demo02 {
    public static void main(String[] args) throws IOException {
        FileWriter fw = null;  // 提高变量作用域
        try{
            fw = new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\IOString\\code_Writer\\text.txt",true);
            fw.write("as你好\nnihao ");
        }catch (IOException e){// 避免文件路径异常
            System.out.println(e);
        }finally {
            if(fw!=null){//避免空指针异常
                try{
                    fw.close();
                }catch (IOException e){
                    e.fillInStackTrace();
                }
            }
        }
    }
}
