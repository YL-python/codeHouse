package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JComboBox 下拉框
// 使用getSelectedItem来获取被选中项
// 使用setSelectedItem() 来指定要选中项
public class demo11_组件_下拉框 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(580, 240);
        f.setLayout(null);

        //下拉框出现的条目
        String[] heros = new String[] { "卡特琳娜", "库奇" };
        JComboBox cb = new JComboBox(heros);

        cb.setBounds(50, 50, 80, 30);

        cb.setSelectedItem("库奇");
        System.out.println(cb.getSelectedItem());

        f.add(cb);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
