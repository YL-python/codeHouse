"""
2019年8月25日16点59分
用到了  nan不等于nan   和布尔索引
遍历每一列（for循环和赋值）  记录这一列有没有nan并判断   有的话先取出不是nan的数据 计算平均值然后赋值给是nan的数据
"""
import numpy as np


def nantomean(t1):
    for i in range(t1.shape[1]):  # 遍历每一列
        temp_col = t1[:, i]  # 当前一列
        nan_num = np.count_nonzero(temp_col != temp_col)  # 判断这一列有没有nan
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 找出不是nan的数据
            temp_mean = temp_not_nan_col.mean()  # 计算不含nan的平均值
            temp_col[np.isnan(temp_col)] = temp_mean  # 把平均值赋给 是nan的地方
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype('float')
    t1[1, 2:] = np.nan
    print(t1)
    t1 = nantomean(t1)
    print(t1)
