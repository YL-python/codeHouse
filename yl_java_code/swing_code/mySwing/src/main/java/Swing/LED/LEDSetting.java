package main.java.Swing.LED;

import java.util.Arrays;

public class LEDSetting {
    private String[] colorList={"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"};
    private String time = "0";

    public String[] getColorList() {
        return colorList;
    }

    public void setColorList(String[] colorList) {
        this.colorList = colorList;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    @Override
    public String toString() {
        return "LEDSetting{" +
                "colorList=" + Arrays.toString(colorList) +
                ", time='" + time + '\'' +
                '}';
    }
}
