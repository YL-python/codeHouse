package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;
import java.io.FileOutputStream;
import java.io.IOException;

// JCheckBox 复选框
//使用isSelected来获取是否选中了
public class demo11_组件_复选框 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(580, 200);
        f.setLayout(null);

        JCheckBox bCheckBox = new JCheckBox("物理 英雄");
        //设置 为 默认被选中
        bCheckBox.setSelected(true);
        bCheckBox.setBounds(50, 50, 130, 30);

        JCheckBox bCheckBox2 = new JCheckBox("魔法 英雄");
        bCheckBox2.setBounds(50, 100, 130, 30);
        //判断 是否 被 选中
        System.out.println(bCheckBox2.isSelected());

        f.add(bCheckBox);
        f.add(bCheckBox2);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);


//        Thread thread = new Thread() {
//            Boolean flag = bCheckBox.isSelected();
//            Boolean flag2 = bCheckBox2.isSelected();
//            public void run() {
//                while (true) {
//                    if(bCheckBox.isSelected() != flag){
//                        System.out.println("物理英雄被选中了");
//                        flag = !flag;
//                    }
//                    if(bCheckBox2.isSelected() != flag2){
//                        System.out.println("魔法英雄被选中了");
//                        flag2 = !flag2;
//                    }
//                }
//            }
//        };
//        thread.start();
    }
}
