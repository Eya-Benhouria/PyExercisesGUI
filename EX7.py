
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
r = Tk()
def ex7():
    try:
        d = int(nameEntered1.get())
    except ValueError:
        messagebox.showerror(title="Error", message="VEUILLEZ ENTREZ UN JOUR",parent=r)
    try:
        m = int(nameEntered2.get())
    except ValueError:
        messagebox.showerror(title="Error", message="VEUILLEZ ENTREZ UN MOIS",parent=r)
    try:
        y = int(nameEntered3.get())
    except ValueError:
        messagebox.showerror(title="Error", message="VEUILLEZ ENTREZ UNE ANNEE",parent=r)
    else:
        d = int(nameEntered1.get())
        m = int(nameEntered2.get())
        y = int(nameEntered3.get())
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if m == 12:
                if d == 31:
                    y, m, d = y + 1, 1, 1
                else:
                    d += 1
            else:
                if d == 31:
                    m, d = m + 1, 1
                else:
                    d += 1
        elif m in [4, 6, 9, 10]:
            if d == 30:
                m, d = m + 1, 1
            else:
                d += 1
        else:
            if y % 4 == 0:
                if d == 29:
                    m, d = m + 1, 1
                else:
                    d += 1
            else:
                if d == 28:
                    m, d = m + 1, 1
                else:
                    d += 1
        date2 = str(d)+"/"+str(m)+ "/"+ str(y)
        label.config(text="la date du lendemain est: " + str(date2))
r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
labe2_title1 = Label(r, text="La Date Du Lendemain "
                     , font=("lucida", 20), bg="#666a66", fg='#ffbfdd')
labe2_title1.place(x=180, y=80)
fontStyle = tkFont.Font(family="verdana", size=10)
label1 = ttk.Label(r, text="donner le jour : ", background='red', foreground="white", width=15, font=fontStyle)
label1.place(x=180, y=180)
label2 = ttk.Label(r, text="donner le mois : ", background='red', foreground="white", width=20)
label2.place(x=180, y=210)
label3 = ttk.Label(r, text="donner l'année : ", background='red', foreground="white", width=20)
label3.place(x=180, y=240)
nameEntered1 = ttk.Entry(r, width=22, background='#666a66')
nameEntered1.place(x=310, y=180)
nameEntered2 = ttk.Entry(r, width=22, background='#666a66')
nameEntered2.place(x=310, y=210)
nameEntered3 = ttk.Entry(r, width=22, background='#666a66')
nameEntered3.place(x=310, y=240)
button = tk.Button(r, text="Résultat", background="#41D1CC", foreground="white", width=15, command=ex7)
button.place(x=270, y=300)
label= ttk.Label(r, text="", background='#666a66', foreground="#00FF00", font=("lucida", 15))
label.place(x=150, y=350)
r.mainloop()
