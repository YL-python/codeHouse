package main.java.Swing.demo;


import javax.swing.*;
import java.awt.*;

// 设置布局器为BorderLayout
// 容器上的组件按照上北 下南 左西 右东 中的顺序摆放
public class demo09_布局_北南西东中 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        // 设置布局器为BorderLayerout
        // 容器上的组件按照上北下南左西右东中的顺序摆放
        f.setLayout(new BorderLayout());

        JButton b1 = new JButton("洪七");
        JButton b2 = new JButton("段智兴");
        JButton b3 = new JButton("欧阳锋");
        JButton b4 = new JButton("黄药师");
        JButton b5 = new JButton("周伯通");

        // 加入到容器的时候，需要指定位置
        f.add(b1, BorderLayout.NORTH);
        f.add(b2, BorderLayout.SOUTH);
        f.add(b3, BorderLayout.WEST);
        f.add(b4, BorderLayout.EAST);
        f.add(b5, BorderLayout.CENTER);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
