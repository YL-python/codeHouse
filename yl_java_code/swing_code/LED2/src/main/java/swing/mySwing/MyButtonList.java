package main.java.swing.mySwing;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JColorChooser;

public class MyButtonList {
	public JButton jbtn;
	public Color color;
	MySwing mySwing;
	int i;

	public MyButtonList(MySwing mySwing, JButton jbtn, int i) {
		setJbtn(jbtn);
		this.mySwing = mySwing;
		this.i = i;
	}

	public void setColor() {
		this.jbtn.setBackground(new Color(0));
	}

	public void setJbtn(JButton jbtn) {
		this.jbtn = jbtn;
		setColor();
		jbtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				color = JColorChooser.showDialog(mySwing.f, "选取颜色", null);
				if (color == null) {
					// 如果用户取消或关闭窗口, 则返回的 color 为 null
					return;
				}
				setColor(i, color);
				/*
				 * mySwing.ledDao.colorList[i] = String.format( "%02x%02x%02x", color.getRed(),
				 * color.getGreen(), color.getBlue()); mySwing.ledDao.colors[i] = color ;
				 */
			}
		});
	}

	public void setColor(int i, Color color) {
		this.jbtn.setBackground(color);
		mySwing.ledDao.colorList[i] = String.format("%02x%02x%02x", color.getRed(), color.getGreen(), color.getBlue());
		mySwing.ledDao.colors[i] = color;

	}

	public void setBound(int x, int y) {
		jbtn.setBounds(x, y, 20, 20);
		mySwing.f.add(jbtn);
	}
}
