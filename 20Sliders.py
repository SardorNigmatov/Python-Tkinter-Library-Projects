from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Sliders")
root.iconbitmap("./icons/university.ico")
root.geometry("250x250")

vertical = Scale(root,from_=0,to=500)
vertical.pack()

horizontal = Scale(root,from_=0,to=500,orient=HORIZONTAL)
horizontal.pack()

def slide():
    label_horizontal = Label(root,text=horizontal.get()).pack()
    label_vertical = Label(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
    
    
my_btn = Button(root,text="Click me!",command=slide).pack()

root.mainloop()