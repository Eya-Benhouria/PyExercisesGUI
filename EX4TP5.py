import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
r = Tk()
def ex4():
    try:
        u = int(nameEntered.get())
    except ValueError:
        messagebox.showerror(title="",message="Veueillez entrer un nombre")
    while u >= 40 and u < 3:
        try:
            u = int(nameEntered.get())
        except ValueError:
            messagebox.showerror(title="Error", message="Veuillez entrez un nombre", parent=r)
    rang = 1
    while u != 4:
        if u % 2 == 0:
            u //= 2
        else:
            u = 3 * u + 1
        rang += 1
    label3.config(text="Résultat: " + str(rang))
r.geometry('640x480')
r.title("EX4TP5")
r.config(background='#666a66')
labe2_title1 = Label(r,
                     text=" un programme permettant de d´eterminer le rang `a partir du quel \n la suite U aboutit au cycle redondant 4, 2 et 1"
                     , font=("lucida", 15), bg="#666a66", fg='#ffbfdd')
labe2_title1.place(x=30, y=60)
nameEntered = ttk.Entry(r, width=20, background='#2B2726')
nameEntered.place(x=300, y=200)
label = ttk.Label(r, text="", background='#666a66', foreground="#ffbfdd", font=("lucida", 20))
label.pack(expand=YES)
label2 = ttk.Label(r, text="donner un nombre de la suite : ", background='red', foreground="white")
label2.place(x=120, y=200)
label3 = ttk.Label(r, text="", background='#666a66', foreground="#00FF00", font=("lucida", 15))
label3.place(x=250, y=340)
button = tk.Button(r, text="valider l'operation", background="#41D1CC", foreground="white", command=ex4)
button.place(x=300, y=280)
r.mainloop()

