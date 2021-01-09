import random
import time
from tkinter import Tk , Button , DISABLED

def show_symbol (x,y):
    global first
    global px , py
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()
    if first :
        px = x
        py = y
        first = False
    elif px != x or py != y :
        if buttons[px,py]['text'] != buttons[x,y]['text']:
            time.sleep(0.2)
            buttons[px,py]['text'] = ''
            buttons[x,y]['text'] =''
        else :
            buttons[px,py]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True





win = Tk()
win.title('MatchMaker')
win.resizable(width=False, height=False)
first = True
px = 0
py = 0
buttons = {}
button_symbols = {}
symbol = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbol)

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x , y=y : show_symbol(x,y) , width = 12 , height = 9 )
        button.grid(column = x , row = y )
        buttons[x,y] = button
        button_symbols[x,y] = symbol.pop()

win.mainloop()