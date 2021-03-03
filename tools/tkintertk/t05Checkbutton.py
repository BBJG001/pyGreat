# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x80')

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #如果选中第一个选项，未选中第二个选项
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #如果选中第二个选项，未选中第一个选项
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #如果两个选项都未选中
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #如果两个选项都选中

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var1.set(1)     # 如果设置值是onvalue的值，就默认选中；如果设置值是offvalue或者非on非off的值，就默认不选中
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
# Checkbutton   复选框
# 其中
# variable  用来传递值的变量
# onvalue   如果被选中var1的值就是onvalue的值
# offvalue  如果未被选中var1的值就是offvalue的值
# Valid resource names: activebackground, activeforeground, anchor,
# background, bd, bg, bitmap, borderwidth, command, cursor,
# disabledforeground, fg, font, foreground, height,
# highlightbackground, highlightcolor, highlightthickness, image,
# indicatoron, justify, offvalue, onvalue, padx, pady, relief,
# selectcolor, selectimage, state, takefocus, text, textvariable,
# underline, variable, width, wraplength.
c2 = tk.Checkbutton(window, text='Java', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()

window.mainloop()