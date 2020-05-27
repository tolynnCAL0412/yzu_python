import tkinter

win = tkinter.Tk()

win.title('我的小視窗')

lable1 = tkinter.Label(win, text='Hello1')
lable2 = tkinter.Label(win, text='Hello2')
lable3 = tkinter.Label(win, text='Hello3')
lable4 = tkinter.Label(win, text='Hello4')
lable5 = tkinter.Label(win, text='Hello5')
lable6 = tkinter.Label(win, text='Hello6')
button1 = tkinter.Button(win, text='Button1')
lable1.grid(column=0, row=0)
lable2.grid(column=1, row=0)
lable3.grid(column=2, row=0)
lable4.grid(column=0, row=1)
lable5.grid(column=0, row=2)
lable6.grid(column=0, row=3)
button1.grid(column=0, row=4)

win.geometry('300x300')

win.mainloop()