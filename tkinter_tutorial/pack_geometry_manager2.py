from tkinter import *
root = Tk()
w = Label(
            root,
            text="Red",
            bg="red",
            fg="white"
        )
w.pack(side=LEFT)

w = Label(
            root,
            text="Green",
            bg="green",
            fg="black"
        )
w.pack(side=LEFT)

w = Label(
            root,
            text="Blue",
            bg="blue",
            fg="white"
        )
w.pack(side=LEFT)
root.mainloop()
