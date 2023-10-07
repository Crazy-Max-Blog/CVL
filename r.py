def rd(f):
    with open(f, "r", encoding="UTF-8") as file:
        s = file.read()
    l1=s.split('\n')
    print(len(l1))
    match len(l1):
        case 2:
            return [l1[0],l1[1],"",""]
        case 4:
            return [l1[0],l1[1],l1[2].split(),l1[3].split()]
    print("error: error file") 
    #return
    
def w1(p):
    for widget in root.winfo_children():
        widget.destroy()
    
    print(rd(p))
    
    print(open(p,'r').read())
    Label(text=rd(p),bg="SteelBlue1").pack()
    l = Button(fg="white",activebackground="SteelBlue1",bd=0,bg="SteelBlue1", text="назад", command=r)
    l.pack(side=LEFT, anchor=SW)    