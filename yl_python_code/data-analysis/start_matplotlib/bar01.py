# 发现字符串太长不好看

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=12)
my_font2 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=18)
plt.figure('条形图', figsize=(20, 10), dpi=80)

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：\n最后的骑士", "摔跤吧！爸爸", "加勒比海盗5：\n死无对证", "金刚：骷髅岛", "极限特工：\n终极回归",
     "生化危机6：\n终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3：\n殊死一战", "蜘蛛侠：\n英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊", ]

b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

plt.bar(range(len(a)), b, width=0.3, color='cyan')

plt.title('票房对比', fontproperties=my_font2)
plt.xlabel('影片', fontproperties=my_font2)
plt.ylabel('票房（亿）', fontproperties=my_font2)

plt.xticks(range(len(a)), a, fontproperties=my_font1, rotation=90)

plt.grid(alpha=0.4, linestyle=':')

plt.show()
