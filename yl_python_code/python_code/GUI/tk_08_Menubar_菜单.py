'''
2019年6月20日 20:57:15
menu.add_cascade      添加子选项
menu.add_command      添加命令（label参数为显示内容）
menu.add_separator    添加分隔线
menu.add_checkbutton  添加确认按钮
delete                删除
'''
import tkinter as tk
root = tk.Tk()
root.title('菜单-Menu')
root.geometry('400x200')

lable_one = tk.Label(root, width=15, bg='yellow')

cent = 0

def do_job():
    global cent
    lable_one.config(text='do'+str(cent))
    cent+=1

lable_one.pack()

menubar = tk.Menu(root)  # 在主窗口创建菜单条

filemenu = tk.Menu(menubar, tearoff=0)  # 在菜单条上创建文件菜单
menubar.add_cascade(label='文件',menu=filemenu)  # 把文件菜单添加到菜单条上
filemenu.add_command(label='New',command=do_job)  # 在文件菜单上添加方法
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command = root.quit)
# filemenu.add_checkbutton(label='勾选')

submenu = tk.Menu(filemenu)  # 在文件菜单上创建扩展菜单
filemenu.add_cascade(label='Import',menu=submenu,underline=0)  # 把扩展菜单添加到文件菜单上
submenu.add_command(label='Submenu1',command=do_job)  # 在扩展菜单上添加一个方法
submenu.add_checkbutton(label='勾选1')
submenu.add_checkbutton(label='勾选2')
submenu.add_checkbutton(label='勾选3')

editmenu = tk.Menu(menubar, tearoff=0) # 在菜单条上创建工具菜单
menubar.add_cascade(label='工具',menu=editmenu)  # 把工具菜单添加到菜单条上
editmenu.add_command(label='Cut',command=do_job)  # 在工具菜单上添加方法
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu2 = tk.Menu(editmenu)
editmenu.add_cascade(label='Import2',menu=submenu2,underline=0)
submenu2.add_command(label='Submenu2',command=do_job)

submenu3 = tk.Menu(submenu2)
submenu2.add_cascade(label='Import3',menu=submenu3,underline=0)
submenu3.add_command(label='Submenu3',command=do_job)

root.config(menu=menubar)  # 修改主界面的菜单条信息

root.mainloop()