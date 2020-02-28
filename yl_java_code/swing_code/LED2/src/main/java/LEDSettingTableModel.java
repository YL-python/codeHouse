package main.java;

import javax.swing.table.AbstractTableModel;

public class LEDSettingTableModel extends AbstractTableModel {
    String[] columnNames = new String[] { "帧", "灯的情况", "延迟时间"};
    String[][] leds = {  };


    // 返回一共有多少行
    @Override
    public int getRowCount() {
        return leds.length;
    }

    // 返回一共有多少列
    @Override
    public int getColumnCount() {
        return columnNames.length;
    }

    // 每一个单元格里的值
    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        return leds[rowIndex][columnIndex];
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
}
