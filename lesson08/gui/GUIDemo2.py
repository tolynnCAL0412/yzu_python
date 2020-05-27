import tkinter

win = tkinter.Tk()

win.title('我的小視窗')

lable = tkinter.Label(win, text='Hello')
lable.pack(side=tkinter.LEFT)

lable2 = tkinter.Label(win, text='Hello2')
lable2.pack(side=tkinter.RIGHT)

win.geometry('300x300')

win.mainloop()