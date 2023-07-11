
from tkinter import *



window = Tk()
window.geometry("500x500")
window.title("Basic Calculator")

def ButtonPress(KeyPressed):
    global TextLabel
    TextLabel += str(KeyPressed)
    DisplayLabel.set(TextLabel)

def EqualPress():
    global TextLabel
    Result=str(eval(TextLabel))
    DisplayLabel.set(Result)
    TextLabel=Result

def ClearPress ():
    global TextLabel
    DisplayLabel.set("")
    TextLabel=""
    

TextLabel=""
DisplayLabel = StringVar()
DisplayScreen = Label(window,textvariable=DisplayLabel, font=("roboto",25), bg="white", width= 24, height= 2)
DisplayScreen.pack()

frame=Frame(window)
frame.pack()

Button1= Button(frame,text=1,height=3,width=7,font= 30, command=lambda:ButtonPress(1))
Button1.grid(row=0,column=0)
 
Button2= Button(frame,text=2,height=3,width=7,font= 30, command=lambda:ButtonPress(2))
Button2.grid(row=0,column=1)

Button3= Button(frame,text=3,height=3,width=7,font= 30, command=lambda:ButtonPress(3))
Button3.grid(row=0,column=2)
 
Button4= Button(frame,text=4,height=3,width=7,font= 30, command=lambda:ButtonPress(4))
Button4.grid(row=1,column=0)

Button5= Button(frame,text=5,height=3,width=7,font= 30, command=lambda:ButtonPress(5))
Button5.grid(row=1,column=1)
 
Button6= Button(frame,text=6,height=3,width=7,font= 30, command=lambda:ButtonPress(6))
Button6.grid(row=1,column=2)

Button7= Button(frame,text=7,height=3,width=7,font= 30, command=lambda:ButtonPress(7))
Button7.grid(row=2,column=0)
 
Button8= Button(frame,text=8,height=3,width=7,font= 30, command=lambda:ButtonPress(8))
Button8.grid(row=2,column=1)

Button9= Button(frame,text=9,height=3,width=7,font= 30, command=lambda:ButtonPress(9))
Button9.grid(row=2,column=2)

Button0= Button(frame,text=0,height=3,width=7,font= 30, command=lambda:ButtonPress(0))
Button0.grid(row=3,column=1)

ButtonAdd= Button(frame,text="+",height=3,width=7,font= 30, command=lambda:ButtonPress("+"))
ButtonAdd.grid(row=0,column=3)

ButtonSubt= Button(frame,text="-",height=3,width=7,font= 30, command=lambda:ButtonPress("-"))
ButtonSubt.grid(row=1,column=3)

ButtonMult= Button(frame,text="*",height=3,width=7,font= 30, command=lambda:ButtonPress("*"))
ButtonMult.grid(row=2,column=3)

ButtonDivd= Button(frame,text="/",height=3,width=7,font= 30, command=lambda:ButtonPress("/"))
ButtonDivd.grid(row=3,column=3)

ButtonEql= Button(frame,text="=",height=3,width=7,font= 30, command=EqualPress)
ButtonEql.grid(row=3,column=2)

ButtonClear= Button(frame,text="C",height=3,width=7,font= 30, command=ClearPress)
ButtonClear.grid(row=3,column=0)

window.mainloop()
