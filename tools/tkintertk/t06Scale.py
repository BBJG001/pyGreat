# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

def print_selection(v):
    l.config(text='you have selected ' + v)

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=2, resolution=0.01, command=print_selection)
# Scale 刻度尺？
# 其中
# from  下界
# to    上届
# orient    # 尺度条的方向, tk.HORIZONTAL为横向，tk.VERTICAL为竖向
# length    # 尺度条的长度，单位为像素
# showvalue # 是否显示游标所在位置的值
# tickinterval  # 刻度间隔
# resolution    # 取值保留小数点后几位
# 可供传入的属性: activebackground, background, bigincrement, bd,
# bg, borderwidth, command, cursor, digits, fg, font, foreground, from,
# highlightbackground, highlightcolor, highlightthickness, label,
# length, orient, relief, repeatdelay, repeatinterval, resolution,
# showvalue, sliderlength, sliderrelief, state, takefocus,
# tickinterval, to, troughcolor, variable, width.
s.pack()

window.mainloop()