import tkinter as tk

window = tk.Tk()            # 声明一个窗口
window.title('my window')   # 设置名称
window.geometry('400x200')  # 设置窗口尺寸

# Label         : 文字展示，传一个textvariable=tk.StringVar的变量可以动态修改展示的内容
# Button        : 按钮
# Entry         : 输入框
# Listbox       :
# RadioButton   :
# Checkbutton   : 复选框
# Scale         : 游标滑块定值
# Menubar       :
# Frame         : 布局，可以分割页面，也可用来做页面切换

'''
fill    : 当前组件填充父组件的方式， fill=NONE or X or Y or BOTH - fill widget if widget grows
ipadx   : 横向内边距
padx    : 横向外边距
width   : 宽度，可以在某些组件中设置，可以在place中设置
height  : 类比width宽度
bg      : 背景颜色
fg      : Label中的背景颜色
side    : 配合pack放置方式，
sticky  : =NSEW, 在grid中，东西南北向哪儿对齐， - if cell is larger on which sides will this widget stick to the cell boundary
'''

var = tk.StringVar()
# l = tk.Label(window, text='OMG, this is TK', bg='green', font=('Arial', 12), width=15, height=2)
l = tk.Label(window, textvariable=var , bg='green', font=('Arial', 12), width=15, height=2)
# label标志/标签，其中的长和宽的单位是字符。上面注释掉的一行用text属性来显示静态内容，textvariable属性可以指定一个变量，指定变量的原因就是为了通过改变变量的值进行动态显示
l.pack()    # 放置方式1
# l.place(x=50, y=100)   # 放置方式2,以形状的左上角为基准，x>0表示向右偏移，y>0表示向下偏移
# l.grid(row=0, column=1)   # 放置方式3，这个像html中的table标签一样，通过网格进行界面布局，这个跟上面的两个不能共用，如果用了grid，则整个界面的所有放置方式都必须是grid
on_hit = False

def hit_me():   # 这是为tk.Button配置的一个函数，点击之后调用执行这个函数
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')   # 改变var也就是在上面tk.Label(textvariable=var)指定的变量
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)    # command调用要执行的处理函数
# 按钮，command属性指定点击按钮之后调用的函数，注意属性值只是函数名，没有后面的()
# 如果有参数的话，通过args属性指定，如 args=(3,5)
b.pack()    # 放置Button

window.mainloop()   # 就是一个循环，不停的刷新串口页面