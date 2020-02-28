'''
2019年6月25日 23:08:51

'''
import tkinter as tk
root = tk.Tk()
root.title('Frame_框架')
root.geometry('400x200')

tk.Label(root,text='on the root').pack()

frame_one = tk.Frame(root)
frame_one.pack()

frame_l = tk.Frame(frame_one,)
frame_r = tk.Frame(frame_one)
frame_l.pack(side="left")
frame_r.pack(side='right')

tk.Label(frame_l,text='frame_l_1').pack()
tk.Label(frame_l,text='frame_l_2').pack()
tk.Label(frame_r,text='frame_r').pack()

root.mainloop()