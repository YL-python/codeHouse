package main.java.Swing.demo;

import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JTextField;
import javax.swing.filechooser.FileFilter;

public class demo13_案例_文件复制进度条 {
    public static long Size = 0;
    public static long srcSize = 0;
    public static long destSize = 0;
    public static String srcStr = null;
    public static String destStr = null;

    public static void main(String[] args) throws IOException {
        JFrame jf = new JFrame("复制文件");
        jf.setSize(350, 200);
        jf.setLayout(new GridLayout(3, 1));
        // 设置窗口相对于指定组件的位置。  null，则此窗口将置于屏幕的中央。
        jf.setLocationRelativeTo(null);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 地址  面板
        JPanel jp1 = new JPanel();

        jp1.setLayout(new GridLayout(2, 3));
        JLabel jb1 = new JLabel("原文件地址");
        JTextField jf1 = new JTextField();
        JLabel jb2 = new JLabel("目标地址");
        JTextField jf2 = new JTextField();
        // 原文件选择器
        JFileChooser jcs = new JFileChooser();

//        设置只选择文件、只选择目录，或者可选择文件和目录
        jcs.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);

        jcs.setFileFilter(new FileFilter() {
            @Override
            public String getDescription() {
                // TODO Auto-generated method stub
                return "";
            }
            @Override
            public boolean accept(File f) {
                // TODO Auto-generated method stub
                return true;
            }
        });

        JButton jbChoose = new JButton("选择文件");
        jbChoose.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub

                //null———当前电脑显示器屏幕的中央
                //this———当前你编写的程序屏幕中央
                int result = jcs.showOpenDialog(null);

                if (result == JFileChooser.APPROVE_OPTION) {
                    srcStr = jcs.getSelectedFile().getAbsolutePath();
                    if (srcStr != null)
                        jf1.setText(srcStr);

                }
            }
        });
        // 目标位置文件选择器
        JFileChooser jcs1 = new JFileChooser();
        jcs1.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        JButton jbChoose1 = new JButton("选择位置");
        jbChoose1.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                int result = jcs1.showOpenDialog(null);
                if (result == JFileChooser.APPROVE_OPTION) {
                    destStr = jcs1.getSelectedFile().getAbsolutePath();
                    if (destStr != null)
                        jf2.setText(destStr);
                }
            }
        });
        jp1.add(jb1);
        jp1.add(jf1);
        jp1.add(jbChoose);
        jp1.add(jb2);
        jp1.add(jf2);
        jp1.add(jbChoose1);
        jf.add(jp1);
        // 开始复制
        JPanel jp2 = new JPanel();
        JButton jbt = new JButton("开始复制");
        jp2.setLayout(new FlowLayout());
        jp2.add(jbt);
        jf.add(jp2);
        // 进度条
        JPanel jp3 = new JPanel();
        JProgressBar jpb = new JProgressBar();
        jpb.setMaximum(100);
        jpb.setStringPainted(true);
        jp3.add(jpb);
        jf.add(jp3);
        jf.setVisible(true);

        jbt.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                // TODO Auto-generated method stub
                jbt.setText("正在复制");
                jpb.setValue(0);
                srcStr = jf1.getText();
                destStr = jf2.getText();
                Size = 0;
                srcSize = 0;
                Thread t2 = new Thread() {  // 复制文件的线程
                    public void run() {
                        try {
                            CopyFolder(srcStr, destStr);
                        } catch (IOException e) {
                            // TODO Auto-generated catch block
                            e.printStackTrace();
                        }
                    }
                };
                t2.start();
                Thread t1 = new Thread() {  // 进度条显示的线程
                    public void run() {
                        srcSize = getFolderSize(srcStr);
                        jbt.setEnabled(false);
                        jbChoose.setEnabled(false);
                        jbChoose1.setEnabled(false);
                        while (true) {
                            Size = 0;
                            destSize = getFolderSize(destStr + "/" + srcStr.substring(srcStr.lastIndexOf("\\")));
                            jpb.setValue((int) (destSize == 0 ? 0 : destSize * 100 / srcSize));
                            if (destSize == srcSize) {
                                JOptionPane jop = new JOptionPane("完成");
                                jop.showMessageDialog(jf, "复制完成！");
                                jbt.setText("开始复制");
                                jbt.setEnabled(true);
                                jbChoose.setEnabled(true);
                                jbChoose1.setEnabled(true);
                                break;
                            }
                        }
                    }
                };
                t1.start();

            }
        });
    }

    public static void CopyFolder(String srcStr, String destStr) throws IOException {
        File Folder = new File(srcStr);
        if (Folder.isDirectory()) {
            File[] files = Folder.listFiles();
            destStr = destStr + "/" + Folder.getName();
            File destFolder = new File(destStr);
            destFolder.mkdir();
            for (File file : files) {
                if (file.isDirectory()) {
                    CopyFolder(file.getAbsolutePath(), destFolder.toString());
                } else {
                    File destFile = new File(destStr + "/" + file.getName());
                    copyFile(file, destFile);
                }
            }
        } else {
            File destFile = new File(destStr + "/" + Folder.getName());
            copyFile(Folder, destFile);
        }
    }
    public static void copyFile(File file,File destFile) throws IOException {
        destFile.createNewFile();  //
        FileInputStream fis = new FileInputStream(file);
        BufferedInputStream bis = new BufferedInputStream(fis);
        FileOutputStream fos = new FileOutputStream(destFile);

        BufferedOutputStream bos = new BufferedOutputStream(fos);
        String content = null;
        byte[] srcByte = new byte[(int) file.length()];
        bis.read(srcByte);
        bos.write(srcByte);
        bis.close();
        fis.close();
        bos.close();
        fos.close();
    }
    public static long getFolderSize(String Address) {
        File file = new File(Address);
        if (!file.exists()) {
            return 0;
        }
        if (file.isFile()) {
            Size = file.length();
            return Size;
        }
        File[] files = file.listFiles();
        for (File f : files) {
            if (f.isDirectory()) {
                getFolderSize(f.getAbsolutePath());
            } else {
                Size += f.length();
            }
        }
        return Size;
    }
}
