package main.java.Swing.LED;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;


public class main {
    public static void main(String[] args) {
        int INDEX = 1;
//        String[] colorList={"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"};
        List<LEDSetting> ledSettingList = new ArrayList<>();

        LEDJFrame ledjFrame = new LEDJFrame();  // 实现主页面展示的类


        JFrame f = ledjFrame.makeMainJFrame();
        JLabel centerLabel = ledjFrame.centerLabel(f, INDEX);

//        LEDSetting ledSetting = new LEDSetting();




        //  下面三个按钮
        JButton jButtonLast = new JButton("上一帧");
        jButtonLast.setBounds(220, 800, 180, 35);
        f.add(jButtonLast);
        jButtonLast.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println(111);
            }
        });

        JButton jButtonNext = new JButton("下一帧");
        jButtonNext.setBounds(800, 800, 180, 35);
        f.add(jButtonNext);
        jButtonNext.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                LEDOneSetting ledOneSetting = new LEDOneSetting();  // 每一页展示的类
                LEDSetting ledSetting = ledOneSetting.SetOnePage(f);
                ledSettingList.add(ledSetting);
                System.out.println(ledSettingList);
            }
        });

        JButton jButtonOver = new JButton("生成文件");
        jButtonOver.setBounds(510, 800, 180, 35);
        f.add(jButtonOver);
        jButtonOver.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });



        ledjFrame.showJFrame(f);
    }
}
