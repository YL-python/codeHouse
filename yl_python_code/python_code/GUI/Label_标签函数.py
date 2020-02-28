from tkinter import *

root = Tk()   # 创建一个根窗口以后的东西都在这个根窗口上显示   Tk类
root.title('Tk...这里是标题')   # 设置根窗口的标题

bj_photo = PhotoImage(file = '背景.gif')   # PhotoImage类
textLabel = Label(root,   # 在哪显示   Label类 用标签函数创建一个标签
                  justify=LEFT,  # 文字对齐方式默认居中对齐 LEFT RIGHT 左对齐和右对齐
                  padx=10,   # 文字距离左边框间距
                  text="。。。..小标签\n..。\t。。",   #  显示的内容
                  image=bj_photo,   # 添加背景 需要图片对象
                  compound=CENTER,    # 图文混合模式 文字浮与上方
                  font=('华文彩云',10),   # 设置标签字体 和字体大小
                  fg='green')   # 设置字体颜色 也就是前景色

textLabel.pack(side=LEFT)   # pack 把创建的标签包装并显示出来  side 参数设置标签位置，默认居中 LEFT  RIGHT

bq_photo = PhotoImage(file = '标签.gif')   # 图片函数 实例化一个图片对象  报错原因可能是图片的后缀名被修改过
imgLabel = Label(root, image=bq_photo)
imgLabel.pack()  # Label类 的pack方法

mainloop()   # 吧主窗口打出来
'''
最开始要设置一个主窗口（Tk()方法）  最后要把主窗口打印出来（mainloop()方法）
1、PhotoImage(file=) 图片函数 传入图片地址 返回一个图片对象

2、Label 标签函数 第一个参数传主窗口
                text参数 设置标签内容
                font参数 设置字体
                justify参数 表示标签文字对齐方式 默认居中对齐 LEFT RIGHT 左对齐和右对齐
                fg参数 设置标签文字前景色
                padx参数 标签文字距左边框距离
                image参数 设置背景 需要穿图片对象
                compound参数 设置图文 的混合模式
         返回一个标签对象

3、pack()  显式标签对象函数  side参数 表示标签对象的位置 默认居中对齐

文字标签和图片标签的参数 text image 参数决定了标签的种类
'''