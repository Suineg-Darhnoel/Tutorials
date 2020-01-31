from tkinter import *

master = Tk()

scroll_bar = Scrollbar(master)
scroll_bar.pack(side=RIGHT, fill=Y)

list_box = Listbox(master, yscrollcommand=scroll_bar.set)

for i in range(1000):
    list_box.insert(END, str(i))

list_box.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=list_box.yview)
scroll_bar.config(command=list_box.yview)

master.mainloop()
