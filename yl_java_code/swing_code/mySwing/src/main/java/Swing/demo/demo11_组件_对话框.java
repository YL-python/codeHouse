package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

// JOptionPane 用于弹出对话框
//JOptionPane.showConfirmDialog(f, "是否 使用外挂 ？");
//表示询问，第一个参数是该对话框以哪个组件对齐
//JOptionPane.showInputDialog(f, "请输入yes，表明使用外挂后果自负");
//接受用户的输入
//JOptionPane.showMessageDialog(f, "你使用外挂被抓住！ 罚拣肥皂3次！");
//显示消息
public class demo11_组件_对话框 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(580, 240);
        f.setLayout(null);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);

        int option = JOptionPane.showConfirmDialog(f, "是否 使用外挂 ？");
        if (JOptionPane.OK_OPTION == option) {
            String answer = JOptionPane.showInputDialog(f, "请输入yes，表明使用外挂后果自负");
            if ("yes".equals(answer))
                JOptionPane.showMessageDialog(f, "你使用外挂被抓住！ 罚拣肥皂3次！");
            else {
                JOptionPane.showMessageDialog(f, "这次就饶了你");
            }
        }
    }
}
