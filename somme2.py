from tkinter import messagebox
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
r = Tk()

def somme2():

    global s2
    
    n = int(nameEntered.get())
    
       
    s2 = sum([1/i for i in range(1, n+1) if i % 2 == 0], 1)
    
    lbl2.config(text="Résultat: "+str(s2))
    print("s1 = ", s2)








r.geometry('640x480')
r.title("somme2")
r.config(background='#666a66')
ch = tk.StringVar()
TEXT=" Ecrire un programme qui permet de saisir N>1 et de calculer S2 \n la somme est S1=1+1/2+1/3 + 1/6 + ...... + 1/N"
labe2_title1=Label(r,text=TEXT,

font=("lucida",15),bg="#666a66",fg='#ffbfdd')

labe2_title1.place(x=50,y=80)
nameEntered = ttk.Entry(r, width = 15,background='#666a66')
nameEntered.place(x=330, y=200)

label2= ttk.Label(r, text = "donner N : ",background='red',foreground="white")
label2.place(x=250, y=200)
label3 = ttk.Label(r, text = "",background='#666a66',foreground="#ffbfdd",font=("verdana",15))
label3.place(x=200, y=250)
labe2_title1.place(x=50,y=80)
button = tk.Button(r, text = "valider l'operation",background="#41D1CC",foreground="white",command=somme2)
button.place(x=270, y=250)
lbl2=Label(text='',background='#666a66',foreground="#00FF00",font=("lucida",20))
lbl2.place(x=250,y=300)
r.mainloop()
