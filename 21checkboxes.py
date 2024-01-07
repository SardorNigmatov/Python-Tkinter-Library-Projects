from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.iconbitmap("./icons/university.ico")
root.geometry("400x400")

var = StringVar()

m = Checkbutton(root,text="Male", variable=var,onvalue="Male",offvalue="Female")
m.pack()

f = Checkbutton(root,text="Female",variable=var,onvalue="Female",offvalue="Male")
f.pack()

def show():
    myLabel = Label(root,text=var.get()).pack()

myButton = Button(root,text="Show selection",command=show).pack()



root.mainloop()