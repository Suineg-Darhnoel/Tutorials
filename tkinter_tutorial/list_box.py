from tkinter import *
master = Tk()
list_box = Listbox(master)
list_box.pack()
list_box.insert(END, "a list entry")
for item in ["one", "two", "three", "four"]:
    list_box.insert(END, item)

master.mainloop()
