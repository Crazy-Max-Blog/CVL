from tkinter import *
from tkinter import filedialog
from r import *

root = Tk()
root["bg"] = "SteelBlue1"

#root.attributes("-fullscreen", True)
#root.attributes("-fullscreen", False)

w, h = 500, 500
root.geometry(f'{w}x{h}')    

w = window(root)
print(w.rd("1.cvl"))
w.r()

root.mainloop()