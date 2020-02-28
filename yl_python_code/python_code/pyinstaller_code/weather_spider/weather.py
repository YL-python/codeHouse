import weather_spider
import tkinter as tk
import requests
from tkinter import messagebox

root = tk.Tk()
root.title('中国天气查询')
root.geometry('500x300')
root.resizable(0,0)

label_one = tk.Label(root, text='输入想要查找的城市:', font=('Arial', 12),
                     height=2, width=20).place(x=20, y=20, anchor='nw')
var = tk.StringVar()
entry_one = tk.Entry(root, textvariable=var, width=15, font=('Arial', 12))
entry_one.place(x=200, y=30, anchor='nw')


def hit_me():
    name = var.get()
    try:
        w_spider = weather_spider.WeatherSpider(name)
        w_str = w_spider.Run()
        text_1.config(state=tk.NORMAL)
        text_1.delete(0.0, 'end')
        text_1.insert('insert', w_str)
        text_1.config(state=tk.DISABLED)
    except requests.exceptions.ConnectionError:
        text_1.config(state=tk.NORMAL)
        text_1.delete(0.0, 'end')
        text_1.insert('insert', '发生了一点问题...可能是网络未连接')
        text_1.config(state=tk.DISABLED)
        var.set('发生了一点小问题')
        tk.messagebox.showerror('错误', '发生了一点小问题\n请检查一下网络')
    except:
        text_1.config(state=tk.NORMAL)
        text_1.delete(0.0, 'end')
        text_1.insert('insert', '发生了一点问题...检查一下城市名是否正确')
        text_1.config(state=tk.DISABLED)
        var.set('发生了一点小问题')
        tk.messagebox.showerror('错误', '发生了一点小问题\n检查一下是否是输入有误')

button_one = tk.Button(root, text='查询', width=15, height=1, command=hit_me)
button_one.place(x=350, y=25, anchor='nw')
text = '使用介绍：\n在输入框中输入你想查找的城市，点击查询即可看到该城市近七天的天气情况\n数据来源：中国天气网:http://www.weather.com.cn'
text_1 = tk.Text(root, width=50, font=('Arial', 9), height=9)
text_1.place(x=70, y=90, anchor='nw')
text_1.insert('insert', text)
text_1.config(state=tk.DISABLED)
root.mainloop()
