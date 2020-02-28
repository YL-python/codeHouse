package main.java.Swing.demo;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class demo08_模态与大小变化 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LOL");
        f.setSize(400, 300);
        f.setLocation(580, 200);
        f.setLayout(null);

        JButton b1 = new JButton("打开一个模态窗口");
        b1.setBounds(50, 50, 280, 30);

        f.add(b1);

        JDialog d = new JDialog(f);
        d.setModal(true);
        d.setTitle("这是一个模态窗口");
        d.setSize(200, 150);
        d.setLocation(650, 300);
        d.setLayout(null);

        JButton b2 = new JButton("锁定大小");
        b2.setBounds(50, 50, 100, 30);

        d.add(b2);

        // 增加按钮监听器
        b1.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                d.setVisible(true);
            }
        });

        b2.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if (b2.getText() == "锁定大小") {
                    d.setResizable(false);
                    b2.setText("解锁大小");
                } else {
                    d.setResizable(true);
                    b2.setText("锁定大小");
                }
            }
        });

        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
}
