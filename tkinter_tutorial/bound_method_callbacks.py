from tkinter import *
class HelloClass:
    # create the window in the class constructor
    def __init__(self):
        widget = Button(None, text="Press me to quit", command=self.quit)
        widget.pack()

    def quit(self):
        print("Leaving now")
        import sys; sys.exit()

HelloClass()
mainloop()
