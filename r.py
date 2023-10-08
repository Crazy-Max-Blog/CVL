from tkinter import *
from tkinter import filedialog

class window:
    def __init__(self, r):
        self.root = r
        
    def r(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.l=Button(font='Times 15',fg="white",activebackground=self.root["bg"],bd=0,bg=self.root["bg"],text="Загрузить задачу",command=self.load_task)
        self.l.pack()
        self.c = Button(fg="white",activebackground=self.root["bg"],bd=0,bg=self.root["bg"], text="выход", command=exit)
        self.c.pack(side=RIGHT, anchor=SE)
    
    def load_task(self):
        self.p=filedialog.askopenfilename(filetypes=(("Задачи CVL", "*.cvl"),("Задачи ВЛ", "*.edu1")))
        print("load task", self.p)
        self.w1(self.p)
    
    def exit(self):
        print("exit")
        self.root.destroy()
        
    def rd(self, f):
        with open(f, "r", encoding="UTF-8") as file:
            self.s = file.read()
        self.l1=self.s.split('\n')
        print(len(self.l1))
        match len(self.l1):
            case 2:
                return [self.l1[0],self.l1[1],"",""]
            case 4:
                print(str(0) not in self.l1[2].split())
                if len(self.l1[2].split())==len(self.l1[3].split()) and str(0) not in self.l1[2].split():
                    return [self.l1[0],self.l1[1],self.l1[2].split(),self.l1[3].split()]
        print("error: error file")
        #return
        
    def w1(self, p):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        print(self.rd(p))
        
        print(open(p,'r').read())
        self.d = self.rd(p)
        self.t = f'Задача типа {self.d[0]}\nЗадача: {self.d[1]}\nНачальное состояние {self.d[2]}\nКонечное сосотояние {self.d[3]}'
        print(self.t)
        Label(text=self.t,bg="SteelBlue1").pack()
        self.l = Button(fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="назад", command=self.r)
        self.l.pack(side=LEFT, anchor=SW)    