from tkinter import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

def clickNext() :
       global num
       num += 1
       if num > 8 :
             num = 0
       label1.configure(text = fnameList[num])

def clickPrev() :
       global num
       num -= 1
       if num < 0 :
             num = 8
       label1.configure(text = fnameList[num])

window = Tk()
window.geometry("700x100")
window.title("tk")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)

label1 = Label(window, text = fnameList[num], fg = "blue", font = ("궁서체", 20))
label1.pack()  

btnPrev.place(x = 150, y = 10)
btnNext.place(x = 500, y = 10)
label1.place(x = 290, y = 10)

window.mainloop()