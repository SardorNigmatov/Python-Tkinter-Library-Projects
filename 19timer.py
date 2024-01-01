import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("Time Counter")


hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(root,width=3,font=("Arial",18,""),textvariable=hour,background='light grey')
hourEntry.place(x=80,y=20)

minuteEntry = Entry(root,width=3,font=('Arial',18,""),textvariable=minute,background='light grey')
minuteEntry.place(x=130,y=20)

secondEntry = Entry(root,width=3,font=("Arial",18,""),textvariable=second,background='light grey')
secondEntry.place(x=180,y=20)

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Iltimos qiymatni to'g'ri kirting!")
    while temp > - 1:
        mins, secs = divmod(temp,60)
        
        hours = 0
        
        if mins > 60:
            hours, mins = divmod(mins,60)
            
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        
        root.update()
        time.sleep(1)
        
        if temp == 0:
            messagebox.showinfo("Time Countdown","Time's up")
        
        temp -= 1
        
bnt = Button(root,text="Set Time Countdown",bd='5',command=submit,bg='light green',fg='black')
bnt.place(x=70,y=120)
root.mainloop()