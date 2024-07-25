import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
r = Tk()

vVals = { "A" : 1 , "E" : 5 , "I" : 9 , "O" : 15 , "U" : 21 , "Y" : 25 }

#------------------ Func To Get Weight --------------------#

#test ---------> t = 0 , e = 5 * 2 , s = 0 , t = 0 


def getWeight(str , vVals):
    val = 0
    str = str.upper()
    for x in range(len(str)):
        #print(str[x])
        if (str[x] in vVals.keys()):
            
            val = val +  (x + 1 )* vVals[str[x]]
            print(val)
    return val
#------------------------------------------------#
def func():
    global vVals
    str = nameEntered.get()
    if( not len(str.split())):
        messagebox.showwarning("Warning", "ECRIRE UN MOT ")
        return 
    val =  getWeight(str, vVals)
    label.config(text = val)
r.geometry('640x480')
r.title("EX1TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text="Un programme Python qui permet de lire une chaine non vide, \n compos´ee seulement par des lettres alphab´etiques majuscules \n puis calcule  et aﬃche le poids de cette chaine. " , font=("verdana",13), bg="#666a66",fg='#ffbfdd')
 

labe2_title1.place(x=30, y=50)
nameEntered = ttk.Entry(r, width = 15, textvariable = ch)
nameEntered.place(x=300, y=200)
label = ttk.Label(r, text = "",background='#666a66',foreground="#ffbfdd",font=("verdana",20))
label.place(x=300,y=300)
label2= ttk.Label(r, text = "donner un mot : ",background='red',foreground="white")
label2.place(x=180, y=200)

button = tk.Button(r, text = "valider l'operation",background="#41D1CC",foreground="white",command = func)
button.place(x=300, y=250)
r.mainloop()
