package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;

public class demo10_计算器布局 {
    public static void main(String[] args) {

        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);
        // 设置布局器为GridLayerout，即网格布局器
        // 该GridLayerout的构造方法表示该网格是4行5列
        //f.setLayout(new GridLayout(4, 5));
        GridLayout lay = new GridLayout(4, 5);
        lay.setHgap(10);  // hgap - 组件之间以及组件与 container 的边之间的水平间隙
        lay.setVgap(10);
        f.setLayout(lay);

        String[] s = {"7","8","9 ","/ ","sq","4","5","6","*","%","1","2","3","-","1/x","0","+/-",".","+","="};

        JButton[] bs = new JButton[20];
        for(int i=0;i<20;i++){
            bs[i] = new JButton(s[i]);
            // 即便 使用 布局器 ，也可以 通过setPreferredSize，向布局器建议该组件显示的大小
            bs[i].setPreferredSize(new Dimension(20, 40));
        }

        for(JButton b:bs){
            f.add(b);
        }
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
