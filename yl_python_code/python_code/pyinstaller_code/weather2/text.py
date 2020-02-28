import tkinter
from tkinter import ttk

'''
165
https://www.easyicon.net/1233767-sun_icon.html
https://www.easyicon.net/1218190-night_icon.html
https://www.easyicon.net/1188528-Weather_icon.html

https://www.easyicon.net/download/ico/1188528/16/

http://image.nmc.cn/static2/site/nmc/themes/basic/images/bj-01.png
'''


# def go(*args):  # 处理事件，*args表示可变参数
#     print(comboxlist.get())  # 打印选中的值
#
#
# win = tkinter.Tk()  # 构造窗体
# comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# comboxlist["values"] = ("1", "2", "3", "4")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()
#
# win.mainloop()  # 进入消息循环


# !/usr/bin/env python
# -*- coding: utf-8 -*-


#
# from tkinter import *
#
# master = Tk()
#
# listbox = Listbox(master)
# listbox.pack()
#
# listbox.insert(END, "a list entry")
#
# for item in ["one", "two", "three", "four"]:
#     listbox.insert(END, item)
#
# mainloop()

from tkinter import *

master = Tk()

Label(text="one").pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()

mainloop()