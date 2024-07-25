'''
Created on Jun 17, 2020

@author: Ellol
'''

#!/bin/python3

from tkinter import messagebox
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
r = Tk()

def ex2():
    string=nameEntered.get()
    if(len(string) > 50):
        messagebox.showwarning("Warning", "Length Of Value > 50")
        return
    elif( not len (string.split())):
        messagebox.showwarning("Warning", "Veuillez ecrire un mot")
        return
    new_string, count = "",1
    for index, c in enumerate(string):
        if index +1 == len(string):
            if c == string[index-1]:
                new_string += f"{count}{c}"
            else: new_string += f"1{c}"
        else:
            if c == string[index+1]:
                count +=1
            else:
                new_string += f"{count}{c}"
                count = 1
    label.config(text ="Résultat: "+ new_string)

 
r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text=" Programme Python permettant de saisir la chaine CH \n qui doit ˆetre non vide et form´ee uniquement par des lettres alphab´etiques, \n puis de former et d’aﬃcher l'occurence de chaque caractére dans la chaine"
,font=("lucida",13),bg="#666a66",fg='#ffbfdd')

labe2_title1.place(x=30, y=50)
nameEntered = ttk.Entry(r, width = 20, textvariable = ch)
nameEntered.place(x=300, y=200)
label = ttk.Label(r, text = "",background='#666a66',foreground="#00FF00",font=("lucida",20))
label.place(x=230,y=300)
label2= ttk.Label(r, text = "donner un mot : ",background='red',foreground="white")
label2.place(x=180, y=200)

button = tk.Button(r, text = "valider l'operation",background="#41D1CC",foreground="white",command = ex2)
button.place(x=260, y=250)
r.mainloop()
