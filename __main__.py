from tkinter import *
from tkinter import filedialog

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
    
def w1(p):
    for widget in root.winfo_children():
        widget.destroy()
    
    print(open(p,'r').read())
    Label(text=open(p,'r').read(),bg="SteelBlue1").pack()
    l = Button(fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="назад", command=r)
    l.pack(side=LEFT, anchor=SW)    

def load_task():
    p=filedialog.askopenfilename(filetypes=(("Задачи ВЛ", "*.edu1"),("All Files", "*.*")))
    print("load task", p)
    w1(p)

def exit():
    print("exit")
    root.destroy()
    
r()

root.mainloop()