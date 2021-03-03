import tkinter as tk

window = tk.Tk()
window.title = ('my window')
window.geometry('400x100')

counter = 0
def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

# 在窗口上创建一个菜单栏（最上方的菜单栏横条）
menubar = tk.Menu(window)
# Valid resource names: activebackground, activeborderwidth,
# activeforeground, background, bd, bg, borderwidth, cursor,
# disabledforeground, fg, font, foreground, postcommand, relief,
# selectcolor, takefocus, tearoff, tearoffcommand, title, type.

# 定义一个竖条
filemenu = tk.Menu(menubar, tearoff=0)

# 在菜单单元中添加一个菜单项File
menubar.add_cascade(label='File', menu=filemenu)

# 在File菜单项添加命令选项
filemenu.add_command(label='New', command=do_job)   # 点击调用do_job
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)

# 添加一条分割线
filemenu.add_separator()

# 定义一个子菜单条
submenu = tk.Menu(filemenu)  # 和上面定义菜单一样，不过此处是在File上创建一个空的菜单
submenu.add_command(label="Submenu1", command=do_job)  # 给submenu添加功能选项
submenu.add_command(label="Submenu2", command=do_job)

# 添加一个展开下拉菜单，并把上面的子菜单嵌入给它
filemenu.add_cascade(label='Import', menu=submenu, underline=0)

# 同样的在File中加入Exit小菜单,此处对应命令为window.quit
filemenu.add_command(label='Exit', command=window.quit)

# 在顶部再添加两个菜单项
viewmenu = tk.Menu(menubar, tearoff=0)
windowsmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='View', menu=viewmenu)
menubar.add_cascade(label='Windows', menu=windowsmenu)

# 将菜单配置给窗口
window.config(menu=menubar)

window.mainloop()
