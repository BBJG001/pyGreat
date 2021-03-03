import tkinter as tk

# 用来测试pyinstaller的，简单的tk可以成功
# 复杂的import会失败
# 生成窗口
window = tk.Tk()
window.title('.exe了一个窗口')
window.geometry('450x300')

canvas = tk.Canvas(window, bg='grey', height=100, width=200)

canvas.pack()

# 不停的刷新显示
window.mainloop()