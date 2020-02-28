'''
s2019年6月20日 13:29:21

'''
import tkinter as tk

root = tk.Tk()
root.title('今天学滑块')
root.geometry('400x200')

label_one = tk.Label(root, text='滑一下试试', height=1, width=50, bg='yellow')
label_one.pack()

def this_def(v):
    label_one.config(text='滑动了' + v)

scale_A = tk.Scale(root, label='这里是滑动条',  # 设置滑块标题
                   from_=0, to=12,  # 设置滑块起始和结束值
                   orient=tk.HORIZONTAL,  # 滑块方向  不写就是默认竖直
                   length=400, showvalue=0,  # 滑动条的长度和是否显示值
                   tickinterval=6, resolution=0.01,  # 设置显示值的步长和滑动的步距
                   command=this_def)  # 指定函数 会给指定函数传一个值
scale_A.pack()

root.mainloop()