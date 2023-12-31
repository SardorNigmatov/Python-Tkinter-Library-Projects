from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images")
root.iconbitmap("ins.ico")


my_img = ImageTk.PhotoImage(Image.open("ins.jfif"))
myLabel = Label(image=my_img)
myLabel.pack()

button_quit = Button(root,text="Exit progamm",command=root.quit)
button_quit.pack()


root.mainloop()