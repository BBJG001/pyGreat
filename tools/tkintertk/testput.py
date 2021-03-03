import tkinter as tk

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
    tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
    tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r, column=2)
    r = r + 1

# tk.Label(text='', relief=tk.RIDGE, width=15).grid(row=r,column=0)
# tk.Entry(bg='grey', relief=tk.SUNKEN, width=10).grid(row=6,column=0,rowspan=2)
tk.Label(text='rowspan=2', relief=tk.RIDGE, width=15).grid(row=6, column=0, rowspan=2)
tk.Label(text='columnspan=2', relief=tk.RIDGE, width=15).grid(row=6, column=1, columnspan=2)

tk.Label(text='row7', relief=tk.RIDGE, width=15).grid(row=7, column=2)

tk.Label(text='row8', relief=tk.RIDGE, width=15).grid(row=8, column=2)

tk.mainloop()