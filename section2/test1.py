from tkinter import *


def print_hello():
    print('hi')


root = Tk()

w = Label(root, text="Python Test")
b = Button(root, text="Hello Python!", command=print_hello)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()
root.mainloop()
