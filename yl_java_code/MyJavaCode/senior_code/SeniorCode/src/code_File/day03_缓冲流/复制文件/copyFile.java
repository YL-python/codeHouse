package code_File.day03_缓冲流.复制文件;

import java.io.*;

public class copyFile {
    public static void main(String[] args) throws IOException {
//        show01();  // 单字节复制文件用时：45673毫秒
//        System.out.println("========================");
//        show02();  // 多字节复制文件用时：69毫秒
//        System.out.println("========================");
//        show03();  // 缓冲单字节复制文件用时：158毫秒
//        System.out.println("========================");
//        show04();  // 缓冲多字节复制文件用时：31毫秒
//        System.out.println("========================");
    }

    private static void show01() throws IOException {
        System.out.println("单字节复制文件开始!");
        long s = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\原文件.png");
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\单字节复制后文件.png");
        int len = 0;
        while ((len = fis.read()) != -1) {
            fos.write(len);
        }
        fis.close();
        fos.close();
        System.out.println("单字节复制文件结束!");
        long e = System.currentTimeMillis();
        System.out.println("单字节复制文件用时：" + (e - s) + "毫秒");
    }

    private static void show02() throws IOException {
        System.out.println("多字节复制文件开始!");
        long s = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\原文件.png");
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\多字节复制后文件.png");
        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = fis.read(bytes)) != -1) {
            fos.write(bytes, 0, len);
        }
        fis.close();
        fos.close();
        System.out.println("多字节复制文件结束!");
        long e = System.currentTimeMillis();
        System.out.println("多字节复制文件用时：" + (e - s) + "毫秒");
    }
    private static void show03() throws IOException {
        System.out.println("缓冲单字节复制文件开始!");
        long s = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\原文件.png");
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\缓冲单字节复制后文件.png");
        BufferedInputStream bis = new BufferedInputStream(fis);
        BufferedOutputStream bos = new BufferedOutputStream(fos);
        int len = 0;
        while ((len = bis.read()) != -1) {
            bos.write(len);
        }
        bis.close();
        bos.close();
        System.out.println("缓冲单字节复制文件结束!");
        long e = System.currentTimeMillis();
        System.out.println("缓冲单字节复制文件用时：" + (e - s) + "毫秒");
    }
    private static void show04() throws IOException {
        System.out.println("缓冲多字节复制文件开始!");
        long s = System.currentTimeMillis();
        FileInputStream fis = new FileInputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\原文件.png");
        FileOutputStream fos = new FileOutputStream("D:\\Intellij_IDEA\\senior_code\\SeniorCode\\src\\code_File\\缓冲流\\复制文件\\缓冲多字节复制后文件.png");
        BufferedInputStream bis = new BufferedInputStream(fis);
        BufferedOutputStream bos = new BufferedOutputStream(fos);
        int len = 0;
        byte[] bytes = new byte[1024];
        while ((len = bis.read(bytes)) != -1) {
            bos.write(bytes, 0, len);
        }
        bis.close();
        bos.close();
        System.out.println("缓冲多字节复制文件结束!");
        long e = System.currentTimeMillis();
        System.out.println("缓冲多字节复制文件用时：" + (e - s) + "毫秒");
    }
}
