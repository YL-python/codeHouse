package main.java.Swing.demo;

import javax.swing.*;

//
public class demo14_菜单栏 {
    public static void main(String[] args) {
        JFrame f = new JFrame("LoL");
        f.setSize(400, 300);
        f.setLocation(200, 200);

        // 菜单栏
        JMenuBar mb = new JMenuBar();

        // 菜单
        JMenu mHero = new JMenu("英雄");
        JMenu mItem = new JMenu("道具");
        JMenu mWord = new JMenu("符文");
        JMenu mSummon = new JMenu("召唤师");
        JMenu mTalent = new JMenu("天赋树");

        // 把菜单加入到菜单栏
        mb.add(mHero);
        mb.add(mItem);
        mb.add(mWord);
        mb.add(mSummon);
        mb.add(mTalent);

        // 把菜单栏加入到frame，这里用的是set而非add
        f.setJMenuBar(mb);

        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.setVisible(true);
    }
}
