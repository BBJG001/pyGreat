import tkinter as tk

# from tkinter import *
# from tkinter.filedialog import askdirectory
#
# def selectPath():
#     path_ = askdirectory()
#     path.set(path_)
#
# root = Tk()
# path = StringVar()
#
# Label(root,text = "目标路径:").grid(row = 0, column = 0)
# Entry(root, textvariable = path).grid(row = 0, column = 1)
# Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
#
# root.mainloop()

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空

var = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window,
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

b = tk.Button(window,
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2,
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

window.mainloop()
