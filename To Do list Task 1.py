#importing modules
from tkinter import *
from tkinter import messagebox

# creating functions
def Task():
    task= entry.get()
    if task !="":
        l.insert(END ,task)
        entry.delete(0,"end")
    else:
        messagebox.showwarning("Enter some Task")
def Delete():
    l.delete(ANCHOR)

#Window creation
window=Tk()
window.geometry('500x450+500+200')
window.title('To Do List')
window.configure(bg='Black')
window.resizable(width=False,height=False)

#Widgets creation
frame=Frame(window)
frame.pack(pady=10)
l=Listbox(
    frame,
    width=25,
    height=8,
    font=("Ariel",18),
    bd=0,
    fg="Pink",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none",
    )
l.pack(side=LEFT,fill=BOTH)
task_list=[
    "Internship",
    "Codesoft",
    "DSA",
    "DAA",
    ]
for item in task_list:
    l.insert(END,item)

scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)

l.config(yscrollcommand=scroll.set)
scroll.config(command=l.yview)

entry=Entry(
    window,
    font=("Ariel",24)
    )
entry.pack(pady=20)

button_frame=Frame(window)
button_frame.pack(pady=20)

addTask=Button(
    button_frame,
    text="ADD TASK",
    font=("Ariel 14"),
    bg="Green",
    padx=20,
    pady=10,
    command=Task
    )
addTask.pack(fill=BOTH,expand=True,side=LEFT)

delTask=Button(
    button_frame,
    text="DELETE TASK",
    font=("Ariel 14"),
    bg="White",
    padx=20,
    pady=10,
    command=Delete
    )
delTask.pack(fill=BOTH,expand=True,side=LEFT)
#creating mainloop
window.mainloop()
    
    
    
    
