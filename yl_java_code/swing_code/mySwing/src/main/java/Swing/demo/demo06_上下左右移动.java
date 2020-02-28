package main.java.Swing.demo;

import javax.swing.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class demo06_上下左右移动 {
    public static void main(String[] args) {

        JFrame f = new JFrame("上下左右移动");
        f.setBounds(580, 200, 400, 300);
        f.setLayout(null);

        JLabel l = new JLabel();

        ImageIcon i = new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\shana.png");
        l.setIcon(i);
        l.setBounds(50, 50, i.getIconWidth(), i.getIconHeight());

        f.add(l);

        /**
         * 增加按键监听适配器
         */
        f.addKeyListener(new KeyAdapter() {

            // 键被弹起
            @Override
            public void keyReleased(KeyEvent e) {
                if (e.getKeyCode() == 38) {
                    // 上 “38”
                    l.setLocation(l.getX(), l.getY() - 10);
                } else if (e.getKeyCode() == 40) {
                    // 下 “40”
                    l.setLocation(l.getX(), l.getY() + 10);
                } else if (e.getKeyCode() == 37) {
                    // 左 “37”
                    l.setLocation(l.getX() - 10, l.getY());
                } else if (e.getKeyCode() == 39) {
                    // 右 “39”
                    l.setLocation(l.getX() + 10, l.getY());
                }
            }
        });

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
