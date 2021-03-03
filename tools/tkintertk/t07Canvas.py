import tkinter as tk

window = tk.Tk()
window.title = ('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# 注意：tkinter中的坐标系左上角为原点，向右为x轴正向，向下为y轴正向

# 在canvas（画布）上放张图片
image_file = tk.PhotoImage(file='data/test1.gif')
image = canvas.create_image(5, 5, anchor='nw', image=image_file)
# 首先传入的是锚点坐标
# anchor指定图片的那个点为锚点可选值有n s w e nw ne sw se

x0, y0, x1, y1 = 50, 50, 80, 80
# canvas的坐标是以左上角为（0，0），往右为x正半轴，往下为y正半轴
line = canvas.create_line(x0, y0, x1, y1)   # 画直线
# 两个点的四个坐标值
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')    # 画椭圆
# 在左上角（x0, y0）和右下角（x1, y1）框住的矩形内画一个椭圆，如果框了一个正方形，就是画了一个正圆
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)    # 画扇形
# 四个坐标值与上面画圆的坐标值一样，start为角度起始，extent为角度结束
rect = canvas.create_rectangle(100, 10, 100+50, 10+20)  # 画矩形
# canvas.delete(rect)   # 在画布上删除某个形状
rect2 = canvas.create_rectangle(120, 20, 110+50, 20+20)

print(canvas.coords(rect))  # 获得图形坐标（就是画图时传入的值）

canvas.pack()

def moveit():
    canvas.move(rect, 0, 2) # 移动某个图形，下移动

tk.Button(window, text='move', command=moveit).pack()

window.mainloop()