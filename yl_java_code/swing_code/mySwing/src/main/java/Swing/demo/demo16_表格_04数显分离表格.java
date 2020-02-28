package main.java.Swing.demo;

import main.java.Swing.domain.HeroTableModel;

import javax.swing.*;
import java.awt.*;

// 显示一个Table需要两组数据
//1. 一维数组： String[]columnNames 表示表格的标题
//2. 二维数组： String[][] heros 表格中的内容
//默认情况下，表格的标题是不会显示出来了，除非使用了JScrollPane
public class demo16_表格_04数显分离表格 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(new BorderLayout());

        //创建一个TableModel
        HeroTableModel htm= new HeroTableModel();

        //根据 TableModel来创建 Table
        JTable t = new JTable(htm);

        JScrollPane sp = new JScrollPane(t);

        f.add(sp, BorderLayout.CENTER);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
