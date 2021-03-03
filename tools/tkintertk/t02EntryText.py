# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

def insert_point():
    var = e.get()   # 从输入框e获取值
    t.insert('insert', var)     # 插入到Text框的光标处
    # t.insert(1.1, var)  # 在（1，1）位置插入（索引从0开始）

def insert_end():
    var = e.get()   # 从输入框e获取值
    t.insert('end', var)    # 插入到Text框的末尾

e = tk.Entry(window, show='*' , bg='#aaaaaa')   # 输入框
# 输入框，可供传入的变量有： background, bd, bg, borderwidth, cursor,
# exportselection, fg, font, foreground, highlightbackground,
# highlightcolor, highlightthickness, insertbackground,
# insertborderwidth, insertofftime, insertontime, insertwidth,
# invalidcommand, invcmd, justify, relief, selectbackground,
# selectborderwidth, selectforeground, show, state, takefocus,
# textvariable, validate, validatecommand, vcmd, width,
# xscrollcommand.
# show='*',以*代替输入, = None,原始显示，不会被代替
# bg    背景颜色
# boderwidth    边框宽度
e.pack(pady=5)    # 放置输入框

b1 = tk.Button(window, text='inster point', width=15, height=2, command=insert_point)
b1.pack(pady=5)    # 放置Button
b2 = tk.Button(window, text='inster end', width=15, height=2, command=insert_end)
b2.pack(pady=5)    # 放置Button

t = tk.Text(window, height=2)
# 放置一个文本框，用来显示
# 可供传入的参数有
# STANDARD OPTIONS
#     background, borderwidth, cursor,
#     exportselection, font, foreground,
#     highlightbackground, highlightcolor,
#     highlightthickness, insertbackground,
#     insertborderwidth, insertofftime,
#     insertontime, insertwidth, padx, pady,
#     relief, selectbackground,
#     selectborderwidth, selectforeground,
#     setgrid, takefocus,
#     xscrollcommand, yscrollcommand,
#
# WIDGET-SPECIFIC OPTIONS
#     autoseparators, height, maxundo,
#     spacing1, spacing2, spacing3,
#     state, tabs, undo, width, wrap,
t.pack(padx=10, pady=5)

window.mainloop()   # 主循环，不停地刷新以显示