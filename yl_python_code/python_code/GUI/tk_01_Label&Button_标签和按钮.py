'''
2019年6月19日 20:09:38
tk.Label() 创建标签
tk.Button() 创建按钮
'''
import tkinter as tk


root = tk.Tk()  # 创建窗口
root.title('窗口标题')  # 设置窗口标题
root.geometry('200x100')  # 设置窗口大小

var = tk.StringVar()  # 创建一个tk里面的字符串类型
label_one = tk.Label(root, textvariable=var, bg='green', font=('Arial',12), height=2, width=15)  # textvariable 传可变字符串的
label_one.pack()

on_hit = False
def hit_me():
    global on_hit
    if not on_hit:
        var.set('you hit ')
        on_hit = True
    else:
        var.set('')
        on_hit = False

button_one = tk.Button(root, text='hit this', width=15, height=2, command=hit_me)
button_one.pack()

root.mainloop()  # 不断刷新窗口