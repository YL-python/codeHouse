package main.java.Swing.demo;


import javax.swing.*;

// 绝对定位就是指不使用布局器，组件的位置和大小需要单独指定
public class demo09_布局_绝对定位 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        // 设置布局器为null，即进行绝对定位，容器上的组件都需要指定位置和大小
        f.setLayout(null);
        JButton b1 = new JButton("英雄1");
        // 指定位置和大小
        b1.setBounds(50, 50, 80, 30);
        JButton b2 = new JButton("英雄2");
        b2.setBounds(150, 50, 80, 30);
        JButton b3 = new JButton("英雄3");
        b3.setBounds(250, 50, 80, 30);
        // 没有指定位置和大小，不会出现在容器上
        JButton b4 = new JButton("英雄4");

        f.add(b1);
        f.add(b2);
        f.add(b3);
        // b4没有指定位置和大小，不会出现在容器上
        f.add(b4);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
