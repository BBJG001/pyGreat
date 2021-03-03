import tkinter as tk
from tkinter.filedialog import *
from application.video_format_convert.convert import convert
import threading

# 点击“选择文件”按钮调用该功能
def selectFilePath():
    path_ = askopenfilename(title='选择文件')
    pathin.set(path_)
    print(pathin.get())

# 点击“选择文件夹”调用该功能
def selectDirecPath():
    path_ = askdirectory(title='选择文件夹')
    # path_ = askopenfilename(title='选择文件')
    pathout.set(path_)
    print(path_)

# 点击提交执行的功能
def executeit():
    hint.set('converting . . .')
    convert(pathin.get(), pathout.get(), aimf.get())
    hint.set('convert finished')

def thread_it(func, *args):
    # 创建进程
    t = threading.Thread(target=func, args=args)
    # 守护进程
    t.setDaemon(True)
    # 启动
    t.start()

# 生成窗口
window = tk.Tk()
window.title('格式转换')
window.geometry('450x300')

# 格式转换label
tk.Label(window, text='格式转换').place(x=200, y=10)  # x是从左向右的偏移，y是从上向下的偏移

# 输入文件一行
pathin = tk.StringVar()     # 定义变量
tk.Label(window, text='输入文件:').place(x=50, y=50)
entry_pathin = tk.Entry(window, textvariable=pathin).place(x=160, y=50)     # 输入框
btn_pathin = tk.Button(window, text='选择文件', command=selectFilePath).place(x=340, y=45)  # 按钮

# 输出文件的一行
pathout = tk.StringVar()
tk.Label(window, text='输出位置:').place(x=50, y=100)  # 从左偏，从上偏
tk.Entry(window, textvariable=pathout).place(x=160, y=100)
tk.Button(window, text='选择文件夹', command=selectDirecPath).place(x=335, y=95)

# 目标格式的一行
aimf = tk.StringVar()
tk.Label(window, text='目标格式:').place(x=50, y=150)  # 从左偏，从上偏
tk.Entry(window, textvariable=aimf).place(x=160, y=150)

# 提交按钮
# tk.Button(window, text='  提 交  ', command=executeit).place(x=200, y=190)
tk.Button(window, text='  提 交  ', command=lambda:thread_it(executeit)).place(x=200, y=190)

# 提示区域
hint = tk.StringVar()
hint.set('')
tk.Label(window, textvariable=hint).place(x=190, y=240)

# 不停的刷新显示
window.mainloop()
