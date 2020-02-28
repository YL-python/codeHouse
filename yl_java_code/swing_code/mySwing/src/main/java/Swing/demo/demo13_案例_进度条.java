package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class demo13_案例_进度条 {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(null);

        int n = 0;
        int m = 100;
        JPanel p = new JPanel();// 基本面板

        p.setBounds(100, 50, 200, 80);
        JLabel l = new JLabel("女朋友生成进度条");

        JProgressBar pr = new JProgressBar();// 进度条
        pr.setMinimum(n);
        pr.setStringPainted(true);

        p.add(l);
        p.add(pr);
        f.add(p);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);

        while (true) {
            try {
                Thread.sleep(m);
                m += 50;// 每次加多少时间
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            pr.setValue(++n);
            if (n == 100) {
                boolean boo = false;  // 退出程序使用
                int a = JOptionPane.showConfirmDialog(f, "女朋友已生成！是否继续生成？");// 询问对话框
                if (JOptionPane.OK_OPTION == a) {
                    n = 0;
                    m = 10;
                    l.setText("女朋友继续生成进度条");
                }
                if (JOptionPane.NO_OPTION == a) {
                    JOptionPane.showMessageDialog(f, "已停止女朋友生成！");
                    boo = true;
                }
                if (boo == true) {
                    JOptionPane.showMessageDialog(f, "程序结束！");
                    System.exit(0);
                }
            }
        }
    }
}
