from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio buttons")
root.iconbitmap("./icons/university.ico")

# r = IntVar()
# r.set("1")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mashroom"),
    ("Onion","Onion")
]

pizz = StringVar()
pizz.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root,text=text,variable=pizz,value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

# Radiobutton(root,text="Option1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
# Radiobutton(root,text="Option2",variable=r,value=2,command=lambda:clicked(r.get())).pack()


myLabel = Label(root,text=pizz.get())
myLabel.pack()

myButton = Button(root,text="Click Me!",command=lambda: clicked(pizz.get()))
myButton.pack()

root.mainloop()


