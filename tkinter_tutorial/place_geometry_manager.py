from tkinter import *
from tkinter import messagebox as msb

top = Tk()
top.title("root's title")
def helloCallBack():
    msb.showinfo("title", "message")

b = Button(top, text="button's text", command=helloCallBack)
b.pack()
b.place(bordermode=OUTSIDE, height=100, width=100)
top.mainloop()
