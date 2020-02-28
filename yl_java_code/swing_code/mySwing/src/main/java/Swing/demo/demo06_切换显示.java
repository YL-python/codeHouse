package main.java.Swing.demo;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class demo06_切换显示 {
    public static void main(String[] args) {

        JFrame f = new JFrame("切换显示");
        f.setBounds(580, 200, 400, 300);
        f.setLayout(null);

        JLabel l = new JLabel();

        // 图片
        ImageIcon i = new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\shana.png");
        l.setIcon(i);
        l.setBounds(50, 50, i.getIconWidth(), i.getIconHeight());

        f.add(l);

        // 按钮
        JButton b = new JButton("隐藏图片");
        b.setBounds(150, 200, 100, 30);

        f.add(b);

        /**
         * 按钮增加监听
         */
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (b.getText() == "隐藏图片") {
                    l.setVisible(false);
                    b.setText("显示图片");
                } else {
                    l.setVisible(true);
                    b.setText("隐藏图片");
                }
            }
        });

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
