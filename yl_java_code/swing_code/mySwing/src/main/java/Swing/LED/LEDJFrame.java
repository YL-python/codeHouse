package main.java.Swing.LED;

import javax.swing.*;
import java.awt.*;

public class LEDJFrame {
    public JFrame makeMainJFrame(){
        // 主窗体
        JFrame f = new JFrame("流水灯");
        // 主窗体设置大小
        f.setSize(1200, 1000);
        // 主窗体设置位置
        f.setLocationRelativeTo(null);
        // 主窗体中的组件设置为绝对定位
        f.setLayout(null);
        return f;
    }

    public void showJFrame(JFrame f){
        // 关闭窗体的时候，退出程序
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // 让窗体变得可见
        f.setVisible(true);
        // 窗体大小不可变
        f.setResizable(false);
    }

    public JLabel centerLabel(JFrame f ,int index){
        JLabel L1 = new JLabel("正在设置第 "+index+" 帧");
        L1.setBounds(510, 50, 200, 35);
        L1.setFont(new Font(Font.DIALOG, Font.BOLD, 25));
        f.add(L1);
        return L1;
    }
}
