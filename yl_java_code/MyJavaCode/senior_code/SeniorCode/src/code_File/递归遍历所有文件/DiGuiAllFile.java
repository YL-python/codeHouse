package code_File.递归遍历所有文件;

import java.io.File;
import java.sql.SQLOutput;

public class DiGuiAllFile {
    public static void main(String[] args) {
        File f = new File("F:\\java\\黑马java\\1-3-Java语言高级");
        getAllFile(f);
    }

    public static void getAllFile(File dir){
        System.out.println(dir);
        File[] fd = dir.listFiles();
        for (File fdfor : fd) {
            if(fdfor.isDirectory()){
                getAllFile(fdfor);
            }else{
                System.out.println(fdfor);
            }
        }
    }
}
