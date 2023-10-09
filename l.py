from tkinter import *
from tkinter import filedialog
from l import *

def l(root, d, r):  
    match int(d[0]):
        case 1:
            p(root, d)
    l = Button(fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="назад", command=r)
    l.pack(side=LEFT, anchor=SW) 
    
def p(root, d):
    t = f'Задача типа {d[0]}\nЗадача: {d[1]}\nЁмкости {d[2]}\nНачальное состояние {d[3]}'
    print(t)
    Label(text=t,bg="SteelBlue1").pack() 
    