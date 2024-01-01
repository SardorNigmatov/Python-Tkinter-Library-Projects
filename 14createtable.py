from tkinter import *

class Table:
    def __init__(self,root) -> None:
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root,width=20,fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,lst[i][j])
                
                
lst = [
    (1,'Sardor','Toshkent viloyati',21),
    (2,'Bekzod','Surxondaryo',20),
    (3,'Zuxriddin','Samarqand',22),
    (4,'Ulug\'bek','Buxoro',21),
]

total_rows = len(lst)
total_columns = len(lst[0])

root = Tk()
root.title("Talabalar")
root.iconbitmap("./icons/university.ico")

t = Table(root)
root.mainloop()