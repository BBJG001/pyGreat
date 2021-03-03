# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x250')

def print_selection():
    l.config(text='you have selected ' + var1.get())
    # 获得var1的值，并配置给（config）Label中的text属性（也就是在label中的显示内容）

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.StringVar()
var1.set('B')   # 设置哪一个被默认选中，如果设置值不在可选项中，则全不被选中
r1 = tk.Radiobutton(window, text='Option A',variable=var1, value='A',
                    command=print_selection)
# Radiobutton   单选框
# 可供传入的属性有: activebackground, activeforeground, anchor,
# background, bd, bg, bitmap, borderwidth, command, cursor,
# disabledforeground, fg, font, foreground, height,
# highlightbackground, highlightcolor, highlightthickness, image,
# indicatoron, justify, padx, pady, relief, selectcolor, selectimage,
# state, takefocus, text, textvariable, underline, value, variable,
# width, wraplength.
r1.pack(anchor='w')
tk.Radiobutton(window, text='Option B',variable=var1, value='B', command=print_selection).pack()


line = tk.Label(window, text='------------------------------------')
line.pack()

# 用for语句循环生成
var2 = tk.StringVar()
vlist = ['张','王','李','赵']
for v in vlist:
    tk.Radiobutton(window, text='Option '+v,variable=var2, value=v).pack()

window.mainloop()   # 主循环，不停地刷新以显示