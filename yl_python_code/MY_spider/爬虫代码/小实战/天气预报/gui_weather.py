import Weather
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('中国天气查询')
root.geometry('500x300')

label_one = tk.Label(root, text='输入想要查找的城市:', font=('Arial', 12),
                     height=2, width=20).place(x=20, y=20, anchor='nw')
var = tk.StringVar()
entry_one = tk.Entry(root, textvariable=var, width=15, font=('Arial', 12))
entry_one.place(x=200, y=30, anchor='nw')


def hit_me():

    name = var.get()
    try:
        w_spider = Weather.WeatherSpider(name)
        w_str = w_spider.Run()
        text_1.delete(0.0,'end')
        text_1.insert('insert', w_str)
    except:
        text_1.delete(0.0, 'end')
        text_1.insert('insert', '出错啦')
        var.set('发生了一点小问题')
        tk.messagebox.showerror('错误', '发生了一点小问题\n检查一下网络或者是否是输入有误')



button_one = tk.Button(root, text='查询', width=15, height=1, command=hit_me)
button_one.place(x=350, y=25, anchor='nw')
text_1 = tk.Text(root, width=50, font=('Arial', 9), height=10)
text_1.place(x=70, y=90, anchor='nw')
root.mainloop()
