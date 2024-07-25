from tkinter import messagebox
import tkinter as tk

from tkinter import *
from tkinter import ttk

r = Tk()
def ex2():
    def premier(_entier):
        for i in range(2, int(_entier//2)):
            if( _entier%i == 0):
                return 0
        return 1

    def factorial(_entier):
        if _entier == 1:
            return 1
        else:
            return factorial(_entier - 1) * _entier

    def appending(_list, _size):
        for i in range(0, _size):
            x = int(input(">_"))
            _list.append(x)

    def sizing():
        _size = 0
        while(_size<5 or _size>50):
            print("The list size : ")
            _size = int(input(">_"))
        return _size

    def premier_factoriel(_entier):
        i = 1
        while( factorial(i) - 1 <= _entier):
            if(factorial(i) - 1 == _entier):
                return 1
            else:
                i = i+1
            i = 1
        while( factorial(i) + 1 <= _entier ):
            if(factorial(i) + 1 == _entier):
                return 1
            else:
                i = i+1
        return 0

    L = []
    size = sizing()
    appending(L, size)
    for i in range(0, size):
        if(premier(int(L[i])) == 1 and premier_factoriel(int(L[i])) == 1 ):
            print(L[i])
r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text="Un entier N est dit premier-factoriel s’il v´eriﬁe les deux propri´et´es suivantes :\n — N est premier \n — N s’´ecrit sous la forme d’une factorielle incr´ement´e ou d´ecr´ement´e de 1 \n( N=F! - 1 ou N=F! + 1).  "
,font=("lucida",13),bg="#666a66",fg='#ffbfdd')
labe2_title1.place(x=20, y=80)


label2= ttk.Label(r, text = "donner la taille de la liste: ",background='red',foreground="white")
label2.place(x=150, y=240)
nameEntered = ttk.Entry(r, width = 24)
nameEntered.place(x=300, y=240)

button = tk.Button(r, text = "DEFINIR",background="#41D1CC",foreground="white",width=15)
button.place(x=400, y=280)







r.mainloop()
