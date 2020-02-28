__author__ = 'xianhua.meng'
# encoding: utf-8
# !/usr/bin/python

'''Tkinter教程之Frame篇'''
# Frame就是屏幕上的一块矩形区域，多是用来作为容器（container）来布局窗体。
'''1.创建Frame'''
# -*- coding: cp936 -*-
from tkinter import *

root = Tk()
# 以不同的颜色区别各个frame
for fm in ['red', 'blue', 'yellow', 'green', 'white', 'black']:
    # 注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    Frame(height=20, width=400, bg=fm).pack()
root.mainloop()
# 添加不同颜色的Frame，大小均为20*400
