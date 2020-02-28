from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入simpledialog
from tkinter import simpledialog
# 导入dialog
from tkinter import dialog
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.msg = 'C语言中文网成立于 2012 年初，目前已经运营了将近 5 年，我们致力于分享精品教程，帮助对编程感兴趣的读者。'
        # 创建2个按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='打开SimpleDialog',
            command=self.open_simpledialog # 绑定open_simpledialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
        ttk.Button(self.master, text='打开Dialog',
            command=self.open_dialog # 绑定open_dialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
    def open_simpledialog(self):
        # 使用simpledialog.SimpleDialog创建对话框
        d = simpledialog.SimpleDialog(self.master, # 设置该对话框所属的窗口
            title='SimpleDialog测试', # 标题
            text=self.msg,  # 内容
            buttons=["是", "否", "取消"],
            cancel=3,
            default=0 # 设置默认是哪个按钮得到焦点
        )
        print(d.go())  #①
    def open_dialog(self):
        # 使用dialog.Dialog创建对话框
        d = dialog.Dialog(self.master # 设置该对话框所属的窗口
            , {'title': 'Dialog测试',  # 标题
            'text':self.msg, # 内容
            'bitmap': 'question', # 图标
            'default': 0,  # 设置默认选中项
            # strings选项用于设置按钮
            'strings': ('确定',
                '取消',
                '退出')})
        print(d.num)  #②
root = Tk()
root.title("对话框测试")
App(root)
root.mainloop()