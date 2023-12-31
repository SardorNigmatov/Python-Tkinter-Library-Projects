from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text=f"Tugma bosildi!")
    myLabel.pack()

myButton = Button(root,text='Meni bos!',command=myClick,padx=50,pady=20,fg='green',bg='red')
myButton.pack()

root.mainloop()