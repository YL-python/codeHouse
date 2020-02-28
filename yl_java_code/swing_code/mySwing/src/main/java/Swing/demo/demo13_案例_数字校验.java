package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class demo13_案例_数字校验 {
    public static void main(String[] args) {
        // 主窗体
        JFrame f = new JFrame("数字校验");
        // 主窗体设置大小
        f.setSize(400, 300);
        // 主窗体设置位置
        f.setLocation(200, 200);
        // 主窗体中的组件设置为水平顺序布局
        f.setLayout(new FlowLayout());
        // 文本框
        JTextField tf = new JTextField("");
        // 设置大小
        tf.setPreferredSize(new Dimension(80, 30));
        //表示让输入框获取焦点
        tf.grabFocus();

        JButton jb = new JButton("检测");

        f.add(tf);
        f.add(jb);
        // 关闭窗体的时候，退出程序
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // 让窗体变得可见
        f.setVisible(true);

        // 给按钮 增加 监听
        jb.addActionListener(new ActionListener() {

            // 当按钮被点击时，就会触发 ActionEvent事件
            // actionPerformed 方法就会被执行
            public void actionPerformed(ActionEvent e) {
                //获取文本框内容
                try{
                    String value = tf.getText();
                    Integer.parseInt(value);
                    JOptionPane.showMessageDialog(f, "是整数");
                }catch (Exception x){
                    JOptionPane.showMessageDialog(f, "不是整数");
                }
            }
        });
    }
}
