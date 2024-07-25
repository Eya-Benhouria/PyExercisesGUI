from tkinter import *



def importer(self):
     print("hello")
     const.MY_METHOD(my_variable)
def create_window1():
    
     window1=Toplevel(window)
     window1.title("TP4")
     window1.geometry("720x360")
     window1.config(background='#E9967A')




     bouton_c1=Button(window1,text="EXERCICE 7",width=10,command=importer)
     bouton_c1.pack(side=LEFT,padx=40)
     bouton_c2=Button(window1,text="EXERCICE 8",width=10)
     bouton_c2.pack(side=LEFT,padx=40)
     bouton_c3=Button(window1,text="EXERCICE 9",width=10)
     bouton_c3.pack(side=LEFT,padx=40)
     bouton_c4=Button(window1,text="EXERCICE 10",width=10)
     bouton_c4.pack(side=LEFT,padx=40)
def create_window2():
    
     window2=Toplevel(window)
     window2.title("TP5")
     window2.geometry("720x360")
     window2.config(background='#E9967A')

     bouton_cc1=Button(window2,text="EXERCICE 1",width=10)
     bouton_cc1.pack(side=LEFT,padx=10)
     bouton_cc2=Button(window2,text="EXERCICE 2",width=10)
     bouton_cc2.pack(side=LEFT,padx=10)
     bouton_cc3=Button(window2,text="EXERCICE 3",width=10)
     bouton_cc3.pack(side=LEFT,padx=10)
     bouton_cc4=Button(window2,text="EXERCICE 4",width=10)
     bouton_cc4.pack(side=LEFT,padx=10)
     bouton_cc5=Button(window2,text="EXERCICE 5",width=10)
     bouton_cc5.pack(side=LEFT,padx=10)
     
def create_window3():
    
     window3=Toplevel(window)
     window3.title("TP6")
     window3.geometry("720x360")
     window3.config(background='#E9967A')
     bouton_ccc1=Button(window3,text="EXERCICE 1",width=10)
     bouton_ccc1.pack(side=LEFT,padx=10)
     bouton_ccc2=Button(window3,text="EXERCICE 2",width=10)
     bouton_ccc2.pack(side=LEFT,padx=10)
     bouton_ccc3=Button(window3,text="EXERCICE 3",width=10)
     bouton_ccc3.pack(side=LEFT,padx=10)
     bouton_ccc4=Button(window3,text="EXERCICE 4",width=10)
     bouton_ccc4.pack(side=LEFT,padx=10)
     bouton_ccc5=Button(window3,text="EXERCICE 5",width=10)
     bouton_ccc5.pack(side=LEFT,padx=10)
     bouton_ccc6=Button(window3,text="EXERCICE 6",width=10)
     bouton_ccc6.pack(side=LEFT,padx=10)
     
     
     

     
window=Tk()
window.title("TP PYTHON")
window.geometry("1080x720")
window.config(background='#E9967A')





label_title=Label(window,text="DES EXERCICES EN PYTHON",font=("courier",30))
label_title.pack()




bouton_1=Button(window,text="TP4",width=10,command=create_window1)
bouton_1.pack(side=LEFT,padx=70)
bouton_2=Button(window,text="TP5",width=10,command=create_window2)
bouton_2.pack(side=LEFT,padx=70)
bouton_3=Button(window,text="TP6",width=10,command=create_window3)
bouton_3.pack(side=LEFT,padx=70)
bouton_4=Button(window,text="QUITTER",width=10,command=window.quit)
bouton_4.pack(side=LEFT,padx=70)





window.mainloop()
