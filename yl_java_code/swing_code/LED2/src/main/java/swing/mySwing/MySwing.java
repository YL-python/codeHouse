package main.java.swing.mySwing;

import java.awt.Color;
import java.awt.Font;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Map;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

import main.java.swing.event.LastEvent;
import main.java.swing.event.NextEvent;
import main.java.swing.event.SaveEvent;
import main.java.swing.event.SleepEvent;
import main.java.swing.vo.LedDao;

public class MySwing {
	BufferedReader buf ;
	OutputStream output ;
	public Map<String,LedDao> mapLedDao ;
	public LedDao ledDao ;
	public JFrame f;
	public MySwing() {
		mapLedDao =new HashMap<String,LedDao>() ;
		ledDao = new LedDao() ;
		f = new JFrame("流水灯");
		f.setSize(1200, 1000);
		// 主窗体设置位置
		f.setLocationRelativeTo(null);
		// 主窗体中的组件设置为绝对定位
		f.setLayout(null);
		// 加载设置第 "+index+" 帧
		centerLabel(1);
		//加载功能按钮
		setButtonMain() ;
		showBtn() ;
		showTimeText() ;
		// 加载界面的方法...
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		// 让窗体变得可见
		f.setVisible(true);
		// 窗体大小不可变
		f.setResizable(false);
	}

	public int index = 1 ; //正在设置第 "+index+"帧
	private JLabel L1;
	public void centerLabel(int index) {
		L1 = new JLabel() ;
		if (index<=0) {
			index = 1 ;
		}
		setLabel1Test() ;
		L1.setBounds(510, 50, 200, 35);
		L1.setFont(new Font(Font.DIALOG, Font.BOLD, 25));
		f.add(L1);
	}
	public void setLabel1Test() {
		L1.setText("正在设置第 "+(index) +" 帧");
	}
	JButton jButtonLast ;
	JButton jButtonNext ;
	JButton jButtonOver ;
	public void setButtonMain() {
		jButtonLast = new JButton("上一帧");
		jButtonLast.setBounds(220, 800, 180, 35);
		f.add(jButtonLast);
		jButtonLast.addActionListener(new LastEvent(this));
		jButtonNext = new JButton("下一帧");
		jButtonNext.setBounds(800, 800, 180, 35);
		jButtonNext.addActionListener(new NextEvent(this));
		f.add(jButtonNext);
		jButtonOver = new JButton("生成文件");
		jButtonOver.setBounds(510, 800, 180, 35);
		f.add(jButtonOver);
		jButtonOver.addActionListener(new SaveEvent(this));
	}

	public MyButtonList myButtonList[] ;
	Color color ;
	public void showBtn() {
		int i = 0;
		myButtonList = new MyButtonList[30] ;
		int[] xList = {560,640,720,800,880,960,1040,1060,1060,1040,960,880,800,720,640,560,480,400,320,240,160,80,60,60,80,160,240,320,400,480};
		int[] yList = {220,165,110,55,55,110,165,220,275,330,385,440,495,550,605,660,605,550,495,440,385,330,275,220,165,110,55,55,110,165};
		for (i = 0; i <30; i++) {
			myButtonList[i] = new MyButtonList(this, new JButton(""+(i+1)),i) ;
			myButtonList[i].setBound(xList[i], yList[i]);
		}
	}
	public JLabel jLabel_Time ;
	public void setJLabel_Time(int sleepTime) {
		jLabel_Time.setText("点击设置当前帧延的延迟时间： "
				+sleepTime+" ms");
	}
	public void showTimeText(){
		jLabel_Time = new JLabel();
		jLabel_Time.setText("点击设置当前帧延的延迟时间： "
				+ledDao.getTime()+" ms");
		jLabel_Time.setBounds(300, 730, 480, 35);
		jLabel_Time.setFont(new Font(Font.DIALOG, Font.BOLD, 25));
		f.add(jLabel_Time);
		JButton b = new JButton("设置");
		b.setBounds(800, 730, 75, 40);
		f.add(b);
		b.addActionListener(new SleepEvent(this));
    }
};