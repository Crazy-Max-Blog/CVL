from tkinter import *
from tkinter import filedialog
from r import *

root = Tk()
root["bg"] = "SteelBlue1"

#root.attributes("-fullscreen", True)
#root.attributes("-fullscreen", False)

w, h = 500, 500
root.geometry(f'{w}x{h}')    

def r():
    for widget in root.winfo_children():
        widget.destroy()
    
    l = Button(font='Times 15',fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="Загрузить задачу", command=load_task)
    l.pack()
    c = Button(fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="выход", command=exit)
    c.pack(side=RIGHT, anchor=SE)

def load_task():
    p=filedialog.askopenfilename(filetypes=(("Задачи CVL", "*.cvl"),("Задачи ВЛ", "*.edu1")))
    print("load task", p)
    w1(p)

def exit():
    print("exit")
    root.destroy()
    
print(rd("1.cvl"))
r()

root.mainloop()