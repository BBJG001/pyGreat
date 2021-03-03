import tkinter as tk

window = tk.Tk()
window.title = ('my window')
window.geometry('300x150')

tk.Label(window, text='on the window').pack()

# 在window上创建一个frame
frm = tk.Frame(window, bg='purple')
frm.pack()


# 把上面的frm分成上下两个frame
frm_top = tk.Frame(frm, bg='red', borderwidth=3)
frm_bottom = tk.Frame(frm, bg='blue', borderwidth=3)
# 放置两个frame并指定在外城frame中的相对位置
frm_top.pack(side='top')
frm_bottom.pack(side='bottom')

# 把frm_bottom分成左右两个frame
frm_b_l = tk.Frame(frm_bottom, bg='orange', borderwidth=3)
frm_b_r = tk.Frame(frm_bottom, bg='yellow', borderwidth=3)

# 放置两个frame
frm_b_l.pack(side='left')
frm_b_r.pack(side='right')

# 分别在top，b_l，b_r三个frame中添加内容
tk.Label(frm_top, text='on the frm_top').pack()
tk.Label(frm_b_l, text='on the frm_l').pack()
tk.Label(frm_b_r, text='on the frm_r1').pack()
tk.Label(frm_b_r, text='on the frm_r2').pack()

window.mainloop()