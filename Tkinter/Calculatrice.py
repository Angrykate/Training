from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculatrice minimaliste')
root.geometry("500x500")

formule = ''


# Definition des fonctions
def click(n):
    global formule
    if not formule:
        delete()
    equation.insert(END, n)
    formule += str(n)


def equal():
    try:
        global formule
        resultat = eval(formule)
        equation.delete(0, END)
        equation.insert(0, resultat)
        formule = ''
    except:
        equation.delete(0, END)
        equation.insert(0, 'ERROR')
        formule = ''


def remove():
    global formule
    equation.delete(len(formule) - 1, END)
    formule = equation.get()


def delete():
    global formule
    equation.delete(0, END)
    formule = ''


def square():
    global formule
    try:
        resultat = int(formule) ** (1 / 2)
        equation.delete(0, END)
        equation.insert(0, resultat)
        formule = ''
    except:
        equation.delete(0, END)
        equation.insert(0, 'ERROR')
        formule = ''


# Création des bouttons
btn_0 = Button(root, text='0', width=15, height=4, command=lambda: click(0))
btn_1 = Button(root, text='1', width=15, height=4, command=lambda: click(1))
btn_2 = Button(root, text='2', width=15, height=4, command=lambda: click(2))
btn_3 = Button(root, text='3', width=15, height=4, command=lambda: click(3))
btn_4 = Button(root, text='4', width=15, height=4, command=lambda: click(4))
btn_5 = Button(root, text='5', width=15, height=4, command=lambda: click(5))
btn_6 = Button(root, text='6', width=15, height=4, command=lambda: click(6))
btn_7 = Button(root, text='7', width=15, height=4, command=lambda: click(7))
btn_8 = Button(root, text='8', width=15, height=4, command=lambda: click(8))
btn_9 = Button(root, text='9', width=15, height=4, command=lambda: click(9))

btn_add = Button(root, text='+', width=15, height=4, command=lambda: click('+'))
btn_sub = Button(root, text='-', width=15, height=4, command=lambda: click('-'))
btn_mul = Button(root, text='*', width=15, height=4, command=lambda: click('*'))
btn_div = Button(root, text='/', width=15, height=4, command=lambda: click('/'))
btn_dot = Button(root, text='.', width=15, height=4, command=lambda: click('.'))
btn_equal = Button(root, text='=', width=15, height=4, command=equal)

btn_remove = Button(root, text='M', width=15, height=4, command=remove)
btn_delete = Button(root, text='effacer', width=15, height=4, command=delete)
btn_mod = Button(root, text='%', width=15, height=4, command=lambda: click('%'))
btn_unknow = Button(root, text='√', width=15, height=4, command=square)

# Création du champ de saisi
equation = Entry(root, font=(("Amasis MT Pro Black"), 30))

# Disposition
equation.grid(row=0, column=0, columnspan=4, pady=40)

btn_1.grid(row=1, column=0, padx=5)
btn_2.grid(row=1, column=1, padx=5)
btn_3.grid(row=1, column=2, padx=5)
btn_add.grid(row=1, column=3, padx=5)

btn_4.grid(row=2, column=0, padx=5)
btn_5.grid(row=2, column=1, padx=5)
btn_6.grid(row=2, column=2, padx=5)
btn_sub.grid(row=2, column=3, padx=5)

btn_7.grid(row=3, column=0, padx=5)
btn_8.grid(row=3, column=1, padx=5)
btn_9.grid(row=3, column=2, padx=5)
btn_mul.grid(row=3, column=3, padx=5)

btn_0.grid(row=4, column=0, padx=5)
btn_dot.grid(row=4, column=1, padx=5)
btn_equal.grid(row=4, column=2, padx=5)
btn_div.grid(row=4, column=3, padx=5)

btn_delete.grid(row=5, column=0, padx=5)
btn_mod.grid(row=5, column=1, padx=5)
btn_unknow.grid(row=5, column=2, padx=5)
btn_remove.grid(row=5, column=3, padx=5)

root.mainloop()
