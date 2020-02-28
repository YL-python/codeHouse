package main.java.Swing.demo;


import javax.swing.*;
import java.awt.*;

// 即便 使用 布局器 ，也可以 通过setPreferredSize，向布局器建议该组件显示的大小.
//注 只对部分布局器起作用，比如FlowLayout可以起作用。 比如GridLayout就不起作用，因为网格布局器必须对齐
public class demo10_布局_修改布局元素大小 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(new FlowLayout());

        JButton b1 = new JButton("英雄1");
        JButton b2 = new JButton("英雄2");
        JButton b3 = new JButton("英雄3");

        // 即便 使用 布局器 ，也可以 通过setPreferredSize，向布局器建议该组件显示的大小
        b3.setPreferredSize(new Dimension(180, 40));

        f.add(b1);
        f.add(b2);
        f.add(b3);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
