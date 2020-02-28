package main.java.Swing.LED;

import javax.swing.*;

public class LEDOneSetting { // 这个类用来设置每一帧  会返回一个ledsetting对象
    public LEDSetting SetOnePage(JFrame f){
        LEDSetting ledSetting = new LEDSetting();
        // 加载多个按钮
        LEDLoadingBtn ledLoadingBtn = new LEDLoadingBtn();
        ledLoadingBtn.showBtn(f,ledSetting);  // 加载30个按钮
        ledLoadingBtn.showTimeText(f, ledSetting);  // 设置时间
        return ledSetting;
    }
}
