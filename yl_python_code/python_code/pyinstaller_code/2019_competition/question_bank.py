import read_code
import tkinter as tk
from tkinter import messagebox

SHUJU_NUM = 1
DATA = None
tihao_list = read_code.get_nrows()
min_tihao = tihao_list[1]
max_tihao = tihao_list[-1]
print(max_tihao)
error_timu = []
try:
    with open(r'WrongTopic.txt', 'r', encoding='utf-8') as fpr:
        error_timu = fpr.read()
        error_timu = error_timu.replace('[', '')
        error_timu = error_timu.replace(']', '')
        error_timu = error_timu.split(',')
        error_timu = [eval(i) for i in error_timu]
except:
    pass


# 获取数据函数
def get_data(num):
    data = read_code.read_file(num)
    return data


root = tk.Tk()
root.title('信息计数大赛题库--question bank-- 18-大数据-杨龙')


# 设置主窗口居中显示
def center_window(window, width, height):
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size = '%dx%d+%d+%d' % (
        width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size)


center_window(root, 700, 430)
root.resizable(0, 0)


# 功能实现函数
# 填充数据
def fill_data():
    global DATA
    DATA = get_data(SHUJU_NUM)
    ans_label_var.set('稳住，我们能对')
    tihao_var.set('题号:{}'.format(int(DATA[0])))
    timu_text.config(state=tk.NORMAL)
    timu_text.delete(0.0, 'end')
    timu_text.insert('insert', DATA[2])
    timu_text.config(state=tk.DISABLED)

    A_text.config(state=tk.NORMAL)
    A_text.delete(0.0, 'end')
    A_text.insert('insert', DATA[3])
    A_text.config(state=tk.DISABLED)

    B_text.config(state=tk.NORMAL)
    B_text.delete(0.0, 'end')
    B_text.insert('insert', DATA[4])
    B_text.config(state=tk.DISABLED)

    C_text.config(state=tk.NORMAL)
    C_text.delete(0.0, 'end')
    C_text.insert('insert', DATA[5])
    C_text.config(state=tk.DISABLED)

    D_text.config(state=tk.NORMAL)
    D_text.delete(0.0, 'end')
    D_text.insert('insert', DATA[6])
    D_text.config(state=tk.DISABLED)

    tiaoz_entry.delete(0,'end')


# 下一题按钮
def click_next_button():
    global SHUJU_NUM
    if SHUJU_NUM + 1 > tihao_list.index(max_tihao):
        tk.messagebox.showinfo(title='提醒', message='这里是最后一题啦')
    else:
        SHUJU_NUM += 1
        fill_data()


# 上一题按钮
def click_last_button():
    global SHUJU_NUM
    if SHUJU_NUM - 1 < min_tihao:
        tk.messagebox.showerror('错误', '题目看多了脑袋瓜子嗡嗡的了把\n这样操作不对哦')
    else:
        SHUJU_NUM -= 1
        fill_data()


# 选择答案按钮
def click_ABCD():
    return ABCD_var.get()


# 添加错题库功能
def click_error_button():
    global error_timu
    ans_label_var.set('又多了一道错题')
    error_timu.append(DATA[0])
    error_timu = list(set(error_timu))
    with open(r'WrongTopic.txt', 'w', encoding='utf-8') as fpw:
        fpw.write(str(error_timu))


# 打开错题库
def click_open_error_button():
    global error_timu
    text_error = str(error_timu).replace('.0', '')
    text_error = text_error.replace('[', '')
    text_error = text_error.replace(']', '')
    text = '错误的题号:' + text_error + ''
    tk.messagebox.showinfo(title='错题库', message=text)


# 点击确定按钮
def click_ans_button():
    ans = click_ABCD()
    if ans == DATA[7]:
        ans_label_var.set('答对啦(ง •_•)ง')
    else:
        ans_label_var.set('答错了(ಥ _ ಥ)')


# 跳转功能
def click_tiaoz():
    global SHUJU_NUM
    str_num = tiaoz_entry.get()
    eval_num = float(eval(str_num))
    if eval_num > max_tihao or eval_num < min_tihao:
        tk.messagebox.showerror('错误', '题号输入有误呀')
    elif eval_num not in tihao_list:
        text = '比赛题目数据有缺失，你输入的题号的数据刚好丢失啦'
        tk.messagebox.showinfo(title='提醒', message=text)
    else:
        SHUJU_NUM = tihao_list.index(eval_num)
        fill_data()


# 题号 标题 跳转功能
tihao_var = tk.StringVar()
tihao_label = tk.Label(root, textvariable=tihao_var, font=20)
tihao_label.place(x=10, y=0)
biaoti_label = tk.Label(root, text='请开始你的表演', font=20)
biaoti_label.place(x=250, y=0)
tiaoz_entry = tk.Entry(root, width=7, font=20)
tiaoz_entry.place(x=520, y=5)
tiaoz_button = tk.Button(root, text='跳转', font=('', 15), command=click_tiaoz)
tiaoz_button.place(x=620, y=0)

# 显示题目
timu_text = tk.Text(root, height=5, width=50, font=('', 20))
timu_text.place(x=0, y=40)

# 显示ABCD四个选项
ABCD_var = tk.StringVar()
radio_A = tk.Radiobutton(root, text='A:', value='A', font=20,
                         variable=ABCD_var, command=click_ABCD)
radio_A.place(x=10, y=180)
A_text = tk.Text(root, height=6, width=20, font=('', 12))
A_text.place(x=63, y=185)

radio_B = tk.Radiobutton(root, text='B:', value='B', font=20,
                         variable=ABCD_var, command=click_ABCD)
radio_B.place(x=250, y=180)
B_text = tk.Text(root, height=6, width=20, font=('', 12))
B_text.place(x=303, y=185)

radio_C = tk.Radiobutton(root, text='C:', value='C', font=20,
                         variable=ABCD_var, command=click_ABCD)
radio_C.place(x=10, y=300)
C_text = tk.Text(root, height=6, width=20, font=('', 12))
C_text.place(x=63, y=305)

radio_D = tk.Radiobutton(root, text='D:', value='D', font=20,
                         variable=ABCD_var, command=click_ABCD)
radio_D.place(x=250, y=300)
D_text = tk.Text(root, height=6, width=20, font=('', 12))
D_text.place(x=303, y=305)

# 功能按钮
ans_button = tk.Button(root, text='确定', width=8, font=('', 15),
                       command=click_ans_button)
ans_button.place(x=480, y=185)
error_button = tk.Button(root, text='加入错题', width=8, font=('', 15),
                         command=click_error_button)
error_button.place(x=480, y=245)
last_button = tk.Button(root, text='上一题', width=8, font=('', 15),
                        command=click_last_button)
last_button.place(x=600, y=185)
next_button = tk.Button(root, text='下一题', width=8, font=('', 15),
                        command=click_next_button)
next_button.place(x=600, y=245)
open_error_button = tk.Button(root, text='打开错题库', width=18, font=('', 15),
                              command=click_open_error_button)
open_error_button.place(x=490, y=305)

ans_label_var = tk.StringVar()
ans_label = tk.Label(root, textvariable=ans_label_var, font=20)
ans_label.place(x=500, y=360)

fill_data()
root.mainloop()
