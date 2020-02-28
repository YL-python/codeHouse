package main.java.Swing.demo;

import main.java.Swing.domain.HeroTableModel;

import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import java.awt.*;

// 显示一个Table需要两组数据
//1. 一维数组： String[]columnNames 表示表格的标题
//2. 二维数组： String[][] heros 表格中的内容
//默认情况下，表格的标题是不会显示出来了，除非使用了JScrollPane
public class demo16_表格_05表格监听 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(new BorderLayout());

        final HeroTableModel htm = new HeroTableModel();

        final JTable t = new JTable(htm);
        // 准备一个Panel上面放一个Label用于显示哪条被选中了
        JPanel p = new JPanel();
        final JLabel l = new JLabel("暂时未选中条目");
        p.add(l);

        JScrollPane sp = new JScrollPane(t);

        // 使用selection监听器来监听table的哪个条目被选中
        t.getSelectionModel().addListSelectionListener(
                new ListSelectionListener() {

                    // 当选择了某一行的时候触发该事件
                    public void valueChanged(ListSelectionEvent e) {
                        // 获取哪一行被选中了
                        int row = t.getSelectedRow();

                        // 更新标签内容
                        l.setText("当前选中的英雄是： " +  htm.heros[row][1]);

                    }
                });

        f.add(p, BorderLayout.NORTH);
        f.add(sp, BorderLayout.CENTER);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
