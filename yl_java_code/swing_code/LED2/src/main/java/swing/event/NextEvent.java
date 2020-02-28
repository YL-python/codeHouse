package main.java.swing.event;

import main.java.swing.mySwing.MySwing;
import main.java.swing.tools.MapTools;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class NextEvent implements ActionListener {
	MySwing mySwing;
	public NextEvent(MySwing mySwing) {
		this.mySwing = mySwing;
	}
	public void actionPerformed(ActionEvent e) {
		System.out.println("��һ�������Է���Map�е�����\n"+mySwing.ledDao.toString());
		mySwing.mapLedDao.put("" + mySwing.index, mySwing.ledDao);
		mySwing.index+=1;
		mySwing.setJLabel_Time(mySwing.ledDao.getTime());
		//mySwing
		try {
			mySwing.ledDao = MapTools.getLedDao(mySwing.mapLedDao, ""+mySwing.index);
		} catch (Exception e2) {
			System.out.println("mySwing.ledDaoΪ�ա�ԭ��:" + e2.getMessage());
		}
		try {
			for (int i = 0; i < 30; i++) {
				mySwing.myButtonList[i].setColor(i,mySwing.ledDao.colors[i]);
			}
		} catch (Exception e2) {
			e2.printStackTrace();
		}




		// mySwing.ledDao��ֵ����
		// System.out.println(mySwing.mapLedDao.keySet());
		// ����ledDao�е�����colors�Ƿ�ֵ�ɹ�
		/*
		 * for(int i=0;i<30;i++) { System.out.print(i+":");
		 * System.out.println(String.format("%02x%02x%02x",
		 * mySwing.ledDao.colors[i].getRed(), mySwing.ledDao.colors[i].getGreen(),
		 * mySwing.ledDao.colors[i].getBlue())); }
		 */
		//mySwing.ledDao = new LEDDao();
	}

};