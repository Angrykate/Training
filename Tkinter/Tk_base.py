from tkinter import *

"""Partie Bouton

window = Tk()
window.title("My first GUI")
window.geometry('400x200')


def action():
    print("ton")


button = Button(window, text='voici un bouton', command=quit, width=20,height=4,relief=GROOVE, bg="yellow",font=('broadway',18))
button.pack()
window.mainloop()"""

"""Partie Label

window2 = Tk()
window2.title('Label version')
window2.geometry('400x200')

def action():
    var.set("Texte changer")

var = StringVar()
lab = Label(window2, textvariable=var, relief=RAISED,font=("broadway",18),bg='yellow',wraplength=150 )
var.set('VOICI UN  EXEMPLE DE LABEL AVEC OPTION ')
lab.pack()

window2.mainloop()"""

"""Partie Entry

window3 = Tk()
window3.title("Entry version")
window3.geometry("400x200")

def even_action(even):
    user.config(text= "Vous avez tapé = "+ user_entry.get())


user_entry = Entry(window3)
user_entry.bind("<Return>",even_action)
user_entry.pack()
user = Label(window3,text="... ")
user.pack()

window3.mainloop()"""

"""Partie Text

window4 = Tk()
window4.title("Version texte")
window4.geometry("400x200")
def sub():
    print(t.get('1.0',END))
t = Text(window4,fg='red',padx=10)
b = Button(window4,text='submit',command=sub)
t.config(font=('Arial',14))
t.insert(0.0,"Exemple de widget Text Tkinter")

t.pack()
b.pack()
window4.mainloop()"""

"""Partie Frame

window5 = Tk()
window5.title("Version Frame")
window5.geometry("400x200")
fra = Frame(window5,bg='green')
fra.place(x=50,y=20,width=200,height=75)

b=Button(fra,text="Un bouton",bg='red',fg='white',command=exit)
b.place(x=10,y=10,width=100,height=30)

window5.mainloop()"""

"""Partie Scale

window6 = Tk()
window6.title("Version Scale")
window6.geometry("400x200")

i = 0
def count():
    global i
    i+=1
    l.config(text=i)
    l.config(font= 'Monospace',fg='red',bg='pink',padx=30)
    if i>10:
        l.config(fg='yellow',bg='purple',padx=30)
    if i==20:
        button.config(state=DISABLED)

l = Label(window6,text='')
l.pack()
v = IntVar()
scale = Scale(window6,variable=v,from_=0,to=30,orient=HORIZONTAL,length=200,tickinterval=5)
scale.pack(anchor=CENTER)
button = Button(window6, text='Get skale value',command=count)
button2 = Button(window6, text='Quitter',command=quit)
button.pack()
button2.pack()
window6.mainloop()"""

"""Partie Listboxes

window7 = Tk()
window7.title("Version listboxes")

def submit():
    if not listbox.curselection():
        print('Nothing')
        return

    print('I love:')
    for i in listbox.curselection():
        print(listbox.get(i))
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

listbox = Listbox(window7,bg='#f7ffde',font=(('constentia'),30),width=10,selectmode=MULTIPLE)
listbox.pack()

listbox.insert(0,'Pizza')
listbox.insert(1,'Tomatoes')
listbox.insert(2,'Pomme')
listbox.config(height=listbox.size())

submitButton = Button(window7,text='Submit',command=submit)
addButton = Button(window7,text='add',command=add)
deleteButton = Button(window7,text='delete',command=delete)
entry = Entry(window7)
entry.pack()
submitButton.pack()
addButton.pack()
deleteButton.pack()

window7.mainloop()"""

"""Partie Messagebox
from tkinter import messagebox
window8 = Tk()
window8.title("Version Messagebox")
def click():
    messagebox.showinfo(title='This is a info',message='Hi everybody i\'m a person')
    messagebox.showwarning(title='This is a warning',message='Hi everybody i\'m a virus')
    messagebox.showerror(title='This is a info',message='Hi everybody i\'m a bug')
def quitter():
    rep = messagebox.askyesnocancel(title='Terminer le script',message='Are you sure you want to quit?')
    print(rep)
    if rep:
        window8.quit()
button = Button(window8,text='Click me',command=click,font=(('Arial'),25))
button2 = Button(window8,text='Quitter',command=quitter,font=(('Arial'),25))

button.grid(row = 0,column=0)
button2.grid(row = 0,column=1)
window8.mainloop()"""

