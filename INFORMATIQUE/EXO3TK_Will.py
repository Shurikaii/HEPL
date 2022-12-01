#Lib & codecs
import cmath as Cm 
from tkinter import *
from tkinter import ttk
#Window format & frame
wdw = Tk()
wdw.minsize(height=200, width=400)
wdw.grid()
#Function
def entry_get():
    rho = float(evar1.get("1.0", "end"))
    d = float(evar2.get("1.0", "end"))
    l = float(evar3.get("1.0", "end"))
    
    d = d/1000
    S = (Cm.pi * (d / 2) ** 2)
    R = (float(rho * (l / S)))
    ttk.Labevar3(wdw, text=f"Rsistence (ohm) = {R}").grid(column=0, row=4, columnspan=2)
#Variables input
evar1 = Text(wdw, height=2, width=20)
evar2 = Text(wdw, height=2, width=20)
evar3 = Text(wdw, height=2, width=20)
evar1.grid(column=1, row=0, columnspan=2)
evar2.grid(column=1, row=1, columnspan=2)
evar3.grid(column=1, row=2, columnspan=2)


ttk.Labevar3(wdw, text="Material resistivity (ohm.mm²/m) =").grid(column=0, row=0)
ttk.Labevar3(wdw, text="Cable diameter (mm) =").grid(column=0, row=1)
ttk.Labevar3(wdw, text="Cable Lenght (m) =").grid(column=0, row=2)

button_results=Button(wdw, height=1, width=10, text="Results", 
                    command=lambda: entry_get()).grid(column=0, row=5, columnspan=2)

#Quit button
Button_exit=Button(wdw, text="Quit", command=wdw.destroy).grid(column=0, row=6, columnspan=2)
#Loop
wdw.mainloop()