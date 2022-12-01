#Lib & codecs
import cmath as Cm 
from tkinter import *
from tkinter import ttk
#Window format & frame
wdw = Tk()
wdw.minsize(height=100, width=400)
wdw.grid()
#Function
def entry_get():
    rho = float(erho.get("1.0", "end"))
    d = float(ed.get("1.0", "end"))
    l = float(el.get("1.0", "end"))
    
    d = d/1000
    S = (Cm.pi * (d / 2) ** 2)
    R = (float(rho * (l / S)))
    ttk.Label(wdw, text=f"Rsistence (ohm) = {R}").grid(column=0, row=4, columnspan=2)
#Variables input
erho = Text(wdw, height=1, width=20)
ed = Text(wdw, height=1, width=20)
el = Text(wdw, height=1, width=20)
erho.grid(column=1, row=0, columnspan=2)
ed.grid(column=1, row=1, columnspan=2)
el.grid(column=1, row=2, columnspan=2)


ttk.Label(wdw, text="Material resistivity (ohm.mm²/m) =").grid(column=0, row=0)
ttk.Label(wdw, text="Cable diameter (mm) =").grid(column=0, row=1)
ttk.Label(wdw, text="Cable Lenght (m) =").grid(column=0, row=2)

button_results=Button(wdw, height=1, width=10, text="Results", 
                    command=lambda: entry_get()).grid(column=0, row=5, columnspan=2)

#Quit button
Button_exit=Button(wdw, text="Quit", command=wdw.destroy).grid(column=0, row=6, columnspan=2)
#Loop
wdw.mainloop()