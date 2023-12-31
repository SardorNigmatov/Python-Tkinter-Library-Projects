from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Frame")
root.iconbitmap("./icons/university.ico")

frame = LabelFrame(root,text="This is my Frame",padx=5,pady=5)
frame.pack(padx=10,pady=10)

b = Button(frame,text="Don't Click Here!")
b2 = Button(frame,text="Here!")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)

root.mainloop()