package main.java.swing.event;

import main.java.swing.mySwing.MySwing;
import main.java.swing.tools.MapTools;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class LastEvent implements ActionListener {
	MySwing mySwing ;
	public LastEvent(MySwing mySwing) {
		this.mySwing = mySwing ;
	}
	public void actionPerformed(ActionEvent e) {
		if (mySwing.index-1<=0) {
			return ;
		}
		//System.out.println(mySwing.index+"上一个,测试放入Map中的数据\n"+mySwing.ledDao.toString());
		mySwing.mapLedDao.put(""+mySwing.index, mySwing.ledDao) ;
		mySwing.index-=1 ;
		mySwing.setLabel1Test();
		try {
			mySwing.ledDao = MapTools.getLedDao(mySwing.mapLedDao,
												""+mySwing.index) ;
		} catch (Exception e2) {
			System.out.println("mySwing.ledDao为空。原因:"
					+e2.getMessage());
		}
		Color color = new Color(0);
		for(int i=0;i<30;i++) {
			color = mySwing.ledDao.colors[i];
			mySwing.myButtonList[i].setColor(i,color);
		}
	}

}
