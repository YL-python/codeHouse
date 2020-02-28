package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// java GUI 显示图片是通过在label上设置图标实现的
public class demo11_组件_图片 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(580, 200);
        f.setLayout(null);

        JLabel l = new JLabel();

        //根据图片创建ImageIcon对象
        ImageIcon i = new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\shana.png");
        //设置ImageIcon
        l.setIcon(i);
        //label的大小设置为ImageIcon,否则显示不完整
        l.setBounds(50, 50, i.getIconWidth(), i.getIconHeight());

        f.add(l);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
