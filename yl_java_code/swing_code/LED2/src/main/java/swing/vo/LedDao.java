package main.java.swing.vo;

import java.awt.Color;
import java.util.Arrays;

public class LedDao {
	public String[] colorList = { "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
			"0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" };
	public int time = 100 ;
	public int getTime() {
		return time;
	}
	public void setTime(int time) {
		this.time = time;
	}
	public Color[] colors ;
	
	public LedDao() {
		colors = new Color[30] ;
		for (int i = 0; i < colors.length; i++) {
				colors[i] = new Color(0) ;
		}
	}
	
	public String[] getColorList() {
		return colorList;
	}

	public void setColorList(String[] colorList) {
		this.colorList = colorList;
	}
	public String toString() {
		return "LEDSetting{" + "colorList=" + Arrays.toString(colorList) + ", time='" + time + '\'' + '}';
	}
}
