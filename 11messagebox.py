from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap("./icons/university.ico")


#showinfo, showwarning, showerror, askquestion, askyesing

def popup():
    response = messagebox.askquestion("Mening xabarim","Hello World!")
    # Label(root,text=response).pack()
    if str(response) == "yes":
        Label(root,text="Siz Yesni bosdingiz!").pack()
    else:
        Label(root,text="Siz No ni bosdingiz!").pack()

Button(root,text="Meni bos",command=popup).pack()


root.mainloop()
