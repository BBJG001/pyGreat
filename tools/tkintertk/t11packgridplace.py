import tkinter as tk

window = tk.Tk()
window.title = ('my window')
window.geometry('200x200')

# # .pack()方式放置
# tk.Label(window, text='1', bg='red').pack(side='top')   #上
# # pack支持的属性after, anchor, before, expand, fill, in, ipadx, ipady, padx, pady, side
# tk.Label(window, text='1', bg='red').pack(side='bottom')#下
# tk.Label(window, text='1', bg='red').pack(side='left')  #左
# tk.Label(window, text='1', bg='red').pack(side='right') #右

# # .grid()放置方式
# # 注：如果用这种方式，则整个窗口中只能出现这种方式
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=1, bg='red').grid(row=i, column=j, padx=10, pady=10,x=4)
#         # grid支持的属性：column, columnspan, in, ipadx, ipady, padx, pady, row, rowspan, sticky

# .place()放置方式
tk.Label(window, text=1, bg='red').place(x=20, y=50, anchor='nw')

window.mainloop()
