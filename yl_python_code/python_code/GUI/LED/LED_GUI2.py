from tkinter import *
from tkinter import ttk, colorchooser, simpledialog, messagebox, filedialog


class App:
    def __init__(self, master):
        self.master = master
        self.font_size = 11
        self.PageNum = 1
        self.xList=[252, 288, 324, 360, 396, 432, 468, 477, 477, 468, 432, 396, 360, 324, 288, 252, 216, 180, 144, 108, 72, 36, 27, 27, 36, 72, 108, 144, 180, 216]
        self.yList =[136, 102, 68, 34, 34, 68, 102, 136, 170, 204, 238, 272, 306, 341, 375, 409, 375, 341, 306, 272, 238, 204, 170, 136, 102, 68, 34, 34, 68, 102]
        self.colorList = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                          "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                          "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        self.time = 0
        self.allData = []
        self.Btn30 = [ttk.Button(self.master, text="", width=3) for i in range(30)]

        self.Lab30 = [Label(root,width=2) for i in range(30)]


        self.timeLab = Label(self.master,
                             text="当前帧延的延迟时间： 未设置", font=('', self.font_size))

        self.nextBtn = ttk.Button(self.master, text="下一帧")
        self.nextBtn.place(x=500/5*3, y=710/5*3)
        self.nextBtn.bind("<ButtonRelease-1>", self.check_nextBtn)

        self.lastBtn = ttk.Button(self.master, text="上一帧")
        self.lastBtn.place(x=300/5*3, y=710/5*3)
        self.lastBtn.bind("<ButtonRelease-1>", self.check_lastBtn)

        self.overBtn = ttk.Button(self.master, text="生成文件")
        self.overBtn.place(x=400/5*3, y=710/5*3)
        self.overBtn.bind("<ButtonRelease-1>", self.check_overBtn)
        self.repeat = 0
        self.repeatLab = Label(self.master,
                             text="所有帧重复次数： 未设置", font=('', self.font_size))

        self.showCenterLab(self.PageNum)
        self.show30LEDBtnLab(self.colorList)
        self.showTime(self.time)
        self.show_repeat(self.repeat)

    def show30LEDBtnLab(self, color):
        for lab in self.Lab30:
            lab.place(x=self.xList[self.Lab30.index(lab)],
                      y=self.yList[self.Lab30.index(lab)])

        for btn in self.Btn30:
            btn.place(x=self.xList[self.Btn30.index(btn)],
                      y=self.yList[self.Btn30.index(btn)]-2)
            btn.bind("<ButtonRelease-1>", self.choose_color)
        for i in range(30):
            if color[i] == "0":
                self.Lab30[i]["text"] = ""
            else:
                self.Lab30[i]["text"] = color[i]
            if color[i] == "0":
                self.Lab30[i]["bg"] = "#f0f0f0"
            else:
                self.Lab30[i]["bg"] = color[i]

    def showTime(self, time):
        if time == 0:
            self.timeLab["text"] = "当前帧延的延迟时间： 未设置"
        else:
            self.timeLab["text"] = "当前帧延的延迟时间： " + str(time) + " ms"
        self.timeLab.place(x=170, y=270)
        timeBtn = ttk.Button(self.master, text='点击设置')
        timeBtn.place(x=200, y=300)
        timeBtn.bind("<ButtonRelease-1>", self.set_time)

    def showCenterLab(self, index):
        centerLab = ttk.Label(self.master,
                              text="正在设置第 " + str(index) + " 帧",font=('', self.font_size))
        centerLab.place(x=340/5*3, y=50/5*3)

    def show_repeat(self,num):
        if num == 0:
            self.repeatLab["text"] = "所有帧重复次数： 未设置"
        else:
            self.repeatLab["text"] = "所有帧重复次数： " + str(num) + " 次"
        self.repeatLab.place(x=253/5*3,y=315/5*3)
        repeatBtn = ttk.Button(self.master, text='点击设置')
        repeatBtn.place(x=200, y=230)
        repeatBtn.bind("<ButtonRelease-1>", self.set_repeat)

    def set_repeat(self, event):
        # 调用askinteger函数生成一个让用户输入整数的对话框
        self.repeat = simpledialog.askinteger("重复帧设置", "设置重复帧（次）:",
                                            initialvalue=0)
        self.repeatLab["text"] = "所有帧重复次数： " + str(self.repeat) + " 次"


    def check_nextBtn(self, event):
        if self.PageNum > len(self.allData):
            data = {}
            colorList = [i["text"] for i in self.Lab30]
            for i in range(30):
                if (colorList[i] == ""):
                    colorList[i] = "0"
            data["colorList"] = colorList
            data["time"] = self.time
            self.allData.append(data)
            self.time = 0
            self.showTime(self.time)
            self.show30LEDBtnLab(self.colorList)
        elif self.PageNum == len(self.allData):
            self.time = 0
            self.showTime(self.time)
            self.show30LEDBtnLab(self.colorList)
        else:
            self.time = self.allData[self.PageNum]["time"]
            self.showTime(self.time)
            self.show30LEDBtnLab(self.allData[self.PageNum]["colorList"])

        self.PageNum = self.PageNum + 1
        self.showCenterLab(self.PageNum)
        self.show_repeat(self.repeat)
        print(self.allData)

    def check_lastBtn(self, event):
        print(self.allData)
        # 第一页判断和页码减一
        self.PageNum = self.PageNum - 1
        if (self.PageNum == 0):
            self.PageNum = 1
            messagebox.showerror('错误', '没有上一页')
        else:
            self.showCenterLab(self.PageNum)
        # 回写数据
        self.show30LEDBtnLab(self.allData[self.PageNum - 1]["colorList"])
        self.time = self.allData[self.PageNum - 1]["time"]
        self.showTime(self.time)
        self.show_repeat(self.repeat)

    def check_overBtn(self, event):
        if self.PageNum != len(self.allData):
            data = {}
            colorList = [i["text"] for i in self.Lab30]
            for i in range(30):
                if (colorList[i] == ""):
                    colorList[i] = "0"
            data["colorList"] = colorList
            data["time"] = self.time
            self.allData.append(data)
        print(self.allData)
        msg = "当前一共设置了 "+ str(len(self.allData)) + " 帧\n是否生成配置文件"
        if messagebox.askyesno(title='确认框', message=msg):
            file_path = filedialog.askdirectory(title='选择保存路径',initialdir='c:/')
            if file_path != '':
                try:
                    with open(file_path+"/information.txt","w")as f:
                        f.write("AAAAAA")
                        f.write(" ")
                        f.write("{:06x}".format(self.repeat))
                        f.write("\n")
                        for data in self.allData:
                            for color in data["colorList"]:
                                if(color == "0"):
                                    f.write(" ")
                                    f.write("000000")
                                else:
                                    f.write(" ")
                                    f.write(color.replace("#",""))
                            f.write(" ")
                            f.write("{:06x}".format(data['time']))
                            f.write("\n")

                    messagebox.showinfo(title='提示', message='文件保存成功，路径是：\n'+file_path+"/information.txt")
                except:
                    messagebox.showerror('错误', '出现了一点错误！')
        else:
            pass

    def choose_color(self, event):
        # 调用askcolor函数获取选中的颜色
        a, b = colorchooser.askcolor(parent=self.master, title='选择画笔颜色',
                                     color='blue')  # 初始颜色
        index = self.Btn30.index(event.widget)
        self.Lab30[index]["text"] = b
        self.Lab30[index]["bg"] = b

    def set_time(self, event):
        # 调用askinteger函数生成一个让用户输入整数的对话框
        self.time = simpledialog.askinteger("延迟时间设置", "设置延迟时间（ms）:",
                                            initialvalue=0)
        self.timeLab["text"] = "当前帧延的延迟时间： " + str(self.time) + " ms"

root = Tk()
root.title("配置文件生成程序")
# 设置主窗口居中显示
w = int(890/5*3)
h = int(750/5*3)
sw = int((root.winfo_screenwidth() - w) / 2)
sh = int((root.winfo_screenheight() - h) / 2)
root.geometry("{}x{}+{}+{}".format(w, h, sw, sh))
# 大小不可改变
root.resizable(0, 0)
App(root)
root.mainloop()

# pyinstaller -F -i w.ico -w LED_GUI.py
