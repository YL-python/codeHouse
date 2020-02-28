package main.java.Swing.demo;

import javax.swing.*;

//
public class demo14_记事本 {
    public static void main(String[] args) {
        JFrame f = new JFrame("记事本");
        f.setSize(500, 300);
        f.setLocation(300, 400);
        f.setLayout(null);

        JMenuBar mb = new JMenuBar();

        JMenu mFile = new JMenu("文件(F)");
        mFile.add(new JMenuItem("新建(N)   Ctrl+N"));
        mFile.add(new JMenuItem("打开(O)…   Ctrl+O"));
        mFile.add(new JMenuItem("保存(S)   Ctrl+S"));
        mFile.add(new JMenuItem("另存为(A)…"));
        mFile.addSeparator();
        mFile.add(new JMenuItem("页面设置(U)…"));
        mFile.add(new JMenuItem("打印(P)   Ctrl+P"));
        mFile.addSeparator();
        mFile.add(new JMenuItem("退出(X)"));

        JMenu mEdit = new JMenu("编辑(E)");
        mEdit.add(new JMenuItem("撤销(U)   Ctrl+Z"));
        mEdit.addSeparator();
        mEdit.add(new JMenuItem("剪切(T)   Ctrl+X"));
        mEdit.add(new JMenuItem("复制(C)   Ctrl+C"));
        mEdit.add(new JMenuItem("粘贴(V)   Ctrl+V"));
        mEdit.add(new JMenuItem("删除(L)   Del"));
        mEdit.addSeparator();
        mEdit.add(new JMenuItem("使用Bing搜索…   Ctrl+E"));
        mEdit.add(new JMenuItem("查找(F)…   Ctrl+F"));
        mEdit.add(new JMenuItem("查找下一个(N)   F3"));
        mEdit.add(new JMenuItem("替换(R)   Ctrl+H"));
        mEdit.add(new JMenuItem("转到(G)   Ctrl+G"));
        mEdit.addSeparator();
        mEdit.add(new JMenuItem("全选(A)   Ctrl+A"));
        mEdit.add(new JMenuItem("时间/日期(D)   F5"));

        JMenu mFormat = new JMenu("格式(O)");
        mFormat.add(new JMenuItem("自动换行(W)"));
        mFormat.add(new JMenuItem("字体(F)…"));

        JMenu mLookup = new JMenu("查看(V)");
        mLookup.add(new JMenuItem("缩放(Z)"));
        mLookup.add(new JMenuItem("状态栏(S)"));

        JMenu mHelp = new JMenu("帮助(H)");
        mHelp.add(new JMenuItem("查看帮助(H)"));
        mHelp.addSeparator();
        mHelp.add(new JMenuItem("关于记事本(A)"));

        mb.add(mFile);
        mb.add(mEdit);
        mb.add(mFormat);
        mb.add(mLookup);
        mb.add(mHelp);

        f.setJMenuBar(mb);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
