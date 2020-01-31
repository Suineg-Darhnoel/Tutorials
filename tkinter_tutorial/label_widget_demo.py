import tkinter

def cb():
    user_input = input()
top = tkinter.Tk()
user_input = "Hello"
label = tkinter.Label(top, text=user_input)

button1 = tkinter.Button(top, text="input", command=cb)
button1.pack()

label.pack()
top.mainloop()
