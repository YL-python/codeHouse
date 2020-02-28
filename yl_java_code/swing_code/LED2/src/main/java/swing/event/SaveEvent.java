package main.java.swing.event;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import main.java.swing.mySwing.MySwing;

public class SaveEvent implements ActionListener {
	MySwing mySwing ;
	public SaveEvent(MySwing mySwing) {
		this.mySwing = mySwing ;
	}

	public void actionPerformed(ActionEvent e) {
		

	}

}
