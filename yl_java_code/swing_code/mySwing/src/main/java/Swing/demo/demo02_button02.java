package main.java.Swing.demo;

import javax.swing.*;
import java.io.*;

public class demo02_button02 {
    public static void main(String[] args) {
        File file = new File("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\weizhi.txt");
        String x = null;
        String y = null;
        // 主窗体
        JFrame f = new JFrame("第一个窗体");

        // 主窗体设置大小
        f.setSize(400, 300);

        try {
            FileInputStream fis = new FileInputStream(file);
            byte[] b = new byte[1024];
            fis.read(b);
            String line = new String(b).trim();
            if (!line.equals("")) {
                // 文件里用@区隔开横纵坐标
                x = line.split("@")[0];
                y = line.split("@")[1];
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 主窗体设置位置
        if (x == null || y == null) {
            f.setLocation(200, 200);
        } else {
            f.setLocation(Integer.parseInt(x), Integer.parseInt(y));
        }

        // 主船体中的组件设置为绝对定位
        f.setLayout(null);

        // 按钮组件
        JButton b = new JButton("一键秒对方基地挂");

        // 同时设置组件的大小和位置
        b.setBounds(50, 50, 280, 30);

        // 把按钮加入到主窗体中
        f.add(b);

        // 关闭窗体的时候，退出程序
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 让窗体变得可见
        f.setVisible(true);

        Thread thread = new Thread() {
            public void run() {
                while (true) {
                    try (FileOutputStream fos = new FileOutputStream(file)) {
                        String line = f.getX() + "@" + f.getY();
                        fos.write(line.getBytes());
                        System.out.println("当前主窗体位置————x：" + f.getX() + "  y：" + f.getY());
                        Thread.sleep(100);
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        };
        thread.start();
    }
}
