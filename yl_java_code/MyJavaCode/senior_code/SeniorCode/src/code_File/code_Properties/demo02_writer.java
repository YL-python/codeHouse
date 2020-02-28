package code_File.code_Properties;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

public class demo02_writer {
    public static void main(String[] args) throws IOException {
        Properties prop = new Properties();
        prop.setProperty("杨龙","18");
        prop.setProperty("猪猪","18");
        prop.setProperty("yanglong","18");
        prop.store(new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\code_Properties\\text.txt"),"");
    }
}
