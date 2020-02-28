'''
2019年7月5日 13:13:33
用tk.Toplevel() 可以创建子窗口


Popup = Toplevel(root)
Popup.resizable(0,0)
Popup.attributes("-toolwindow", 1)
Popup.wm_attributes("-topmost", 1)
这些代码是让子窗口一直在主窗口前面的

root_2.quit()   是退出全部窗口
root_2.destroy()   能关闭当前窗口

获取文本框里面的值 设置textvariable  用Tk的变量类型
'''

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title('登陆界面')
root.geometry('400x300')
root.resizable(0,0)

shuju = {'123':'123'}

# 欢迎图片
img = tk.PhotoImage(file='landin_photo.gif')
img_lab = tk.Label(image=img)
img_lab.pack()

# 输入框
text_lab1 = tk.Label(root,text='账号：',font=('楷体',13)).place(x=70,y=180)
text_lab2 = tk.Label(root,text='密码：',font=('楷体',13)).place(x=70,y=220)
var_name = tk.StringVar()
var_name.set('example@python.com')
var_pwd = tk.StringVar()
entry_one = tk.Entry(root,show=None,font=('楷体',13),textvariable=var_name).place(x=140,y=180)
entry_two = tk.Entry(root,show='*',font=('楷体',13),textvariable=var_pwd).place(x=140,y=220)
# check_one = tk.Checkbutton(root,variable=var_3,onvalue=1, offvalue=0,command=look_pwd).place(x=325,y=217)

# 登录注册
def login():
    usr_name = var_name.get()
    usr_pwd = var_pwd.get()
    if usr_pwd == '':
        tk.messagebox.showinfo(title='提示', message='请输入密码')
    elif usr_name not in shuju.keys():
        ans = tk.messagebox.askyesno(title='提示', message='用户不存在，是否现在注册？')
        if ans:
            sign()
    elif not(usr_pwd == shuju[usr_name]):
        tk.messagebox.showinfo(title='提示', message='密码错误，请重试')
    else:
        tk.messagebox.showinfo(title='提示', message='登录成功')

def sign():
    def sign_2():
        name = var_name2.get()
        pwd1 = var_pwd2.get()
        x = len(pwd1)
        pwd2 = var_pwd2_two.get()
        if name=='':
            tk.messagebox.showinfo(title='提示', message='注册失败\n请输入账号')
            # root_2.attributes("-toolwindow", 1)
            root_2.wm_attributes("-topmost", 1)
        elif pwd1 == '' or pwd2 == '':
            tk.messagebox.showinfo(title='提示', message='注册失败\n请输入密码')
            # root_2.destroy()
            root_2.wm_attributes("-topmost", 1)
        elif name in shuju.keys():
            tk.messagebox.showinfo(title='提示', message='注册失败\n用户已存在，请换一个账号重试')
            root_2.wm_attributes("-topmost", 1)
        elif x < 6 or x > 16:
            tk.messagebox.showinfo(title='提示', message='注册失败\n密码长度有误，请重新输入')
            root_2.wm_attributes("-topmost", 1)
        elif not(pwd1 == pwd2):
            tk.messagebox.showinfo(title='提示', message='注册失败\n两次输入的密码不同，请重新输入')
            root_2.wm_attributes("-topmost", 1)
        else:
            shuju[name] = pwd1
            tk.messagebox.showinfo(title='提示', message='注册成功')
            root_2.wm_attributes("-topmost", 1)
            root_2.destroy()

    root_2 = tk.Toplevel() # 创建窗口上的窗口
    root_2.title('注册界面')
    root_2.geometry('350x200')
    tk.Label(root_2, text='账号：', font=('楷体', 13)).place(x=50, y=20)
    tk.Label(root_2, text='密码：', font=('楷体', 13)).place(x=50, y=50)
    tk.Label(root_2, text='密码：', font=('楷体', 13)).place(x=50, y=90)
    tk.Label(root_2, text='6-16个字符组成', font=('楷体', 8)).place(x=100, y=70)
    tk.Label(root_2, text='请您再次输入您的密码', font=('楷体', 10)).place(x=100, y=120)
    var_name2 = tk.StringVar()
    var_pwd2 = tk.StringVar()
    var_pwd2_two = tk.StringVar()
    tk.Entry(root_2, show=None, font=('楷体', 13), textvariable=var_name2).place(x=100, y=20)
    tk.Entry(root_2, show=None, font=('楷体', 13), textvariable=var_pwd2).place(x=100, y=50)
    tk.Entry(root_2, show=None, font=('楷体', 13), textvariable=var_pwd2_two).place(x=100, y=90)
    tk.Button(root_2, text='注册', font=('楷体', 13), width=5, command=sign_2).place(x=150, y=150)


btn_login = tk.Button(root,text='登陆',font=('楷体',13), width=5,command=login).place(x=150,y=250)
btn_sign = tk.Button(root,text='注册',font=('楷体',13), width=5,command=sign).place(x=250,y=250)
root.mainloop()