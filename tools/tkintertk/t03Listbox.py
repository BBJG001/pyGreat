# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)   # ��ʾ��
l.pack()

def print_selection():
    value = lb.get('active')    # ��ù�괦��ֵԭget��lb.curselection()�����һ��ʼû�й�궨λʱ�ᱨ��
    # lb.get('active')Ҳ�У����һ��ʼĬ�Ϲ�궨λ�ڵ�һ��
    var1.set(value)

b = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b.pack()    # ����Button

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # ��������ΪԪ�顢list������
lb = tk.Listbox(window, listvariable=var2)
# tk.Listbox()������һ�����ݣ������������ֵ
# ���Դ���Ĳ���: background, bd, bg, borderwidth, cursor,
# exportselection, fg, font, foreground, height, highlightbackground,
# highlightcolor, highlightthickness, relief, selectbackground,
# selectborderwidth, selectforeground, selectmode, setgrid, takefocus,
# width, xscrollcommand, yscrollcommand, listvariable.
list_items = [1, 2, 3, 4]   # ÿ���������Listbox�������end������һ��ֵ
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')   # ���������루�������㿪ʼ��
lb.insert(2, 'second')
lb.delete(2)            # ������ɾ��
lb.pack()               # ����ListBox

window.mainloop()   # ��ѭ������ͣ��ˢ������ʾ