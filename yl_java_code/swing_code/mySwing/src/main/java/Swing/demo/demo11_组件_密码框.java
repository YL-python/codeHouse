package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JPasswordField 密码框
//与文本框不同，获取密码框里的内容，推荐使用getPassword，该方法会返回一个字符数组，而非字符串
public class demo11_组件_密码框 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        f.setLayout(new FlowLayout());

        JLabel l = new JLabel("密码：");
        // 密码框
        JPasswordField pf = new JPasswordField("");
        pf.setText("&48kdh4@#");
        pf.setPreferredSize(new Dimension(80, 30));

        // 与文本框不同，获取密码框里的内容，推荐使用getPassword，该方法会返回一个字符数组，而非字符串
        char[] password = pf.getPassword();
        String p = String.valueOf(password);
        System.out.println(p);

        f.add(l);
        f.add(pf);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
