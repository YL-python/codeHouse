'''
2019年7月1日 08:33:33

'''

import tkinter as tk
root = tk.Tk()
root.title('位置摆放')
root.geometry('400x200')

# 方法一
# tk.Label(root,text=1).pack(side='top')
# tk.Label(root,text=1).pack(side='bottom')
# tk.Label(root,text=1).pack(side='left')
# tk.Label(root,text=1).pack(side='right')

# # 方法2   grid   方格
# for i in range(4): # 行
#     for j in range(3): #列
#         tk.Label(root, text=1).grid(row=i,column=j,padx=10,pady=10,ipadx=5,ipady=5)

# 方法3  指定像素点
tk.Label(root,text=1).place(x=10,y=100,anchor='nw')  # anchor 方位

root.mainloop()