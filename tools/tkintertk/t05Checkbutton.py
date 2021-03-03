# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x80')

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):   #���ѡ�е�һ��ѡ�δѡ�еڶ���ѡ��
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1): #���ѡ�еڶ���ѡ�δѡ�е�һ��ѡ��
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):  #�������ѡ�δѡ��
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')             #�������ѡ�ѡ��

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var1.set(1)     # �������ֵ��onvalue��ֵ����Ĭ��ѡ�У��������ֵ��offvalue���߷�on��off��ֵ����Ĭ�ϲ�ѡ��
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
# Checkbutton   ��ѡ��
# ����
# variable  ��������ֵ�ı���
# onvalue   �����ѡ��var1��ֵ����onvalue��ֵ
# offvalue  ���δ��ѡ��var1��ֵ����offvalue��ֵ
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