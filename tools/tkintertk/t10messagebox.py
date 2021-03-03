import tkinter as tk
import tkinter.messagebox  # 注：这里必须引入这个，没有这个直接tk.messagebox会报错

window = tk.Tk()
window.title = ('my window')
window.geometry('200x200')

def hit_me():
   # 提示信息弹窗
   tk.messagebox.showinfo(title='Hi', message='info')
   # tk.messagebox.showinfo(title='', message='')    # 提示信息对话窗
   # tk.messagebox.showwarning(message='warning!')   # 提出警告对话窗
   # tk.messagebox.showerror()                       # 提出错误对话窗
   # tk.messagebox.askquestion()                     # 询问选择对话窗

def confirm():
   # 带有返回值的弹窗
   print(tk.messagebox.askquestion(title='Hi', message='confirm?'))
   # print(tk.messagebox.askquestion())     # 返回yes和no
   # print(tk.messagebox.askokcancel())     # 返回true和false
   # print(tk.messagebox.askyesno())        # 返回true和false
   # print(tk.messagebox.askretrycancel())  # 返回true和false

tk.Button(window, text='hit me', command=hit_me).pack(pady=30)
tk.Button(window, text='confirm', command=confirm).pack()

window.mainloop()