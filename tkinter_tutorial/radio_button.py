from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)

root = Tk()
var = IntVar()
radio_button_nums = 5

for i in range(radio_button_nums):
    radio_button = Radiobutton(
            root,
            text="Option {}".format(i+1),
            variable=var,
            value=i+1,
            command=sel
        )
    radio_button.pack()

label = Label(root)
label.pack()
root.mainloop()
