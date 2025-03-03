from tkinter import *
def lighton():
    global photo2
    photo2 =PhotoImage(file="icons8-light-48 (2).png")
    lb.config(image=photo2,bg="#B7B1F2",text="on", )
    print("Light is ON!")

def lightOFF():
    global photo3
    photo3 =PhotoImage(file="icons8-light-48 (1).png")
    lb.config(image=photo3,bg="#B7B1F2",text="OFF")
    print("light is OFF !")
win = Tk()
# add title
win.title("My Fast Application ")
# add icon
win.iconbitmap("icons8-light-48.ico")
# add bg color
win.config(bg="#B7B1F2")
width = 500
height = 500
sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()
c_x = int(sys_width /2 - width /2)
c_y = int(sys_height /2 - height /2)

win.geometry(f"{width}x{height}+{c_x}+{c_y}")

labal =Label(win, text="Hello World !",font=("Franklin Gothic Medium",30) ,fg="#37AFE1",bg="#B7B1F2",cursor="heart")
labal.pack(ipadx=10, ipady=10)

photo = PhotoImage(file="icons8-light-48 (1).png")
lb = Label(win,image=photo,bg="#B7B1F2",text="off",compound="top")
lb.place(x=80,y=15)
bt = Button(win,text="ON",command=lighton,cursor="hand1")
bt2 = Button(win,text="OFF",command=lightOFF,cursor="hand1")
bt.place(x=240,y=200)
bt2.place(x=200,y=200)
mainloop()
