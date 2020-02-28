'''
2019年6月19日 20:10:10
tk.Entry() 定义文本框
tk.Text() 定义文字栏
'''
import tkinter as tk

root = tk.Tk()  # 创建窗口
root.title('窗口标题')  # 设置窗口标题
root.geometry('400x200')  # 设置窗口大小

entry_one = tk.Entry(root,show=None)  # show='*'
entry_one.pack()


def insert_point():
    var = entry_one.get()  # 获取文本框的文本
    text_one.insert('insert',var)  # ‘insert’决定插入文本在文字栏的光标位置


def insert_end():
    var = entry_one.get()
    text_one.insert('end',var)  # ‘end’决定插入文本在文字栏的末尾        还可以用 行.列 设置具体插入到哪  比如 2.1 就是插入到第二行第一列


button_one = tk.Button(root, text='在光标处插入', width=15, height=2, command=insert_point)
button_two = tk.Button(root, text='在末尾插入', width=15, height=2, command=insert_end)
button_one.pack()
button_two.pack()

text_one = tk.Text(root, height=2)
text_one.pack()

# DISABLED 无法编辑、插入、删除。在你需要插入、删除的时候把状态变为NORMAL，完成插入、删除后再改回DISABLED
# text.config(state=NORMAL)
# text.delete(1.0, END)
# text.insert(END, text)
# text.config(state=DISABLED)

root.mainloop()  # 不断刷新窗口
