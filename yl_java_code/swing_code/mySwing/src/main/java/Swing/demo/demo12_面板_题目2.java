package main.java.Swing.demo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;

//参考eclipse的风格，借助TabbedPanel显示一个包下所有的java文件
public class demo12_面板_题目2 {
    public static void main(String[] args) {
        JFrame f = new JFrame("eclipse");
        f.setSize(900, 600);
        f.setLocation(200, 50);
        f.setLayout(null);
        //打开文件并获取文件数量
        File file = new File("D:\\Intellij_IDEA\\mySwing\\src\\main\\java\\Swing");
        //以文件数组的形式，返回当前文件夹下的所有文件（不包含子文件及子文件夹）
        File[] files = file.listFiles();
        int len = files.length;
        JTabbedPane tp = new JTabbedPane();
        tp.setSize(f.getWidth(), f.getHeight());

        for (int i = 0; i < len; i++) {
            File temp = files[i];
            JPanel p = new JPanel();
            p.setLayout(new BorderLayout());

            try (
                    Reader r = new FileReader(temp);
                    BufferedReader br = new BufferedReader(r);
            ) {
                JTextArea ta = new JTextArea();
                ta.setSize(p.getWidth(), p.getHeight());
                String line;
                while ((line = br.readLine()) != null) {
                    ta.append(line);
                    ta.append("\n");
                }
                JScrollPane sp = new JScrollPane(ta);
                p.add(sp, BorderLayout.CENTER);
            } catch(FileNotFoundException e) {
                e.printStackTrace();
            } catch (IOException e1) {
                e1.printStackTrace();
            }


            tp.add(p);
            tp.setTitleAt(i, temp.getName());
        }

        f.setContentPane(tp);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
