"""from tkinter import *


def submit():
    user.config(state=DISABLED)
    print(user.get())


def remove():
    user.delete(0,len(user.get()))



def delete():
    user.delete(len(user.get())-1,len(user.get()))


window = Tk()
# window.geometry("400x200")

user = Entry(window,font=('Ink free',50),bg='#111111',fg='#00FF00',width=10)
b1 = Button(window, text="Submit", command=submit)
b2 = Button(window, text="Remove", command=remove)
b3 = Button(window, text="Delete", command=delete)
user.pack(side = LEFT)
b1.pack(side = RIGHT)
b2.pack(side = RIGHT)
b3.pack(side = RIGHT)
window.mainloop()"""

"""import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple de boutons")

# Création des boutons
bouton1 = tk.Button(fenetre, text="Open")
bouton2 = tk.Button(fenetre, text="Save")

# Placement des boutons en haut, au centre, côte à côte
fenetre.columnconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.columnconfigure(2, weight=1)

bouton1.grid(row=0, column=1, sticky='e')
bouton2.grid(row=0, column=2, sticky='w')

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()"""

from tkinter import *
from time import *

window = Tk()
def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d,%Y")
    dateLabel.config(text=timeString)

    timeLabel.after(1000,update)
timeLabel = Label(window,font=('Arial',50),fg = "#00FF00",bg='black')
timeLabel.pack()

dayLabel = Label(window,font=('Ink Free',25))
dayLabel.pack()

dateLabel = Label(window,font=('Ink Free',25))
dateLabel.pack()

update()
window.mainloop()







