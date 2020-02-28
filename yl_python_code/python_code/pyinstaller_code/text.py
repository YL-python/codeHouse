from tkinter import *
root = Tk()
frame = Frame(root,width=200,height=200)
def callback(event):
    print('当前位置为：',event.x,event.y)
frame.bind('<Button-1>',callback)
frame.pack()
mainloop()