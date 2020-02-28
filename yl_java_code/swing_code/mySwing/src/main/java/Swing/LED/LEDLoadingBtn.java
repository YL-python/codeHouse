package main.java.Swing.LED;


//        int[] xList = {7,8,9,10,11,12,13,13,13,13,12,11,10,9,8,7,6,5,4,3,2,1,1,1,1,2,3,4,5,6};
//        int[] yList = {4,3,2,1,1,2,3,4,5,6,7,8,9,10,11,12,11,10,9,8,7,6,5,4,3,2,1,1,2,3};

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LEDLoadingBtn {

    public void showBtn(JFrame f, LEDSetting ledSetting){
        int[] xList = {560,640,720,800,880,960,1040,1060,1060,1040,960,880,800,720,640,560,480,400,320,240,160,80,60,60,80,160,240,320,400,480};
        int[] yList = {220,165,110,55,55,110,165,220,275,330,385,440,495,550,605,660,605,550,495,440,385,330,275,220,165,110,55,55,110,165};

//        LEDBtn ledBtn = new LEDBtn();  // 实现多个按钮的类
        for (int i = 0; i < 30; i++) {
            markBtn(f,xList[i],yList[i],i,ledSetting.getColorList());
        }
    }

    public void showTimeText(JFrame f, LEDSetting ledSetting){
        JLabel L1 = new JLabel("点击设置当前帧延的延迟时间： "+ledSetting.getTime()+" ms");
        L1.setBounds(300, 730, 480, 35);
        L1.setFont(new Font(Font.DIALOG, Font.BOLD, 25));
        f.add(L1);
        JButton b = new JButton("设置");
        b.setBounds(800, 730, 75, 40);
        f.add(b);
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String answer = JOptionPane.showInputDialog(f, "请输入数字，表明当前帧的延迟时间");
                try{
                    int anInt = Integer.parseInt(answer);
                    L1.setText("点击设置当前帧延的延迟时间： "+answer+" ms");
                    ledSetting.setTime(answer);
                }catch (Exception ep){
                    JOptionPane.showMessageDialog(f, "输入的数据有误！");
                }

            }
        });
    }

    public static void markBtn(JFrame f, int x, int y, int index, String[] colorList) {
        String LabelDEFAULTEXT = String.format("%02x,%02x,%02x",0,0,0);

        JButton b = new JButton("灯"+(index+1));
        JLabel L1 = new JLabel(LabelDEFAULTEXT);
        if(!colorList[index].equals("0")){
            L1.setText(colorList[index]);
        }

        b.setBounds(x, y, 75, 40);
        L1.setBounds(x + 5, y - 15, 65, 15);
        L1.setOpaque(true);
        L1.setHorizontalAlignment(JLabel.CENTER);  // 居中对其
        L1.setVerticalAlignment(JLabel.CENTER);

        f.add(b);
        f.add(L1);
        b.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // 显示颜色选取器对话框, 返回选取的颜色（线程将被阻塞, 直到对话框被关闭）
                Color color = JColorChooser.showDialog(f, "选取颜色", null);
                if (color == null) {  // 如果用户取消或关闭窗口, 则返回的 color 为 null
                    return;
                }
                L1.setBackground(color);  // 把选取的颜色设置为标签的背景
                L1.setText(String.format("%02x,%02x,%02x", color.getRed(), color.getGreen(), color.getBlue()));  // 获取颜色的 ARGB 各个分量值
                colorList[index] = String.format("%02x%02x%02x", color.getRed(), color.getGreen(), color.getBlue());
            }
        });
    }

}
