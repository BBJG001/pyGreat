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
# Scale �̶ȳߣ�
# ����
# from  �½�
# to    �Ͻ�
# orient    # �߶����ķ���, tk.HORIZONTALΪ����tk.VERTICALΪ����
# length    # �߶����ĳ��ȣ���λΪ����
# showvalue # �Ƿ���ʾ�α�����λ�õ�ֵ
# tickinterval  # �̶ȼ��
# resolution    # ȡֵ����С�����λ
# �ɹ����������: activebackground, background, bigincrement, bd,
# bg, borderwidth, command, cursor, digits, fg, font, foreground, from,
# highlightbackground, highlightcolor, highlightthickness, label,
# length, orient, relief, repeatdelay, repeatinterval, resolution,
# showvalue, sliderlength, sliderrelief, state, takefocus,
# tickinterval, to, troughcolor, variable, width.
s.pack()

window.mainloop()