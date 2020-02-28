package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// 显示一个Table需要两组数据
//1. 一维数组： String[]columnNames 表示表格的标题
//2. 二维数组： String[][] heros 表格中的内容
//默认情况下，表格的标题是不会显示出来了，除非使用了JScrollPane
public class demo16_表格_02滚动条表格 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(new BorderLayout());

        String[] columnNames = new String[] { "id", "name", "hp", "damage" };
        String[][] heros = new String[][] { { "1", "盖伦", "616", "100" },
                { "2", "提莫", "512", "102" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" }, { "3", "奎因", "832", "200" } };
        JTable t = new JTable(heros, columnNames);

        // 根据t创建 JScrollPane
        JScrollPane sp = new JScrollPane(t);

        //或则创建一个空的JScrollPane，再通过setViewportView把table放在JScrollPane中
        // JScrollPane sp = new JScrollPane(t);
        // sp.setViewportView(t);

        // 把sp而非JTable加入到JFrame上，
        f.add(sp, BorderLayout.CENTER);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
