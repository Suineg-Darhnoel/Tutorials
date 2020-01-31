from tkinter import *

root = Tk()

# to create a tkinter variable, call the corresponding constructor
v = StringVar()
label = Label(root, textvariable=v).pack()
v.set("New Text!")

print(v.get())
root.mainloop()
