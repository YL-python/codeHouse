from matplotlib import pyplot as plt
from matplotlib import font_manager

# 大小和字体信息
my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=8)
my_font2 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=18)
plt.figure('散点图',figsize=(20,8),dpi=80)

# 数据
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_3=range(1,32)
x_10=range(51,82)

#绘制
plt.scatter(x_3,y_3,label="三月")
plt.scatter(x_10,y_10,label='十月')

# 信息
plt.title('三月和十月的温度变化',fontproperties=my_font2)
plt.xlabel('日期',fontproperties=my_font2)
plt.ylabel('温度',fontproperties=my_font2)

#单位长度
_x = list(x_3)+list(x_10)
_x_3 = ['{}号'.format(i) for i in x_3]
_x_10 = ['{}号'.format(i-50) for i in x_10]
_x_label = _x_3+_x_10
_y_label = range( min(min(y_3), min(y_10)), max( max(y_3), max(y_10))+2 )
plt.xticks(_x,_x_label,fontproperties=my_font1,rotation=45)
plt.yticks(_y_label,fontproperties=my_font1)

# 网格
plt.grid(alpha=0.4,linestyle=':')

# 显示图例
plt.legend(prop=my_font2)

#显示图像
plt.show()