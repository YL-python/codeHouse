'''
2019年6月19日 21:30:51
设置可变文本值的时候要用 set()方法
插入要用 insert()方法
listbox 可以插入值 删除值
listbox_one.curselection() 可以获取当前鼠标确定的列表的值
'''
import tkinter as tk

root = tk.Tk()
root.title('标题呀')
root.geometry('400x200')

var_one = tk.StringVar()
label_one = tk.Label(root,textvariable=var_one,bg='blue',width=10,height=2)
label_one.pack()

def print_selection():
    value = listbox_one.get(listbox_one.curselection())
    var_one.set(value)

button_one = tk.Button(root,text='print selection',command=print_selection)
button_one.pack()

var_two = tk.StringVar()
var_two.set((11,22,33,44))
listbox_one = tk.Listbox(root, listvariable=var_two)

list_items = [1,2,3,4]
for item in list_items:
    listbox_one.insert('end',item)
item = 'First'
listbox_one.insert(1,item)
item = 'Second'
listbox_one.insert(2,item)
listbox_one.delete(2)
listbox_one.pack()


root.mainloop()