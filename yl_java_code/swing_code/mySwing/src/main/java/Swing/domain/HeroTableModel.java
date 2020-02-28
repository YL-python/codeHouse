package main.java.Swing.domain;

import javax.swing.table.AbstractTableModel;

public class HeroTableModel extends AbstractTableModel {
    String[] columnNames = new String[] { "id", "name", "hp", "damage" };
    public String[][] heros = new String[][] { { "1", "盖伦", "616", "100" },
            { "2", "提莫", "512", "102" }, { "3", "奎因", "832", "200" } };

    // 返回一共有多少行
    public int getRowCount() {
        // TODO Auto-generated method stub
        return heros.length;
    }

    // 返回一共有多少列
    public int getColumnCount() {
        // TODO Auto-generated method stub
        return columnNames.length;
    }

    // 获取每一列的名称
    public String getColumnName(int columnIndex) {
        // TODO Auto-generated method stub
        return columnNames[columnIndex];
    }

    // 单元格是否可以修改
    public boolean isCellEditable(int rowIndex, int columnIndex) {
        return false;
    }

    // 每一个单元格里的值
    public Object getValueAt(int rowIndex, int columnIndex) {
        // TODO Auto-generated method stub
        return heros[rowIndex][columnIndex];
    }
}
