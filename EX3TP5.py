import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
r = Tk()
def ex3():
    def saisie():
        while True:
            try:
                x = int(nameEntered.get())
            except ValueError:
                messagebox.showerror(title="Error",message="Veuillez entrez un nombre",parent=r)
            if (-1 <= x <= 1):
                break;
            return x
    def FACT(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
    def Calcul_Cos(x):
        elm1 = 1
        elm2 = elm1 - (x ** 2 / 2)
        signe = 1
        puis = 2
        i = 2
        while abs(elm2 - elm1) > 0.0001:
            i += 2
            f = FACT(i)
            elm1 = elm2
            elm2 = elm1 + signe * (x ** i / f)
            signe *= (-1)
        return elm2
    x = saisie()
    label3.config(text="Résultat: " + str(Calcul_Cos(x)))
r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
labe2_title1 = Label(r, text="calcul du cosinus d'un nombre : "
                     , font=("lucida", 20), bg="#666a66", fg='#ffbfdd')
labe2_title1.place(x=120, y=80)
nameEntered = ttk.Entry(r, width=20, background='#666a66')
nameEntered.place(x=300, y=150)
label = ttk.Label(r, text="", background='#666a66', foreground="#ffbfdd", font=("lucida", 20))
label.pack(expand=YES)
label2 = ttk.Label(r, text="donner un nombre : ", background='red', foreground="white")
label2.place(x=180, y=150)
label3 = ttk.Label(r, text="", background='#666a66', foreground="#00FF00", font=("verdana", 15))
label3.place(x=150, y=300)
button = tk.Button(r, text="valider l'operation", background="#41D1CC", foreground="white", width=15, command=ex3)
button.place(x=270, y=220)
r.mainloop()
