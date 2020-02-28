import city_spider
import analysis_json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

city_spider.spider().run()
root = tk.Tk()
root.title('中国天气查询-yl')
root['bg'] = '#b3d9ff'
# 设置主窗口居中显示
w = 760
h = 500
sw = int((root.winfo_screenwidth() - w)/2)
sh = int((root.winfo_screenheight() - h)/2)
root.geometry("{}x{}+{}+{}".format(w, h, sw, sh))
root.resizable(0, 0)
root.iconbitmap('lib/Images/classic.ico')

# photo_bg = ImageTk.PhotoImage(Image.open("lib/Images/forecast_bg.png"))
# label = tk.Label(root, image=photo_bg)
# label.pack()

combox_province_value = tk.StringVar()
combox_city_value = tk.StringVar()
combox_city2_value = tk.StringVar()
combox_city2_value.set("点击查询")
combox_day_value = tk.StringVar()



def chick_province(event):
    combox_province_value.set(combox_province.get())
    combox_city["values"] = analysis_json.city_list(combox_province_value.get())
    combox_city.current(0)
    combox_city2_value.set(combox_city_value.get())


def chick_city(event):
    combox_city_value.set(combox_city.get())
    combox_city2_value.set("点击查询")


def chick_seach():
    combox_city2_value.set(combox_city_value.get())
    print(combox_province_value.get() + combox_city_value.get())


label_province = tk.Label(root, text='省份:',bg='#b3d9ff').place(x=50, y=10)
combox_province = ttk.Combobox(root,
                               textvariable=combox_province_value, width=15)
combox_province["values"] = analysis_json.province_list()
combox_province.current(0)
combox_province.place(x=90, y=10)
combox_province.bind("<<ComboboxSelected>>", chick_province)

label_city = tk.Label(root, text='城市:',bg='#b3d9ff').place(x=250, y=10)
combox_city = ttk.Combobox(root,textvariable=combox_city_value,width=15)
combox_city["values"] = analysis_json.city_list("北京市")
combox_city.current(0)
combox_city.place(x=290, y=10)
combox_city.bind("<<ComboboxSelected>>", chick_city)

label_day = tk.Label(root, text='时间:',bg='#b3d9ff').place(x=440, y=10)
combox_day = ttk.Combobox(root,textvariable=combox_day_value,width=15)
combox_day["values"] = ['今天-10月17日-四']
combox_day.current(0)
combox_day.place(x=480, y=10)
combox_day.bind("<<ComboboxSelected>>", chick_city)

button_seach = tk.Button(root, text='查询', width=5, height=1,bg="#b3d9ff",
                         activebackground="#99e6ff", command=chick_seach)
button_seach.place(x=640, y=7, anchor='nw')

label_city2 = tk.Label(root, text='城市:',
                       bg='#b3d9ff',font=('',15)).place(x=80, y=90)
label_city3 = tk.Label(root, textvariable=combox_city2_value,
                       bg='#b3d9ff',font=('',40)).place(x=130, y=70)


photo_bg = ImageTk.PhotoImage(Image.open("lib/Images/bj-01.png"))
labelri = tk.Label(root, image=photo_bg,bg="#b3d9ff")
labelri.place(x=10,y=140)
label_cu = tk.Label(root, text='日出:',
                       bg='#b3d9ff',font=('',15)).place(x=5, y=265)



root.mainloop()

# url_list = analysis_json.get("江西省", "南昌")
# print(url_list)