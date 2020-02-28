'''
2019年6月29日 09:38:31

'''
from tkinter import messagebox
import tkinter as tk
root = tk.Tk()
root.title('弹窗')
root.geometry('400x200')

def hit_it():
    # tk.messagebox.showinfo(title='hi',message='hahaha')  # 提示消息框
    # tk.messagebox.showwarning('警告', '明日有大雨')  # 警告消息框
    # tk.messagebox.showerror('错误', '出错了')  # 错误消息框
    # print(tk.messagebox.askquestion(title='hi', message='hahaha'))  # 是否 返回值是 yes no 字符串 用if判断做后续操作
    # print(tk.messagebox.askyesno(title='hi', message='hahaha'))  # 是否  返回值是 TRUE FALSE  用if判断做后续操作
    # print(tk.messagebox.askretrycancel(title='hi', message='hahaha'))  # 重试取消 返回值是 TRUE FALSE  用if判断做后续操作
    print(tk.messagebox.askokcancel(title='hi', message='hahaha'))  # 是否 返回值是 TRUE FALSE  用if判断做后续操作

tk.Button(root,text='hit me',command=hit_it).pack()

root.mainloop()