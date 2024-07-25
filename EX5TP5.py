from tkinter import messagebox
import tkinter as tk

from tkinter import *
from tkinter import ttk
r = Tk()
def ex5():
    string = nameEntered.get()
    
        
    cle = "HYLUJPVREAKBNDOFSQZCWMGITX"
    crypted_string = ""
    for char in string:
        crypted_string += cle[ord(char) - 65]
    label.config(text ="Résultat: "+crypted_string)


r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text="Cryptage d'une chaine : "
,font=("lucida",20),bg="#666a66",fg='#ffbfdd')
labe2_title1.place(x=170, y=80)
nameEntered = ttk.Entry(r, width = 15, textvariable = ch)
nameEntered.place(x=300, y=200)
label = ttk.Label(r, text = "",background='#666a66',foreground="#00FF00",font=("lucida",20))
label.place(x=220,y=300)
label2= ttk.Label(r, text = "donner une chaine : ",background='red',foreground="white")
label2.place(x=180, y=200)

button = tk.Button(r, text = "valider l'operation",background="#41D1CC",foreground="white",command = ex5)
button.place(x=300, y=250)



r.mainloop()
