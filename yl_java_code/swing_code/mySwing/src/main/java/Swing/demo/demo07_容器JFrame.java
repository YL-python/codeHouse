package main.java.Swing.demo;

import javax.swing.*;

// JFrame是最常用的窗体型容器，默认情况下，在右上角有最大化最小化按钮
public class demo07_容器JFrame {
    public static void main(String[] args) {

        //普通的窗体，带最大和最小化按钮
        JFrame f = new JFrame("JFrame");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(null);
        JButton b = new JButton("一键秒对方基地挂");
        b.setBounds(50, 50, 280, 30);

        f.add(b);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
