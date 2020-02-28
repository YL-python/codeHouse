package main.java.Swing.demo;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class demo13_案例_字符串拼接 {
    public static void main(String[] args) {
        JFrame f = new JFrame("我是最棒哒！");
        f.setSize(600, 450);
        f.setLocation(200, 200);
        f.setLayout(null);
        //地名
        JLabel dm=new JLabel("地名：");
        dm.setBounds(20, 10, 100, 30);
        JTextField tdm = new JTextField("");
        tdm.setBounds(120, 10, 120, 30);
        //公司类型
        JLabel lx=new JLabel("公司类型：");
        lx.setBounds(300, 10, 100, 30);
        JTextField tlx = new JTextField("");
        tlx.setBounds(400, 10, 120, 30);
        //公司名称
        JLabel gs=new JLabel("公司名称：");
        gs.setBounds(20, 50, 100, 30);
        JTextField tgs = new JTextField("");
        tgs.setBounds(120, 50, 120, 30);
        //老板名称
        JLabel lb=new JLabel("老板名称：");
        lb.setBounds(300, 50, 100, 30);
        JTextField tlb = new JTextField("");
        tlb.setBounds(400, 50, 120, 30);
        //金额
        JLabel je=new JLabel("金额：");
        je.setBounds(20, 90, 100, 30);
        JTextField tje = new JTextField("");
        tje.setBounds(120, 90, 120, 30);
        //产品
        JLabel cp=new JLabel("产品：");
        cp.setBounds(300, 90, 100, 30);
        JTextField tcp = new JTextField("");
        tcp.setBounds(400, 90, 120, 30);
        //价格计量单位
        JLabel jg=new JLabel("价格计量单位：");
        jg.setBounds(20, 130, 100, 30);
        JTextField tjg = new JTextField("");
        tjg.setBounds(120, 130, 120, 30);
        ///按钮
        JButton b=new JButton("生成");
        b.setBounds(250,200,100,30);
        //文本框
        JTextArea ta=new JTextArea();
        ta.setBounds(30, 250, 520,150);
        ta.setLineWrap(true);
        //提前准备字符串
        String s="1最大23倒闭了，王八蛋老板4吃喝嫖赌，欠下了5个亿，"
                + "带着他的小姨子跑了!我们没有办法，拿着6抵工资!"
                + "原价都是一7多、两7多、三7多的6，现在全部只卖二十块，统统只要二十块!"
                + "4王八蛋，你不是人!我们辛辛苦苦给你干了大半年，你不发工资，你还我血汗钱，还我血汗钱!";
        //监听
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                //判断为空
                if(tdm.getText().length()==0||tlx.getText().length()==0||tgs.getText().length()==0||tlb.getText().length()==0||
                        tje.getText().length()==0||tcp.getText().length()==0||tjg.getText().length()==0){
                    JOptionPane.showMessageDialog(f, "你倒是填完整啊！");
                    return;
                }
                //判断数字
                String si=tje.getText();
                for(int i=0;i<si.length();i++){
                    if(!Character.isDigit(si.charAt(i))){
                        JOptionPane.showMessageDialog(f, "让你输数字知不知道！");
                        return;
                    }
                }
                //打印文本
                String st=s;
                String[] ss=new String[]{tdm.getText(),tlx.getText(),tgs.getText(),
                        tlb.getText(),tje.getText(),tcp.getText(),tjg.getText()};
                for(int i=1;i<8;i++){
                    st=st.replaceAll(String.valueOf(i),ss[i-1]);
                }
                ta.append(st);
            }
        });
        f.add(dm);f.add(tdm);
        f.add(lx);f.add(tlx);
        f.add(gs);f.add(tgs);
        f.add(lb);f.add(tlb);
        f.add(je);f.add(tje);
        f.add(cp);f.add(tcp);
        f.add(jg);f.add(tjg);
        f.add(b);f.add(ta);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
