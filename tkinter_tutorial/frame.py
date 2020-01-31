from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

red_button = Button(frame, text="Red", fg="red")
red_button.pack(side=LEFT)

green_button = Button(bottom_frame, text="Brown", fg="brown")
green_button.pack(side=LEFT)

blue_button = Button(frame, text="Blue", fg="blue")
blue_button.pack(side=LEFT)

black_button = Button(bottom_frame, text="Black", fg="black")
black_button.pack(side=LEFT)

root.mainloop()
