from tkinter import *

def callbake():
    var.set('吹吧你，我才不信！')


root = Tk()
root.title('Tk...这里是标题')

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("未满18周岁禁止观看！")

textLabel = Label(frame1,
                  justify=LEFT,
                  textvariable=var,
                  font=('宋体',20))

textLabel.pack(side=LEFT)

bq_photo = PhotoImage(file = '禁止.gif')
imgLabel = Label(frame1, image=bq_photo)
imgLabel.pack()

theButton = Button(frame2,text='我已满18周岁',command=callbake)
theButton.pack(pady=10)
frame1.pack()
frame2.pack()

mainloop()