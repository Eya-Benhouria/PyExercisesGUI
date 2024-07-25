from tkinter import messagebox
import tkinter as tk

from tkinter import *
from tkinter import ttk

r = Tk()
l=[]
global j
i=0

def premier(n):
    if n==1:
        return 0
    else:
        i=2
        while i<=n//2 :
            if n%i ==0 :
                return 0
            i=i+1
    return 1
def super_premier(x):
    while x:
        if premier(x)==0:
            return 0
        x=x//10
    return 1
def taille(r,nameEntered):
    n_info=nameEntered.get()
    if n_info=='':
                nameEntered.delete(0,END)
                messagebox.showerror("Error","la taille de la liste ne doit pas etre vide",parent=r)
    elif n_info.isdigit()==False:
                nameEnterd.delete(0,END)
                messagebox.showerror("Error","la taille de la liste doit etre un entier",parent=r)
    elif(int(n_info)<=2)and(int(n_info)>30):
                nameEntered.delete(0,END)
                messagebox.showerror("Error","la taille de la liste doit etre >2 et <=30",parent=r)
    elif(int(n_info)>2)and(int(n_info)<=30):


                elem_text=Label(r,text="element"+str(j)+" de la liste")
                elem_text.place(x=200,y=200)
                ajout_element= ttk.Entry(r, width = 20)
                ajout_element.place(x=300, y=200)
                button_ajouter = tk.Button(r, text = "Ajouter",background="#41D1CC",foreground="white")
                button_ajouter.place(x=300, y=200)
                


def remplir(r,n_info,elem_text):
            global j
            ch=''
            cp=0
            if len(l)!=int(n_info):
                                x=name(0,END)
                                if x=='':
                                        name.delete(0,END)
                                        messagebox.showerror("Error","la taille de la liste ne doit pas etre vide",parent=r)
                                if x.isdigit()==False:
                                        name.delete(0,END)
                                        messagebox.showerror("Error","l'element de la liste doit etre un entier",parent=r)
                                if int(x)<0:
                                        name.delete(0,END)
                                        messagebox.showerror("Error","la taille de la liste doit etre positif",parent=main)
                                    
                                if int(x)>0:
                                        j+=1
                                        name(0,END)
                                        L.append(x)
                                        elem_text.config(text="element"+str(j)+"de la liste")
                
            else:
                messagebox.showinfo("information","la liste est déja remplie",parent=r)
                for i in l:
                        if(super_premier(int(i))):
                            cp=cp+1
                            ch=ch+'     '+str(i)
                if cp!=0:
                        continue_text=Label(r,"Resultat:les element",background='#666a66',foreground="#ffbfdd",font=("lucida",20))
                        continue_text.place(x=170,y=310)
                        resultat=Label(r,background='#666a66',foreground="#ffbfdd",font=("lucida",20))
                        resultat.place(x=250,y=340)
                else:
                        res=Label(r,"resultat : il n'existe pas des entiers super premier dans la liste",background='#666a66',foreground="#ffbfdd",font=("lucida",20))
                        res.place(x=170,y=330)
                


                        

    

r.geometry('640x480')
r.title("EX2TP5")
r.config(background='#666a66')
ch = tk.StringVar()
labe2_title1=Label(r,text="Un nombre est dit super premier s’il est premier et si en supprimant \n des chiﬀres a` partir de sa droite, le nombre restant est aussi premier "
,font=("lucida",15),bg="#666a66",fg='#ffbfdd')
labe2_title1.place(x=10, y=80)


label2= ttk.Label(r, text = "donner la taille de la liste: ",background='red',foreground="white")
label2.place(x=200, y=200)
nameEntered = ttk.Entry(r, width = 20)
nameEntered.place(x=300, y=200)
button = tk.Button(r, text = "DEFINIR",background="#41D1CC",foreground="white",command=remplir)
button.place(x=400, y=250)

r.mainloop()



