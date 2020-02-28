package main.java.Swing.demo;

import javax.swing.*;

// JDialog也是窗体型容器，右上角没有最大和最小化按钮
public class demo07_容器JDialog {
    public static void main(String[] args) {

        // 对话框却不带最大和最小化按钮
        JDialog d = new JDialog();
        d.setTitle("LOL");
        d.setSize(400, 300);
        d.setLocation(200, 200);
        d.setLayout(null);
        JButton b = new JButton("一键秒对方基地挂");
        b.setBounds(50, 50, 280, 30);

        d.add(b);

        d.setVisible(true);
    }
}
