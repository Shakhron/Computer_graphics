import math
from tkinter import *
import main

def pifagor(n , x, y, a, fi, alfa):
    x1 = x
    y1 = y
    dx = a * math.sin(fi)
    dy = a * math.cos(fi)
    x2 = x + dx
    y2 = y - dy
    x3 = x + dx - dy
    y3 = y - dy - dx
    x4 = x - dy
    y4 = y - dx
    x5 = x - dy + a * math.cos(alfa) * math.sin(fi - alfa)
    y5 = y - dx - a * math.cos(alfa) * math.cos(fi - alfa)

    canv.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4,fill='white',outline='blue')
    canv.create_polygon(x4, y4, x3, y3, x5, y5,fill='white',outline='blue')

    if n > 1:
        pifagor(n-1 ,x5, y5, a * math.sin(alfa), fi - alfa + math.pi / 2, alfa)
        pifagor(n-1 ,x4, y4, a * math.cos(alfa), fi - alfa, alfa)



root = Tk();
canv = Canvas(root, width=1800, height=1200,bg='white')
canv.pack()

x = 680
y = 650
a = 120
n = 16
f = math.pi / 2
alfa = math.pi / 3

pifagor(n, x, y, a, f , alfa)

root.mainloop()