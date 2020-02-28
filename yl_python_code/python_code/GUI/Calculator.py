'''
2019年7月1日 09:07:49

'''
import tkinter as tk
from tkinter import messagebox

var=''
lishi_xinxi=[]
font_size = 24

root = tk.Tk()
root.title('计算器')
root.geometry('350x600')
# root.resizable(0,0)

frame_one = tk.Frame(root)
frame_one.pack()
frame_two = tk.Frame(root)
frame_two.pack()

text_one = tk.Text(frame_one,height=4,font=('楷体',font_size))
text_one.pack()

def set_1():
    global var
    var = var+'1'
    text_one.insert('end','1')
def set_2():
    global var
    var = var + '2'
    text_one.insert('end', '2')
def set_3():
    global var
    var = var + '3'
    text_one.insert('end', '3')
def set_4():
    global var
    var = var + '4'
    text_one.insert('end', '4')
def set_5():
    global var
    var = var + '5'
    text_one.insert('end', '5')
def set_6():
    global var
    var = var + '6'
    text_one.insert('end', '6')
def set_7():
    global var
    var = var + '7'
    text_one.insert('end', '7')
def set_8():
    global var
    var = var + '8'
    text_one.insert('end', '8')
def set_9():
    global var
    var = var + '9'
    text_one.insert('end', '9')
def set_0():
    global var
    var = var + '0'
    text_one.insert('end', '0')
def set_jia():
    global var
    var = var + '+'
    text_one.insert('end', '+')
def set_jian():
    global var
    var = var + '-'
    text_one.insert('end', '-')
def set_cheng():
    global var
    var = var + '*'
    text_one.insert('end', '*')
def set_chu():
    global var
    var = var + '/'
    text_one.insert('end', '/')
def set_mo():
    global var
    var = var + '%'
    text_one.insert('end', '%')
def set_dian():
    global var
    var = var + '.'
    text_one.insert('end', '.')
def del_one():
    global var
    var = var[0:-1]
    text_one.delete(1.0,'end')
    text_one.insert('end', var)
def del_all():
    global var
    var = ''
    text_one.delete(1.0,'end')
def final_jisuan():
    global var,lishi_xinxi
    var_1 ,var_3= var, ''
    var = ''
    try:
        var_2 = str(eval(var_1))
        var_3 = var_1 + '=' + var_2
        text_one.delete(1.0, 'end')
        text_one.insert('end', var_3+'\n')
    except:
        tk.messagebox.showerror('错误', '出现了一点问题\n可能是计算式有误')  # 错误消息框
    if var_3:
        lishi_xinxi.append(var_3)
    print(lishi_xinxi)

tk.Button(frame_two,text='C',font=('楷体',24),height=2,width=5,command=del_all).grid(row=0,column=0)
tk.Button(frame_two,text='➗',font=('楷体',24),height=2,width=5,command=set_chu).grid(row=0,column=1)
tk.Button(frame_two,text='X',font=('楷体',24),height=2,width=5,command=set_cheng).grid(row=0,column=2)
tk.Button(frame_two,text='<-',font=('楷体',24),height=2,width=5,command=del_one).grid(row=0,column=3)
tk.Button(frame_two,text='1',font=('楷体',24),height=2,width=5,command=set_1).grid(row=1,column=0)
tk.Button(frame_two,text='2',font=('楷体',24),height=2,width=5,command=set_2).grid(row=1,column=1)
tk.Button(frame_two,text='3',font=('楷体',24),height=2,width=5,command=set_3).grid(row=1,column=2)
tk.Button(frame_two,text='-',font=('楷体',24),height=2,width=5,command=set_jian).grid(row=1,column=3)
tk.Button(frame_two,text='4',font=('楷体',24),height=2,width=5,command=set_4).grid(row=2,column=0)
tk.Button(frame_two,text='5',font=('楷体',24),height=2,width=5,command=set_5).grid(row=2,column=1)
tk.Button(frame_two,text='6',font=('楷体',24),height=2,width=5,command=set_6).grid(row=2,column=2)
tk.Button(frame_two,text='+',font=('楷体',24),height=2,width=5,command=set_jia).grid(row=2,column=3)
tk.Button(frame_two,text='7',font=('楷体',24),height=2,width=5,command=set_7).grid(row=3,column=0)
tk.Button(frame_two,text='8',font=('楷体',24),height=2,width=5,command=set_8).grid(row=3,column=1)
tk.Button(frame_two,text='9',font=('楷体',24),height=2,width=5,command=set_9).grid(row=3,column=2)
tk.Button(frame_two,text='=',font=('楷体',24),height=4,width=5,command=final_jisuan).grid(row=3,column=3,rowspan=2)
tk.Button(frame_two,text='%',font=('楷体',24),height=2,width=5,command=set_mo).grid(row=4,column=0,rowspan=1)
tk.Button(frame_two,text='0',font=('楷体',24),height=2,width=5,command=set_0).grid(row=4,column=1,rowspan=1)
tk.Button(frame_two,text='.',font=('楷体',24),height=2,width=5,command=set_dian).grid(row=4,column=2,rowspan=1)

menubar = tk.Menu(root)

def look_lishi():
    global lishi_xinxi
    lishi_xinxi2 = lishi_xinxi[::-1]
    lishi_xinxi3='空'
    for i in lishi_xinxi2[0:10]:
        lishi_xinxi3= lishi_xinxi3 + str(i) + '\n'
    print(lishi_xinxi3)
    tk.messagebox.showinfo(title='历史记录', message=lishi_xinxi3[1:])

def del_lishi():
    global lishi_xinxi
    lishi_xinxi=[]
    tk.messagebox.showinfo(title='删除历史记录', message='删除成功')

lishimenu = tk.Menu(menubar, tearoff=0)  # 下拉菜单
menubar.add_cascade(label='历史记录',menu=lishimenu)
lishimenu.add_command(label='查看历史记录',command=look_lishi)
lishimenu.add_command(label='清空历史记录',command=del_lishi)

def help_data():
    tk.messagebox.showinfo(title='帮助', message='这是一个基于Python的小型计算器程序\n'\
                                               '您可以使用它做一些简单的运算\n\
                                               历史记录最多保存10条')

helpmenu = tk.Menu(menubar, tearoff=0)  #顶级菜单
menubar.add_command(label='帮助',command=help_data)

def set_font_max():
    global font_size
    font_size = font_size+4
def set_font_min():
    global font_size
    font_size = font_size - 4
setmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='设置',menu=setmenu)
setfontmenu = tk.Menu(setmenu)  #扩展菜单
setmenu.add_cascade(label='设置字体大小',menu=setfontmenu,underline=0)
setfontmenu.add_command(label='字体加大',command=set_font_max)
setfontmenu.add_command(label='字体减小',command=set_font_min)

def not_set():
    tk.messagebox.showinfo(title='其他设置', message='程序员偷了一点懒')

setothermenu = tk.Menu(setmenu)  #扩展菜单
setmenu.add_cascade(label='其他设置',menu=setothermenu,underline=0)
setothermenu.add_command(label='其他设置1',command=not_set)
setothermenu.add_command(label='其他设置2',command=not_set)
setothermenu.add_command(label='其他设置3',command=not_set)

root.config(menu=menubar)
root.mainloop()