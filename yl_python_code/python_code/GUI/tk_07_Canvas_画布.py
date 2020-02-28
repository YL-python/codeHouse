'''
2019年6月20日 20:23:27

'''
import tkinter as tk
root = tk.Tk()
root.title('画布')
root.geometry('400x400')

canvas = tk.Canvas(root, bg='blue', height=300, width=400)
image_file = tk.PhotoImage(file='标签.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
x0,y0,x1,y1 = 200,0,250,50
line = canvas.create_line(x0,y0,x1,y1)  # 画线
oval = canvas.create_oval(x0+50,y0,x1+50,y1,fill='red')  # 画圆
arc = canvas.create_arc(x0,y0+50,x1,y1+50,start=30,extent=60)  # 画扇形
rect = canvas.create_rectangle(250,50,300,100)   # 画矩形
canvas.pack()

def moveit():
    canvas.move(rect,0,5)

button = tk.Button(root,text='move',command=moveit).pack()

root.mainloop()