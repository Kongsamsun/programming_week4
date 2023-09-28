from tkinter import *

photo_dict = {"dog" : "dog.gif"
              ,"cat" : "cat.gif"
              ,"rabbit" : "rabbit.gif"}

def Vote():
    vote_option = radio_var.get()
    if vote_option == 1:
        photo = PhotoImage(file = "C:\Python Program\jpeg파일\dog.gif")
    elif vote_option == 2:
        photo = PhotoImage(file = "C:\Python Program\jpeg파일\cat.gif")
    else:
        photo = PhotoImage(file = "C:\Python Program\jpeg파일/rabbit.gif")
    pLabel.configure(image = photo, borderwidth = 3, highlightthickness = 3, highlightbackground = "yellow")
    pLabel.image = photo

window = Tk()
window.title("애완동물 선택하기")
window.geometry("400x400")

tLabel = Label(window, text = "좋아하는 동물 투표", fg = "blue", font = ("궁서체", 20)).pack()

radio_var = IntVar()
rb1 = Radiobutton(window, text = "강아지", variable = radio_var, value = 1).pack()
rb2 = Radiobutton(window, text = "고양이", variable = radio_var, value = 2).pack()
rb3 = Radiobutton(window, text = "토끼", variable = radio_var, value = 3).pack()

image_button = Button(window, text = "사진 보기", command = Vote)
image_button.pack()

pLabel = Label(window)
pLabel.pack()

window.mainloop()