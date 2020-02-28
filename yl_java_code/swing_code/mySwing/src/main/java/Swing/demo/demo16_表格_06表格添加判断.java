package main.java.Swing.demo;

import main.java.Swing.domain.HeroTableModel;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// 显示一个Table需要两组数据
//1. 一维数组： String[]columnNames 表示表格的标题
//2. 二维数组： String[][] heros 表格中的内容
//默认情况下，表格的标题是不会显示出来了，除非使用了JScrollPane
public class demo16_表格_06表格添加判断 {
    public static void main(String[] args) {
        final JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        f.setLayout(new BorderLayout());

        final HeroTableModel htm = new HeroTableModel();

        final JTable t = new JTable(htm);
        // 设置选择模式为 只能选中一行
//        t.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        // 选中第一行 （基本0）
//        t.getSelectionModel().setSelectionInterval(0, 0);
        JPanel p = new JPanel();

        final JLabel lName = new JLabel("名称");
        final JTextField tfName = new JTextField("");
        final JLabel lHp = new JLabel("血量");
        final JTextField tfHp = new JTextField("");
        JButton bAdd = new JButton("增加");
        tfName.setPreferredSize(new Dimension(80, 30));
        tfHp.setPreferredSize(new Dimension(80, 30));

        p.add(lName);
        p.add(tfName);
        p.add(lHp);
        p.add(tfHp);
        p.add(bAdd);

        bAdd.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

                Hero h = new Hero();
                String name = tfName.getText();

                // 通过name长度判断 名称是否为空
                if (name.length() == 0) {
                    // 弹出对话框提示用户
                    JOptionPane.showMessageDialog(f, "名称不能为空");

                    // 名称输入框获取焦点
                    tfName.grabFocus();
                    return;
                }

                String hp = tfHp.getText().trim();

                try {
                    // 把hp转换为浮点型，如果出现异常NumberFormatException表示不是浮点型格式
                    Float.parseFloat(hp);
                } catch (NumberFormatException e1) {
                    JOptionPane.showMessageDialog(f, "血量只能是小数 ");
                    tfHp.grabFocus();
                    return;
                }
                t.updateUI();

            }
        });

        JScrollPane sp = new JScrollPane(t);

        f.add(p, BorderLayout.NORTH);
        f.add(sp, BorderLayout.CENTER);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
