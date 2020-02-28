package main.java.swing.event;

import main.java.swing.mySwing.MySwing;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JOptionPane;

public class SleepEvent implements ActionListener {
	MySwing mySwing ;
	public SleepEvent(MySwing mySwing) {
		this.mySwing = mySwing ;
	}
	public void actionPerformed(ActionEvent arg0) {
		String answer = JOptionPane.showInputDialog(
				mySwing.f, "请输入数字，表明当前帧的延迟时间");
        try {
			mySwing.ledDao.time = Integer.parseInt(answer) ;
		} catch (Exception e) {
			JOptionPane.showMessageDialog(mySwing.f, "输入的数据有误！");
		}
		mySwing.jLabel_Time.setText("点击设置当前帧延的延迟时间： "
				+mySwing.ledDao.getTime()+" ms");
	}
};
