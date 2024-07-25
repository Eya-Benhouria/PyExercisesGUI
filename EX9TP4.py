
from tkinter import *
def ex9():
    
    s0, s1= 2, 3
    for i in range(2, 21):
        s = s1 + (-1)**i * s0
        s0 = s1
        s1 = s
    lbl2.config(text=s)
    print("s20 = ",s)

    
    
    

    
fenex9tp4=Tk()
fenex9tp4.title("EX9TP4")
fenex9tp4.geometry("640x480")
fenex9tp4.config(background='#666a66')
label_title1=Label(fenex9tp4,text="un programme qui d´etermine le 20ieme terme d une suite deﬁnie par: \n S0 = 2 S1 = 3  :",font=("verdana",13),bg="#666a66",fg='#ffbfdd')
label_title1.place(x=20,y=70)


    



# AJOUTER LE BOUTON VALIDER
valider=Button(fenex9tp4, text="valider l'operation",background="#41D1CC",foreground="white",command=ex9)
valider.place(x=280,y=250)

    
lbl2=Label(text='',background='#666a66',foreground="#00FF00",font=("verdana",20))
lbl2.place(x=300,y=350)


fenex9tp4.mainloop()



