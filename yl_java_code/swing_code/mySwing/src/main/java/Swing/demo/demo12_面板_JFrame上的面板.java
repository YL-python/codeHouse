package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JFrame上有一层面板，叫做ContentPane
//平时通过f.add()向JFrame增加组件，其实是向JFrame上的 ContentPane加东西
public class demo12_面板_JFrame上的面板 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(null);
        JButton b = new JButton("一键秒对方基地挂");
        b.setBounds(50, 50, 280, 30);

        f.add(b);
        // JFrame上有一层面板，叫做ContentPane
        // 平时通过f.add()向JFrame增加组件，其实是向JFrame上的 ContentPane加东西
        // f.add等同于f.getContentPane().add(b);
        f.getContentPane().add(b);

        // b.getParent()获取按钮b所处于的容器
        // 打印出来可以看到，实际上是ContentPane而非JFrame
        System.out.println(b.getParent());

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
