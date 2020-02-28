package SnakeCode;

import javax.swing.*;

public class SnakeMain {
    public static void main(String[] args) {
        JFrame frame = new JFrame();  // 创建窗口
        frame.setBounds(10,10,915,720);  // 起始位置和大小
        frame.setResizable(false);  // 不可修改
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // 关闭按钮

        frame.add(new Panel());

        frame.setVisible(true);  // 展示
    }
}
