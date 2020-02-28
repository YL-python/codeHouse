package text;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class day01 {
    public static void main(String[] args) throws IOException, InterruptedException {
        System.out.println("开始咯");
        Process proc;
        try {
            proc = Runtime.getRuntime().exec("python D:\\Intellij_IDEA\\MyProject\\Java_Python\\src\\text\\competition_spider.py");// 执行py文件
            //用输入输出流来截取结果
            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }
            in.close();
            proc.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
