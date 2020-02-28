package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

//设计一个像SplitPanel的左右风格的SplitPanel
//左边放3个按钮，上面的文字分别是: 盖伦，提莫，安妮
//右边默认显示盖伦
//当左边按钮点击的时候，右边就会显示对应的图片
public class demo12_面板_题目1 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        f.setLayout(null);
        //左边
        JPanel pleft=new JPanel();
        pleft.setBounds(50, 50, 300, 60);
        pleft.setLayout(new FlowLayout());

        JButton b1=new JButton("滑板鞋");
        JButton b2=new JButton("艾克");
        JButton b3=new JButton("挖掘机");
        pleft.add(b1);
        pleft.add(b2);
        pleft.add(b3);
        pleft.setBackground(Color.red);

        //右边面板
        //1
        JPanel huabanxie=new JPanel();
        JLabel l1=new JLabel();
        ImageIcon i1=new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\gareen.jpg");
        l1.setIcon(i1);
        l1.setBounds(50, 50, i1.getIconWidth(), i1.getIconHeight());
        huabanxie.add(l1);
        //2
        JPanel aike=new JPanel();
        JLabel l2=new JLabel();
        ImageIcon i2=new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\annie.jpg");
        l2.setIcon(i2);
        l2.setBounds(50, 50, i2.getIconWidth(), i2.getIconHeight());
        aike.add(l2);
        //3
        JPanel wanjueji=new JPanel();
        JLabel l3=new JLabel();
        ImageIcon i3=new ImageIcon("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing\\teemo.jpg");
        l3.setIcon(i3);
        l3.setBounds(50, 50, i3.getIconWidth(), i3.getIconHeight());
        wanjueji.add(l3);
        //
        JPanel cards=new JPanel(new CardLayout());
        cards.add(huabanxie,"滑板鞋");
        cards.add(aike,"艾克");
        cards.add(wanjueji,"挖掘机");

        b1.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                CardLayout cl = (CardLayout) (cards.getLayout());
                cl.show(cards, "滑板鞋");

            }
        });
        b2.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                CardLayout cl = (CardLayout) (cards.getLayout());
                cl.show(cards, "艾克");

            }
        });
        b3.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                CardLayout cl = (CardLayout) (cards.getLayout());
                cl.show(cards, "挖掘机");

            }
        });
        //分隔板
        JSplitPane sp=new JSplitPane(JSplitPane.HORIZONTAL_SPLIT,pleft,cards);
        sp.setDividerLocation(80);
        f.setContentPane(sp);
        //结尾
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
