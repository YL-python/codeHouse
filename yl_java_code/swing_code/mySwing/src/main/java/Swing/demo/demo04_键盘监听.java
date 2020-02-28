package main.java.Swing.demo;


// 键盘监听器： KeyListener
// keyPressed 代表 键被按下
// keyReleased 代表 键被弹起
// keyTyped 代表 一个按下弹起的组合动作
// KeyEvent.getKeyCode() 可以获取当前点下了哪个键

import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class demo04_键盘监听 {
    public static void main(String[] args) {
        JFrame f = new JFrame("键盘监听");
        f.setSize(400, 300);
        f.setLocation(580, 200);
        f.setLayout(null);

        final JLabel l = new JLabel();

        ImageIcon i = new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\shana.png");
        l.setIcon(i);
        l.setBounds(50, 50, i.getIconWidth(), i.getIconHeight());

        // 增加键盘监听
        f.addKeyListener(new KeyListener() {
            // 键被弹起
            public void keyReleased(KeyEvent e) {
                // 32代表按下了 “空格”
                System.out.println(e.getKeyCode());
                if (e.getKeyCode() == 32) {
                    // 图片向右移动 （y坐标不变，x坐标增加）
                    l.setLocation(l.getX() + 10, l.getY());
                }
            }
            //键被按下
            public void keyPressed(KeyEvent e) {
                // TODO Auto-generated method stub
            }
            // 一个按下弹起的组合动作
            public void keyTyped(KeyEvent e) {
            }
        });

        f.add(l);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
