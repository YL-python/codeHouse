package code_File.文件重排序;

import java.io.*;
import java.util.HashMap;

public class FileSort {
    public static void main(String[] args) throws IOException {
        // 创建字典存放数据，按照key来排序
        HashMap<String,String> map = new HashMap<>();
        BufferedReader br = new BufferedReader(new FileReader("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\文件重排序\\text.txt"));
        BufferedWriter bw = new BufferedWriter(new FileWriter("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\文件重排序\\out.txt"));
        // 读取文本并存到字典里面
        String line;
        while ((line = br.readLine()) != null){
            String[] arr = line.split("\\.");
            map.put(arr[0],arr[1]);
        }
        // 遍历字典存贮数据
        for(String key : map.keySet()){
            String valur = map.get(key);
            line = key + "." + valur;
            bw.write(line);
            bw.newLine();
        }
        bw.close();
        br.close();
    }
}
