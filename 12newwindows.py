from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Create new windows")
root.iconbitmap("./icons/university.ico")

# Oyna ichida yangi oyna ochish

def open():
    global my_img
    top = Toplevel()
    top.title("My second Window")
    top.iconbitmap("./icons/ins.ico")
    lb1 = Label(top,text='Hello, World!').pack()
    my_img = ImageTk.PhotoImage(Image.open("./images/img3.png"))
    my_label = Label(top,image=my_img).pack()
    btn2 = Button(top,text="close window",command=top.destroy).pack()

btn = Button(root,text="Open Second Window",command=open).pack()

mainloop()