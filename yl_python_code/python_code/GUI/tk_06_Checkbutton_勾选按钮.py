'''
2019年6月20日 20:06:53
设置整形的可变参数 勾选时赋值为1 不勾选时赋值为0
'''

import tkinter as tk

root = tk.Tk()
root.title('今天学勾选')
root.geometry('400x200')

label_one = tk.Label(root, text='I not love Enthing', height=1, width=50, bg='yellow')
label_one.pack()

def set_data():
    if(var1.get() == 1)and(var2.get() == 0):
        label_one.config(text='I love only Python')
    elif(var1.get() == 0)and(var2.get() == 1):
        label_one.config(text='I love only Java')
    elif(var1.get() == 0)and(var2.get() == 0):
        label_one.config(text='I not love Enthing')
    else:
        label_one.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
check_one = tk.Checkbutton(root, text='Python',variable=var1,onvalue=1, offvalue=0,command=set_data)
check_two = tk.Checkbutton(root, text='Java',variable=var2,onvalue=1, offvalue=0,command=set_data)
check_one.pack()
check_two.pack()

root.mainloop()