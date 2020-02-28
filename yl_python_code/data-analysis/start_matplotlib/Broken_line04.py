from matplotlib import pyplot as plt
from matplotlib import font_manager

# 图形大小和字体参数
plt.figure(num='折线图',figsize=(20,8),dpi=80)  #源码说 第一个参数num传字符串就会变成标题
my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=20)
my_font2 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf',size=26)

# 数据
x = range(11,31)
y_1 = [1,2,3,2,3,4,3,4,5,4,5,6,5,6,7,6,7,8,7,8]
y_2 = [5,6,7,5,4,3,2,5,7,3,6,7,3,7,3,7,3,2,4,1]

# 绘制
plt.plot(x,y_1,label='自己',color='cyan',linestyle=':',linewidth='3',alpha=1)   # 看源码呀
plt.plot(x,y_2,label='别人',color='orange',linestyle='--',linewidth='5',alpha=0.4)

# 单位长度
_x_label = ['{}岁'.format(i) for i in x]
_y_label = [i/2 for i in range(min(y_1),2*max(y_2)+1)]
plt.xticks(x,_x_label,rotation=45, fontproperties=my_font1)
plt.yticks(_y_label)

# 信息
plt.xlabel('年龄',fontproperties=my_font1)
plt.ylabel('某变化',fontproperties=my_font1)
plt.title('展示',fontproperties=my_font2)
plt.text(20, 4, r'\mu=100,\ \sigma=15$')    #文本中注释

# 网格
plt.grid(alpha=0.7,linestyle=':')   # alpha 透明度 [0,1]

# 添加图例  辅助绘制时候的Label参数
plt.legend(prop=my_font1, loc=0)   # 添加图例传字体参数用 prop   只有这里是prop    loc位置参数
# ['upper left', 'upper center', 'upper right','center left', 'center', 'center right', 'best', 'right', 'lower left', 'lower center', 'lower right']
# ['左上角'，     '上中间'，        '右上角'，     '左中'，        '中间'，   '右中'，         '最佳'， '右'，    '左下角'，    '下中'，         '下右']
# 2  9  1            0 默认最佳位置
# 6  10 5/7
# 3  8  4

plt.show()

# manager   管理
# Properties   属性
# ticks   文本上的钩号
# grid   网格
# legend   说明
# rotation   旋转
# figure   图形