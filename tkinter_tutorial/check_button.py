from tkinter import *
def cb():
    print("variable1  is", var1.get())
    print("variable2  is", var2.get())

win = Tk()
var1 = IntVar()
var2 = IntVar()

c = Checkbutton(
            win,
            text="Enable Tab",
            variable=var1,
            command=(lambda: cb())
        )
c.pack()
c1 = Checkbutton(
            win,
            text="Enable Tab2",
            variable=var2,
            command=(lambda: cb())
        )
c1.pack()

win.mainloop()
