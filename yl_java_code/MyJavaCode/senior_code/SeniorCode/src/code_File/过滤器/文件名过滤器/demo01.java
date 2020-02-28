package code_File.过滤器.文件名过滤器;

import java.io.File;
import java.io.FileFilter;
import java.io.FilenameFilter;

public class demo01 {
    public static void main(String[] args) {
        File f = new File("F:\\java\\黑马java\\1-3-Java语言高级");
        getAllFile(f);
    }

    public static void getAllFile(File dir){
        System.out.println(dir);
        File[] fd = dir.listFiles(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                return new File(dir,name).isDirectory() || name.toLowerCase().endsWith(".java");
            }
        });
        for (File fdfor : fd) {
            if(fdfor.isDirectory()){
                getAllFile(fdfor);
            }else{
                System.out.println(fdfor);
            }
        }
    }
}
