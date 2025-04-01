"""import time
from tkinter import *
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


window = Tk()
window.title('version multiple animation')
WIDTH = 500
HEIGHT = 500
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
# Volley = Ball(canvas,0,0,100,1,1,'white')
golf = Ball(canvas,0,0,25,3,1,'maroon')
tennis = Ball(canvas,100,100,50,4,3,'yellow')
# basket = Ball(canvas,0,0,125,8,7,'orange')
t = 0
while t == 0:
    # Volley.move()
    tennis.move()
    golf.move()
    # basket.move()
    window.update()
    time.sleep(0.01)
    print("golf:",golf.canva.coords(golf.image))
    print("tennis:",tennis.canva.coords(tennis.image))
    ten = tennis.canva.coords(tennis.image)
    gol = golf.canva.coords(golf.image)
    if ten[0] in [(gol[2]+i) for i in range(26)] and ten[1] == [(gol[3]+i) for i in range(26)]  or gol[0] in [(ten[2]+i) for i in range(51)] and gol[1] in [(ten[3]+i) for i in range(51)]:
            t = 1

window.mainloop()"""

import time
from tkinter import *

class Ball:
    def __init__(self, canva, x, y, diametre, x_velocity, y_velocity, color):
        self.canva = canva
        self.image = canva.create_oval(x, y, x + diametre, y + diametre, fill=color)
        self.xvelocity = x_velocity
        self.yvelocity = y_velocity
        self.diametre = diametre

    def move(self):
        coordinate = self.canva.coords(self.image)
        if (coordinate[2] > self.canva.winfo_width() or coordinate[0] < 0):
            self.xvelocity = -self.xvelocity
        if (coordinate[3] > self.canva.winfo_height() or coordinate[1] < 0):
            self.yvelocity = -self.yvelocity
        self.canva.move(self.image, self.xvelocity, self.yvelocity)

    def check_collision(self, other_ball):
        coord1 = self.canva.coords(self.image)
        coord2 = other_ball.canva.coords(other_ball.image)
        # Calculer les centres des deux balles
        center1_x = (coord1[0] + coord1[2]) / 2
        center1_y = (coord1[1] + coord1[3]) / 2
        center2_x = (coord2[0] + coord2[2]) / 2
        center2_y = (coord2[1] + coord2[3]) / 2
        # Calculer la distance entre les centres
        distance = ((center2_x - center1_x) ** 2 + (center2_y - center1_y) ** 2) ** 0.5
        # Vérifier si la distance est inférieure à la somme des rayons
        if distance < (self.diametre / 2 + other_ball.diametre / 2):
            return True
        return False

window = Tk()
window.title('version multiple animation')
WIDTH = 500
HEIGHT = 500
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

golf = Ball(canvas, 0, 0, 25, 3, 1, 'maroon')
tennis = Ball(canvas, 100, 100, 50, 4, 3, 'yellow')

while True:
    golf.move()
    tennis.move()
    if golf.check_collision(tennis):
        golf.xvelocity = -golf.xvelocity
        golf.yvelocity = -golf.yvelocity
        tennis.xvelocity = -tennis.xvelocity
        tennis.yvelocity = -tennis.yvelocity
    window.update()
    time.sleep(0.01)

window.mainloop()