"""Partie colorchooser
from tkinter import colorchooser
window9 = Tk()
window9.title('Version colorchooser')
window9.geometry('400x400')
def click():
    color = colorchooser.askcolor()
    window9.config(bg= color[1])
b =  Button(window9,text='Click on me',command=click)
b.pack()
window9.mainloop()"""

"""Partie file
from tkinter import filedialog
window10 = Tk()
window10.title('Version file')
def openFile():
    filepath = filedialog.askopenfilename(title='Ok Bro',filetypes=[("Text File",".txt"),("Html",".html"),("Pdf",".pdf"),("All files",".*")])
    with open(filepath,'r') as file:
        print(file.read())
def saveFile():
    file = filedialog.asksaveasfile(title='If you want',defaultextension= '.txt',filetypes=[("Text File",".txt"),("Html",".html"),("Pdf",".pdf"),("All files",".*")])
    if file is None:
        return 
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()
buton = Button(window10,text='open',command=openFile)
button = Button(window10,text='save',command=saveFile)
text= Text(window10)
buton.pack()
button.pack()
text.pack()
window10.mainloop()"""

"""Partie Menu

import os
def new():
    os.popen("python Tk_base.py")

window11 = Tk()
menubar = Menu(window11)
menufichier = Menu(menubar,tearoff=0)
menufichier2 = Menu(menubar,tearoff=1)
menubar.add_cascade(label='Fichier',menu=menufichier)
menubar.add_cascade(label='Edit',menu=menufichier2)
menufichier.add_command(label='Nouveau',command=new)
menufichier.add_command(label='Ouvrir')
menufichier.add_separator()
menufichier.add_command(label='Quitter',command=quit)
menufichier2.add_command(label='Copier')
menufichier2.add_command(label='Couper')
window11.config(menu=menubar)
window11.mainloop()"""

"""Partie window

window12 = Tk()
def create_window():
    new =Tk()
    window12.destroy()
Button(window12,text='Create a new window',command=create_window).pack()
window.mainloop()"""

"""Partie progressbar
from tkinter.ttk import *
import time

window13 = Tk()
window13.title('version progressbar')
def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + '%')
        test.set(str(download) + '/' + str(GB) + " GB completed")
        window13.update_idletasks()
bar = Progressbar(window, length=300)
bar.pack(pady=10)
percent = StringVar()
test = StringVar()
Label(window13, textvariable=percent).pack()
Label(window13, textvariable=test).pack()
Button(window13, text='Download', command=start).pack()
window13.mainloop()"""

"""Partie Canvas
from tkinter import Canvas
window14 =Tk()
window14.title('Version canvas')
canva = Canvas(window14,height=500,width=500)
# canva.create_line(0,500,500,0,width=3,fill='maroon')
# canva.create_rectangle(100,200,400,400,fill='yellow')
# canva.create_polygon(10,10,490,10,250,490,fill='yellow',outline='black',width=3)
canva.create_arc(0, 0, 500, 500, start=0, extent=180, fill="red", style=CHORD,width =10)
canva.create_arc(0, 0, 500, 500, start=180, extent=180, fill="white", style=CHORD,width = 10)
canva.create_oval(190,190,310,310,fill = 'white',width=10)
canva.pack()
window14.mainloop()"""

"""Partie evenement

window15 = Tk()

def callable(even):
    frm.focus_set()
    print("Vous avez cliquer à la position {} et {}".format(even.x,even.y))
    print(even.num)

def key(even):
    print("Vous avez appuyer sur la touche {}".format(repr(even.char)))
    var.set(even.keysym)

def act1(even):
    window15.config(bg='white')
def act2(even):
    window15.config(bg='black')

frm =Frame(window15,width=200,height=200,bg='pink')
var = StringVar()
lab = Label(window15,textvariable=var).pack()
var.set('lettre')
frm.bind("<Key>",key)
frm.bind("<Button>",callable)
frm.pack()

window15.mainloop()"""

