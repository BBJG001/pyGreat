# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

def insert_point():
    var = e.get()   # �������e��ȡֵ
    t.insert('insert', var)     # ���뵽Text��Ĺ�괦
    # t.insert(1.1, var)  # �ڣ�1��1��λ�ò��루������0��ʼ��

def insert_end():
    var = e.get()   # �������e��ȡֵ
    t.insert('end', var)    # ���뵽Text���ĩβ

e = tk.Entry(window, show='*' , bg='#aaaaaa')   # �����
# ����򣬿ɹ�����ı����У� background, bd, bg, borderwidth, cursor,
# exportselection, fg, font, foreground, highlightbackground,
# highlightcolor, highlightthickness, insertbackground,
# insertborderwidth, insertofftime, insertontime, insertwidth,
# invalidcommand, invcmd, justify, relief, selectbackground,
# selectborderwidth, selectforeground, show, state, takefocus,
# textvariable, validate, validatecommand, vcmd, width,
# xscrollcommand.
# show='*',��*��������, = None,ԭʼ��ʾ�����ᱻ����
# bg    ������ɫ
# boderwidth    �߿���
e.pack(pady=5)    # ���������

b1 = tk.Button(window, text='inster point', width=15, height=2, command=insert_point)
b1.pack(pady=5)    # ����Button
b2 = tk.Button(window, text='inster end', width=15, height=2, command=insert_end)
b2.pack(pady=5)    # ����Button

t = tk.Text(window, height=2)
# ����һ���ı���������ʾ
# �ɹ�����Ĳ�����
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

window.mainloop()   # ��ѭ������ͣ��ˢ������ʾ