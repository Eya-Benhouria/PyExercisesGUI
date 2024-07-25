'''
Created on Jun 18, 2020

@author: Eloll
'''

import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
r = Tk()
def is_distinct(str):
    for x in range(0 , len(str)):
        if (str.rfind(str[x] , x+1) != -1):
            return 0
    return 1
def ex10():
    str = nameEntered.get()
    try:
        int(str)
    except  :
        messagebox.showerror("error", "Veuillez saisir un nombre ")
        return 
    print(is_distinct(str))
    if(is_distinct(str)):
        label3.config(text="le nombre est distinct")
    else:
        label3.config(text="le nombre n'est pas distinct")
    
r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text="vérifier si un entier est distinct : "
,font=("lucida",20),bg="#666a66",fg='#ffbfdd')
labe2_title1.place(x=120, y=80)
nameEntered = ttk.Entry(r, width = 15,background='#666a66')
nameEntered.place(x=300, y=150)
label = ttk.Label(r, text = "",background='#666a66',foreground="#ffbfdd",font=("lucida",20))
label.pack(expand=YES)
label2= ttk.Label(r, text = "donner un nombre : ",background='red',foreground="white")
label2.place(x=160, y=150)
label3 = ttk.Label(r, text = "",background='#666a66',foreground="#ffbfdd",font=("lucida",20))
label3.place(x=300, y=250)
button = tk.Button(r, text = "valider l'operation",background="#41D1CC",foreground="white",command = ex10)
button.place(x=300, y=200)

label3 = ttk.Label(r, text = "",background='#666a66',foreground="#00FF00",font=("verdana",15))
label3.place(x=220, y=250)
r.mainloop()
