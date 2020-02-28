'''
2019年6月20日 13:19:35
Radiobutton() 创建选择按钮 variable参数带一个可变字符串  value 给可变字符串赋值、
标签对象.config()可以修改 该标签对象的属性
'''

import tkinter as tk

root = tk.Tk()
root.title('今天学选择按钮')
root.geometry('400x200')

label_one = tk.Label(root, text='', height=1, width=50, bg='yellow')
label_one.pack()

def set_data():
    label_one.config(text='you set '+ var.get())

var = tk.StringVar()
radio_A = tk.Radiobutton(root, text='Option A', variable=var, value='A', command=set_data)
radio_A.pack()
radio_B = tk.Radiobutton(root, text='Option B', variable=var, value='B', command=set_data)
radio_B.pack()
radio_C = tk.Radiobutton(root, text='Option C', variable=var, value='C', command=set_data)
radio_C.pack()

root.mainloop()