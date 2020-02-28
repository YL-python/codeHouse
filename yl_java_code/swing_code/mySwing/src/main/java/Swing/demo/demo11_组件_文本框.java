package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JTextField 输入框
//setText 设置文本
//getText 获取文本
//JTextField 是单行文本框，如果要输入多行数据，请使用JTextArea
//tfPassword.grabFocus(); 表示让密码输入框获取焦点

public class demo11_组件_文本框 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        f.setLayout(new FlowLayout());

        JLabel lName = new JLabel("账号：");
        // 输入框
        JTextField tfName = new JTextField("");
        tfName.setText("请输入账号");
        tfName.setPreferredSize(new Dimension(80, 30));

        JLabel lPassword = new JLabel("密码：");
        // 输入框
        JTextField tfPassword = new JTextField("");
        tfPassword.setText("请输入密码");
        tfPassword.setPreferredSize(new Dimension(80, 30));

        f.add(lName);
        f.add(tfName);
        f.add(lPassword);
        f.add(tfPassword);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
        // 获取焦点
        tfPassword.grabFocus();
    }
}
