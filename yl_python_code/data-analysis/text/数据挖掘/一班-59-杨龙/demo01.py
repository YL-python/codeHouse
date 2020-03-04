import xlrd
from matplotlib import pyplot as plt
from matplotlib import font_manager

# 学号列表
stu_id = list()
# 身高列表
stu_height = list()
# 体重列表
stu_weight = list()
# 支出列表
stu_expend = list()

my_font1 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=12)
my_font2 = font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf', size=25)


# get_data方法用来读取数据
def get_data():
    # 打开文件
    data_xlsx = xlrd.open_workbook("BSdata.xlsx")
    # 进入第一张表
    sheet1 = data_xlsx.sheets()[0]
    # 获取总行数 53
    sheet1_rows = sheet1.nrows
    # 获取总列数 8
    # sheet1_cols = sheet1.ncols
    for i in range(1, sheet1_rows):
        stu_id.append(str(int(sheet1.cell(i, 0).value)))
        stu_height.append(int(sheet1.cell(i, 2).value))
        stu_weight.append(int(sheet1.cell(i, 3).value))
        stu_expend.append(sheet1.cell(i, 4).value)


# 展示身高数据的方法
def show_height():
    plt.figure('直方图', figsize=(20, 8), dpi=80)
    bin_width = 3
    plt.hist(stu_height, range(min(stu_height), max(stu_height) + bin_width, bin_width), density=0)
    plt.xticks(range(min(stu_height), max(stu_height) + bin_width, bin_width))
    plt.xlabel('身高(单位：cm)', fontproperties=my_font1)
    plt.ylabel('人数', fontproperties=my_font1)
    plt.title('身高数据分布情况', fontproperties=my_font1)
    plt.grid(alpha=0.4, linestyle=':')
    plt.show()


# 展示体重数据的方法
def show_weight():
    plt.figure('直方图', figsize=(20, 8), dpi=80)
    bin_width = 3
    plt.hist(stu_weight, range(min(stu_weight), max(stu_weight) + bin_width, bin_width), density=0)
    plt.xticks(range(min(stu_weight), max(stu_weight) + bin_width, bin_width))
    plt.xlabel('体重(单位：Kg)', fontproperties=my_font1)
    plt.ylabel('人数', fontproperties=my_font1)
    plt.title('体重数据分布情况', fontproperties=my_font1)
    plt.grid(alpha=0.4, linestyle=':')
    plt.show()


# 展示支出数据的方法
def show_expend():
    plt.figure('条形图', figsize=(20, 10), dpi=80)
    plt.barh(range(len(stu_id)), stu_expend, height=0.3, color='cyan')
    plt.title('每个人的支出情况', fontproperties=my_font2)
    plt.xlabel('支出', fontproperties=my_font2)
    plt.ylabel('学号', fontproperties=my_font2)
    plt.yticks(range(len(stu_id)), stu_id, fontproperties=my_font1)
    plt.grid(alpha=0.4, linestyle=':')
    plt.show()


# 入口
def main():
    get_data()
    print("输入数字查看图表\n1:查看身高关系图表, 2:查看体重关系图表, 3:查看支出关系图表\n请输入:")
    num = int(input())
    if num == 1:
        show_height()
    elif num == 2:
        show_weight()
    elif num == 3:
        show_expend()
    else:
        print("输入的数据有误！")


if __name__ == '__main__':
    main()
