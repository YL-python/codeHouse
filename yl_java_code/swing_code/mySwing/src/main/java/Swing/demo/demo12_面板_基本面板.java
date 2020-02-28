package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JPanel即为基本面板
//面板和JFrame一样都是容器，不过面板一般用来充当中间容器，把组件放在面板上，然后再把面板放在窗体上。
//一旦移动一个面板，其上面的组件，就会全部统一跟着移动，采用这种方式，便于进行整体界面的设计
public class demo12_面板_基本面板 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        f.setLayout(null);

        JPanel p1 = new JPanel();
        // 设置面板大小
        p1.setBounds(50, 50, 300, 60);
        // 设置面板背景颜色
        p1.setBackground(Color.RED);

        // 这一句可以没有，因为JPanel默认就是采用的FlowLayout
        p1.setLayout(new FlowLayout());

        JButton b1 = new JButton("英雄1");
        JButton b2 = new JButton("英雄2");
        JButton b3 = new JButton("英雄3");

        // 把按钮加入面板
        p1.add(b1);
        p1.add(b2);
        p1.add(b3);

        JPanel p2 = new JPanel();
        JButton b4 = new JButton("英雄4");
        JButton b5 = new JButton("英雄5");
        JButton b6 = new JButton("英雄6");

        p2.add(b4);
        p2.add(b5);
        p2.add(b6);

        p2.setBackground(Color.BLUE);
        p2.setBounds(10, 150, 300, 60);

        // 把面板加入窗口
        f.add(p1);
        f.add(p2);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