"""Partie drag

window16 = Tk()
window16.title('Version drag')

label = Label(window16,width=10,height=5,bg='red')
label.place(x=0,y=0)
label2 = Label(window16,width=10,height=5,bg='blue')
label2.place(x=100,y=100)

def move(even):
    widget = even.widget
    widget.startX = even.x
    widget.startY = even.y

def drag(even):
    widget = even.widget
    x = widget.winfo_x() - widget.startX + even.x
    y = widget.winfo_y() - widget.startY + even.y
    widget.place(x=x,y=y)

label.bind('<Button-1>',move)
label.bind('<B1-Motion>',drag)
label2.bind('<Button-1>',move)
label2.bind('<B1-Motion>',drag)
window16.mainloop()"""

"""Partie moveImage
window17 = Tk()
window17.title('ImageMoving')
window17.geometry('500x500')
myImage = PhotoImage(file='OIP (3).png')
canvas = Canvas(window17,width=500,height=500)
canvas.pack()
img = canvas.create_image(0,0,image = myImage,anchor = NW)
def move_up(even):
    canvas.move(img,0,-10)
def move_down(even):
    canvas.move(img,0,10)
def move_left(even):
    canvas.move(img,-10,0)
def move_right(even):
    canvas.move(img,10,0)
# label = Label(window17,image=myImage)
# label.place(x=0,y=0)
# def move_up(even):
#     label.place(x=label.winfo_x(),y=label.winfo_y()-10)
# def move_down(even):
#     label.place(x=label.winfo_x(),y=label.winfo_y()+10)
#
# def move_left(even):
#     label.place(x=label.winfo_x()-10,y=label.winfo_y())
#
# def move_right(even):
#     label.place(x=label.winfo_x()+10,y=label.winfo_y())

window17.bind('<z>',move_up)
window17.bind('<s>',move_down)
window17.bind('<q>',move_left)
window17.bind('<d>',move_right)
window17.mainloop()"""

"""Partie animation
import time
window18 = Tk()
window18.title('version animation')
WIDTH = 500
HEIGHT = 500
x_velocity = 3
y_velocity = 2
canva = Canvas(window18,width=WIDTH,height=HEIGHT,bg='light yellow')
canva.pack()
image = PhotoImage(file='OIP (3).png')
img = canva.create_image(0,0,image=image,anchor = NW)
imgWidth = image.width()
imgHeight = image.height()

while True:
    coordinates = canva.coords(img)
    print(coordinates)
    if (coordinates[0]>WIDTH-imgWidth or coordinates[0]<0):
        x_velocity = -x_velocity
    if (coordinates[1]>WIDTH-imgWidth or coordinates[1]<0):
        y_velocity = -y_velocity
    canva.move(img, x_velocity, y_velocity)
    window18.update()
    time.sleep(0.01)

window18.mainloop()"""

"""Partie consort

window19 = Tk()
x = IntVar()
y = IntVar()
check = Radiobutton(window19,text="I like python",font=20,value=0)
check2 = Checkbutton(window19,text="I like Java",font=20,onvalue=0,offvalue=1)
check.pack(anchor = 'w')
check2.pack()
window19.mainloop()"""

