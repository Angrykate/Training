from tkinter import *

"""window = Tk()
window.title('Exercice 293-295')
window.geometry('400x200')

b1 = Button(text='Button 1')
b2 = Button(text='Button 2')
b3 = Button(text='Button 3')
b4 = Button(text='Button 4')

# b1.grid(row = 0,column=0,padx = 10,pady = 10)
# b2.grid(row = 0,column=1,padx = 10,pady = 10)
# b3.grid(row = 1,column=0,padx = 10,pady = 10)
# b4.grid(row = 1,column=1,padx = 10,pady = 10)
b1.place(x = 50,y = 50,width=100)
b2.place(x = 200,y = 50,width=100)
b3.place(x =50,y=100,width=100)
b4.place(x = 200,y = 100,width=100)
window.mainloop()"""

"""window2 = Tk()
window2.title('Exercice 296')
window2.geometry("300x100")

def click(event):
    window2.quit()
b1 = Button(text='Fermer la fenêtre',command=quit)
b2 = Button(text='Fermer la fenêtre')
b2.bind('<Button>',click)
b1.pack()
b2.pack()
window2.mainloop()"""

"""window3 = Tk()
window3.title('Exercice 297-298')
window3.geometry('400x200')

def afficher():
    var.set('Hello world!')
    lbl.config(font=('Arial',50),fg='#00FF00',bg='black')

Boutton = Button(text='Affichage',command=afficher)
var =StringVar()
lbl = Label(textvariable=var)
lbl.pack()
Boutton.pack(pady = 30)
window3.mainloop()"""

"""window4 = Tk()
window4.title('Exercice 299-300')
window4.geometry('400x200')


def Affichage(event):
    affichage.config(text=userInput.get())
    userInput.delete(0,len(userInput.get()))


message = Label(text='Enter your name :')
userInput = Entry()
userInput.bind('<Return>',Affichage)
# submit = Button(text='Valider', command=Affichage)
affichage = Label(text='')

message.grid(row = 0,column = 0,padx = 10)
userInput.grid(row = 0,column =1,pady = 10)
# submit.grid(row = 1,column =0)
affichage.grid(row = 1,column =1)
window4.mainloop()"""

"""window5 = Tk()
window5.title('Exercice 301')
window5.geometry('400x200')

def affichage(event):
    nombre = str(2*int(user.get()))
    user2.delete(0,END)
    user2.insert(0,nombre)

def ent(event):
    user2.config(state=DISABLED)
def sort(event):
    user2.config(state=NORMAL)
message1 = Label(text='Enter the value of N')
message2 = Label(text='Here is the value of 2*N')
user = Entry()
user2 = Entry()
user.bind('<Return>',affichage)
user2.bind('<Enter>',ent)
user2.bind('<Leave>',sort)
message1.grid(row = 0,column = 0,padx = 10,pady = 10)
message2.grid(row = 1,column = 0,padx = 10)
user.grid(row = 0,column = 1,padx = 10)
user2.grid(row = 1,column = 1,padx = 10)
window5.mainloop()"""

"""window6 = Tk()
window6.title('Exercice 302')
window6.geometry('400x200')

def Affichage():
    n = int(user.get())
    Liste = [str(x) for x in range(1,n+1) if n%x==0 ]
    affListe = '      '.join(Liste)
    message.config(text=affListe)
message1 = Label(text='Enter the value of N')
message2 = Label(text='The divisor of N :')
message = Label(text='')
submit = Button(text='Validate', command=Affichage)
user = Entry()
message1.grid(row = 0,column = 0,padx = 10,pady = 10)
message2.grid(row = 1,column = 0,padx = 10,pady = 10)
message.grid(row = 1,column = 1,padx = 10,pady = 10)
user.grid(row = 0,column = 1,padx = 10,pady = 10)
submit.grid(row = 2,column = 0,columnspan = 2,padx = 10,pady = 10)
window6.mainloop()"""

"""window7 = Tk()
window7.title('Exercice 303')
window7.geometry("350x150")
def select(event):
    n = int(spin.get())
    window7.geometry("{}x{}".format(350 + 10*n,150 + 10*n))

lab = Label(window7,text='Resize window')
spin = Spinbox(window7,from_=1,to=25)
spin.bind('<Button-1>',select)
lab.pack()
spin.pack()
window7.mainloop()"""

"""window8 = Tk()
window8.title('Exercice 304')
window8.geometry('400x200')


def change(event):
    window8.config(bg='yellow')

def change2(event):
    window8.config(bg='Black')

window8.bind("<Enter>", change)
window8.bind("<Leave>", change2)
window8.mainloop()"""

"""from tkinter import ttk
from math import gcd
window9 = Tk()
window9.title('Exercice 305-306')
window9.geometry('350x170')
lab1 = Label(window9,text='Enter value of m :')
lab2 = Label(window9,text='Enter value of n :')
lab3 = Label(window9,text=' Choose function :')
entry1 = Entry(window9)
entry2 = Entry(window9)
selection = ttk.Combobox(window9,values=["PGCD","PPCM"])
Input = Label(window9, text='')

lab1.place(x=10,y = 20,width = 150)
lab2.place(x=10,y = 45,width = 150)
lab3.place(x=10,y = 70,width = 150)
entry1.place(x=150,y = 20,width = 165)
entry2.place(x=150,y = 45,width = 165)
selection.place(x=150,y = 70,width = 165)
Input.place(x=150,y = 95)

# def PGCD(a,b):
#     l = []
#     for i in range(1,min(a,b)+1):
#         if a%i == 0 and b%i == 0:
#             l.append(i)
#     return max(l)
def calcul(event):
    m = int(entry1.get())
    n = int(entry2.get())
    if selection.get()=='PGCD':
        x = gcd(m,n)
        af = "PGCD  = "+str(x)
        Input.config(text=af)
    else:
        x = abs(m*n)//gcd(m,n)
        af = "PPCM  = " + str(x)
        Input.config(text=af)

selection.bind("<<ComboboxSelected>>",calcul)

window9.mainloop()"""

from tkinter import ttk

window10 = Tk()
window10.title('Exercice 307')
window10.geometry('400x200')


def multiplication(a):
    l = ''
    for i in range(1, 10):
        l += str(i) + "   x   " + str(a) + "   =   " + str(i * a) + '\n'
    return l


def display(event):
    saisi = selection.get()
    nombre = saisi.split(' : ')[1]
    affichage.config(text=multiplication(int(nombre)))


table = ["Table de multiplication de : " + str(x) for x in range(1, 8)]
selection = ttk.Combobox(window10, values=table,width=25)
selection.bind("<<ComboboxSelected>>", display)
affichage = Label(window10, text='')
selection.pack(pady = 10)
affichage.pack()
window10.mainloop()


