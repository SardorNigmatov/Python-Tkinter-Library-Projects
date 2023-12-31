from tkinter import *
from datetime import datetime
root = Tk()

# en = Entry(root,width=50,borderwidth=10,border=5,fg='red',bg='black')
# en.pack()

# def myClick():
#     myLabel = Label(root,text=f"Tugma bosildi!\n{en.get()}")
#     myLabel.pack()

# myButton = Button(root,text='Meni bos!',command=myClick,padx=50,pady=20,fg='green',bg='red')
# myButton.pack()

e = Entry(root,width=50,fg="black",bg="green",borderwidth=10,border=10)
e.pack()
e.insert(1,"Tug'ilgan yilingizni kiriting:")

def myClick():
    year = int(e.get())
    age = datetime.now().year - year
    myLabel = Label(root,text=f"Siz {age} yoshdasiz!")
    myLabel.pack()
    
myButton = Button(root,text="Yoshni hisoblash",command=myClick,padx=50,pady=20,bg="black",fg='white')
myButton.pack()

root.mainloop()