"""Partie multiple animation
import time
class Ball:
    def __init__(self,canva,x,y,diametre,x_velocity,y_velocity,color):
        self.canva = canva
        self.image = canva.create_oval(x,y,diametre,diametre,fill = color)
        self.xvelocity = x_velocity
        self.yvelocity =y_velocity

    def move(self):
        coordinate = self.canva.coords(self.image)
        if (coordinate[2]>self.canva.winfo_width() or coordinate[0]<0):
            self.xvelocity = -self.xvelocity
        if (coordinate[3]>self.canva.winfo_width() or coordinate[1]<0):
            self.yvelocity = -self.yvelocity
        self.canva.move(self.image,self.xvelocity,self.yvelocity)
window20 = Tk()
window20.title('version multiple animation')
WIDTH = 500
HEIGHT = 500
canvas = Canvas(window20,width=WIDTH,height=HEIGHT)
canvas.pack()
Volley = Ball(canvas,0,0,100,1,1,'white')
golf = Ball(canvas,0,0,25,3,1,'maroon')
tennis = Ball(canvas,0,0,50,4,3,'yellow')
basket = Ball(canvas,0,0,125,8,7,'orange')

while True:
    Volley.move()
    tennis.move()
    golf.move()
    basket.move()
    window20.update()
    time.sleep(0.01)

window20.mainloop()"""

"""Partie ttk
from tkinter import ttk
window21 = Tk()
window21.geometry('500x200')
window21.title('Version ttk')
style = ttk.Style()
style.configure("BW.TButton",foreground='blue',background='red')
style.configure('BW.TLabel',foreground = 'blue',background = 'white')
b = ttk.Button(text='Un boutton',style='BW.TButton')
c = ttk.Label(text='Un label design avec ttk',style='BW.TLabel')
labeltop = Label(text="Choisissez votre Laptop")
labeltop.grid(row =0,column =1)
liste = ["Acer","HP","Lenovo","Del","Asus"]
combo = ttk.Combobox(window21,values=liste)
def comboact(even):
    af = combo.get()
    print('Vous avez choisis',af)

b.grid(row =0,column =0)
c.grid(row =1,column =0,padx = 20)
combo.grid(row =1,column =1)
combo.bind("<<ComboboxSelected>>",comboact)
combo.current(1)
# notebook = ttk.Notebook(window21)
# tab1 = Frame(window21)
# tab2 = Frame(window21)
# notebook.add(tab1,text="Tab1")
# notebook.add(tab2,text="Tab2")
# notebook.pack(expand = True,fill = 'both')
# Label(tab1,text="Ohayo sekai good morning world",width=50,height=25).pack()
# Label(tab2,text="Konbanwa sekai good evening world",width=50,height=25).pack()
tree = ttk.Treeview(window21,columns=(1,2,3,4),height=5,show="headings")
tree.place(x=50,y=50,width = 400)
tree.column(1,width=20)
tree.column(2,width=70)
tree.column(3,width=150)
tree.column(4,width=50)

tree.heading(1,text='ID')
tree.heading(2,text='Nom')
tree.heading(3,text='Email')
tree.heading(4,text='Age')

tree.insert('','end', values=(1,"Albert","albert@gmail.com",27))
tree.insert('','end', values=(2,"Majid","majid@gmail.com",33))
tree.insert('','end', values=(3,"Natalie","natalie@gmail.com",21))
tree.insert('','end', values=(4,"John","john@gmail.com",19))
tree.insert('','end', values=(5,"Tom","tom@gmail.com",22))
tree.insert('','end', values=(6,"Joe","joe@gmail.com",38))

def selectElement(event):
    select =tree.item(tree.selection())['values']
    print(select)
    
scroll = ttk.Scrollbar(window21,orient='vertical',command=tree.yview)
scroll.place(x=450,y=50,width =20,height =140)
tree.configure(yscrollcommand=scroll.set)
b = Button(window21,text='element selectionné')
b.grid(row =1,column = 2,padx = 2)
b.bind("<Button-1>",selectElement)
window21.mainloop()"""

"""buttons = [
    ('0', 4, 0), ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('.', 4, 1), ('=', 4, 2), ('%', 5, 1), ('unknown', 5, 2),
    ('M', 5, 3), ('effacer', 5, 0)
]

for (text, row, col) in buttons:
    Button(root, text=text, width=15, height=4, command=lambda t=text: click(t) if t not in ['=', 'effacer', 'M'] else (equal() if t == '=' else (delete() if t == 'effacer' else remove()))).grid(row=row, column=col, padx=5)
"""

