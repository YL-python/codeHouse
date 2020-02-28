package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

//
public class demo11_组件_进度条 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        f.setLayout(new FlowLayout());

        JProgressBar pb = new JProgressBar();

        //进度条最大100
        pb.setMaximum(100);
        //当前进度是50
        pb.setValue(50);
        //显示当前进度
        pb.setStringPainted(true);

        f.add(pb);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
