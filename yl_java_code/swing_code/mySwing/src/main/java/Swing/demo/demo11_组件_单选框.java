package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

//JRadioButton 单选框
//使用isSelected来获取是否选中了
//在这个例子里，两个单选框可以被同时选中，为了实现只能选中一个，还需要用到ButtonGroup
public class demo11_组件_单选框 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(580, 200);
        f.setLayout(null);
        JRadioButton b1 = new JRadioButton("物理英雄");
        // 设置 为 默认被选中
        b1.setSelected(true);
        b1.setBounds(50, 50, 130, 30);
        JRadioButton b2 = new JRadioButton("魔法 英雄");
        b2.setBounds(50, 100, 130, 30);

        System.out.println(b2.isSelected());

        f.add(b1);
        f.add(b2);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
