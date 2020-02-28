package code_File.code_Properties;

import java.util.Properties;
import java.util.Set;

public class demo01_基本使用 {
    public static void main(String[] args) {
        Properties prop = new Properties();
        prop.setProperty("杨龙","18");
        prop.setProperty("猪猪","18");
        prop.setProperty("yanglong","18");
        Set<String> set = prop.stringPropertyNames();
        for (String key : set) {
            String value = prop.getProperty(key);
            System.out.println(key+"="+value);
        }
    }
}
