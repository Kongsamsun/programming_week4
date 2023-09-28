from tkinter import *

def add_task(): #입력란(추가) 함수
    task = entry.get()
    if task is not None:
        listbox.insert(END, task)
        entry.delete(0, END)
    
def del_task():  #삭제 함수
    task_select = listbox.curselection()
    if task_select:
        listbox.delete(task_select)

window = Tk()

label1 = Label(window, text = "Add a Task:")

entry = Entry(window) #입력란 추가

button1 = Button(window, text = "Add Task", command = add_task)

listbox = Listbox(window) #목록 추가

button2 = Button(window, text = "Delete Task", command = del_task)

label1.pack();entry.pack();button1.pack();listbox.pack();button2.pack()

window.mainloop()