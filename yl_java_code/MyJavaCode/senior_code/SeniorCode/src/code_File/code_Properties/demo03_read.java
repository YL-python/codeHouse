package code_File.code_Properties;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;
import java.util.Set;

public class demo03_read {
    public static void main(String[] args) throws IOException {
        Properties prop = new Properties();
        prop.load(new FileReader("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\code_Properties\\text.txt"));
        Set<String> set = prop.stringPropertyNames();
        for (String key : set) {
            String value = prop.getProperty(key);
            System.out.println(key+"="+value);
        }
    }
}
