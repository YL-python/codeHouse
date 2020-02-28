package code_File.过滤器.路径过滤器;

import java.io.File;

public class demo01 {
    public static void main(String[] args) {
        File f = new File("F:\\java\\黑马java\\1-3-Java语言高级");
        getAllFile(f);
    }

    public static void getAllFile(File dir){
        System.out.println(dir);
        File[] fd = dir.listFiles(new FileFilterImpl());
        for (File fdfor : fd) {
            if(fdfor.isDirectory()){
                getAllFile(fdfor);
            }else{
                System.out.println(fdfor);
            }
        }
    }
}
