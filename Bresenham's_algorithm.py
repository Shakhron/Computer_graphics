from tkinter import *


def draw_circle(x, y, r):
    disp_x = x
    disp_y = y
    x = 0
    y = r
    delta = (1 - 2 * r)
    error = 0
    while y >= 0:
        canv.create_line(disp_x + x, disp_y + y,disp_x + x + 1, disp_y + y,fill='black')
        canv.create_line(disp_x + x, disp_y - y,disp_x + x + 1, disp_y - y,fill='black')
        canv.create_line(disp_x - x, disp_y + y,disp_x - x + 1, disp_y + y,fill='black')
        canv.create_line(disp_x - x, disp_y - y,disp_x - x + 1, disp_y - y,fill='black')

        error = 2 * (delta + y) - 1
        if ((delta < 0) and (error <= 0)):
            x += 1
            delta = delta + (2 * x + 1)
            continue
        error = 2 * (delta - x) - 1
        if ((delta > 0) and (error > 0)):
            y -= 1
            delta = delta + (1 - 2 * y)
            continue
        x += 1
        delta = delta + (2 * (x - y))
        y -= 1

def draw_line(x1, y1, x2, y2):
    N = x2 - x1
    M = y2 - y1

    sign_x = 1 if N > 0 else -1 if N < 0 else 0
    sign_y = 1 if M > 0 else -1 if M < 0 else 0

    if N < 0: N = - N
    if M < 0: M = -M

    if N > M:
        pdx, pdy = sign_x, 0
        es, el = M, N
    else:
        pdx, pdy = 0, sign_y
        es, el = N, M

    x, y = x1, y1

    error, t = el / 2, 0

    canv.create_line(x, y, x+1, y, width=0, fill='black')

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        canv.create_line(x, y, x + 1, y, width=0, fill='black')


root = Tk()
canv = Canvas(root, width=1800, height=1200,bg='white')
canv.pack()
draw_line(1200,1200,10,100)
draw_circle(400,400,100)
root.mainloop()