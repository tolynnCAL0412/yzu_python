import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('300x300')

# fruits = ['apple', 'banana', 'mango', 'melonwater']
fruits = {'apple':50, 'banana':60, 'mango':70, 'melonwater':25}
combo = ttk.Combobox(win, values=list(fruits.keys()), state='readonly')  # readonly, disabled
combo.current(1)    # index
combo.pack()

win.mainloop()