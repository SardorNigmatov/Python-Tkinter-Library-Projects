from tkinter import *
# message box xabarni ko'rsatish uchun
from tkinter import messagebox

# Global o'zgaruchi vazifalarni salash uchun
tasks_list = []
# Vazifalarni sanagich
counter = 1


def inputError():
    """
    Agar kiritishda bo'sh yoki bo'sh 
    emaslikka tekshiradi
    """
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1

def clearTaskNumberField():
    """Vazifani raqamini o'chiruvchi funksiya
    """
    taskNumberField.delete(0.0,END)
    
    
def clear_taskField():
    """Vazifani o'chiruvchi funksiya
    """
    enterTaskField.delete(0,END)
    
def insertTask():
    global counter
    
    #Inputni tekshirish
    value = inputError()
    
    if value == 0:
        return 0
    
    content = enterTaskField.get() + "\n"
    
    tasks_list.append(content)
    
    TextArea.insert('end -1 chars',str(counter) + ")" + content)
    
    counter += 1
    
    clear_taskField()
    
    
def delete():
    global counter
    
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    
    number = taskNumberField.get((1.0),END)
    
    if number == "\n":
        messagebox.showerror("input error")
        return
    
    else:
        task_no = int(number)
        
    clear_taskField()
    
    tasks_list.pop(task_no - 1)
    
    counter -= 1
    
    TextArea.delete(1.0,END)
    
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', str(i+1)+")" + tasks_list[i])



if __name__ == "__main__":
    root = Tk()
    
    root.configure(background="light green")
    root.title("ToDo App")
    
    root.geometry("300x400")
    
    enterTask = Label(root,text="Enter your Task",bg="light green")
    
    enterTaskField = Entry(root)
    
    Submit = Button(root,text="Submit",fg="black",bg="Red",command=insertTask)
    
    TextArea = Text(root,height=10,width=30,font='lucida 13')
    
    taskNumber = Label(root,text="Delete Task Number",bg="blue")
    
    taskNumberField = Text(root,height=1,width=2,font="lucida")
    
    delete = Button(root,text="Delete",fg="Black",bg="Red",command=delete)
    
    Exit = Button(root,text="Exit",fg="Black",bg="Red",command=exit)
    
    enterTask.grid(row=0,column=2)
    
    enterTaskField.grid(row=1,column=2,ipadx=50)
    
    Submit.grid(row=2,column=2)
    
    TextArea.grid(row=3,column=2,padx=10,sticky=W)
    
    taskNumber.grid(row=4,column=2,pady=5)
    
    taskNumberField.grid(row=5,column=2)
    
    delete.grid(row=6,column=2,pady=5)
    
    Exit.grid(row=7,column=2)
    
    root.mainloop()


        