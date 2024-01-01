from tkinter import *
import calendar

def show_calendar():
    new_root = Tk()
    
    #yangi oynaning orqa fonini oq rang qiliyapmiz
    new_root.config(background='white')
    
    #Title
    new_root.title("CALENDAR")
    
    #Yangi oynaning o'lchami
    new_root.geometry("550x600")
    
    # Kiritilganyilni tutib olish
    year = int(year_field.get())
    
    cal_content = calendar.calendar(year)
    
    cal_year = Label(new_root,text=cal_content,font="Consolas 10 bold")
    
    cal_year.grid(row=5,column=1,padx=20)
    
    new_root.mainloop()
    
if __name__ == "__main__":
    root = Tk()
    
    root.config(background="white")
    
    root.title("CALENDAR")
    
    root.geometry("250x140")
    
    cal = Label(root,text="CALENDAR",bg='dark gray',font=('times',28,'bold'))
    
    year = Label(root,text="Enter year:",bg="light green")
    
    year_field = Entry(root)
    
    Show = Button(root,text="Show Calendar",fg="Black",bg="Red",command=show_calendar)
    
    Exit = Button(root,text='Exit',fg='Black',bg="Red",command=exit)
    
    cal.grid(row=1,column=1)
    
    year.grid(row=2,column=1)
    
    year_field.grid(row=3,column=1)
    
    Show.grid(row=4,column=1)
    
    Exit.grid(row=6,column=1)
    
    root.mainloop()
    
    
    
    
    