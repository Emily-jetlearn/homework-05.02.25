#Basic vidgets
             
from tkinter import * 

win = Tk()
win.geometry("700x700")
win.title("my first window") #name of window
win.config(bg="#8fdbd9") #gives colour to the window

#name=Label(win,text="what is your name",font=("Comic Sans Ms",15),bg="#264b5e",fg="#a4ebb8",width=30,height=8)
#name.grid(row=0,column=0) #position label is placed

name=Label(win,text="label1",bg="#327da8",width=60,height=8)
name.grid(row=0,column=0,columnspan=2)

name=Label(win,text="label2",bg="#90d6b4",width=30, height=8)
name.grid(row=0, column=2)

name=Label(win,text="label3",bg="#66CDAA",width=30,height=10)
name.grid(row=1,column=0)

name=Label(win,text="label4",bg="#48D1CC",width=30, height=10)
name.grid(row=1, column=1)

name=Label(win,text="label5",bg="#C71585",width=30, height=10)
name.grid(row=1, column=2)

win.mainloop()
