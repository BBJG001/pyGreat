# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x250')

def print_selection():
    l.config(text='you have selected ' + var1.get())
    # ���var1��ֵ�������ø���config��Label�е�text���ԣ�Ҳ������label�е���ʾ���ݣ�

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.StringVar()
var1.set('B')   # ������һ����Ĭ��ѡ�У��������ֵ���ڿ�ѡ���У���ȫ����ѡ��
r1 = tk.Radiobutton(window, text='Option A',variable=var1, value='A',
                    command=print_selection)
# Radiobutton   ��ѡ��
# �ɹ������������: activebackground, activeforeground, anchor,
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

# ��for���ѭ������
var2 = tk.StringVar()
vlist = ['��','��','��','��']
for v in vlist:
    tk.Radiobutton(window, text='Option '+v,variable=var2, value=v).pack()

window.mainloop()   # ��ѭ������ͣ��ˢ������ʾ