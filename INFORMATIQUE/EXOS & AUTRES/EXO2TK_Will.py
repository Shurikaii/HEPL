#Lib & codecs
import cmath as Cm 
from tkinter import *
from tkinter import ttk
#Window format & frame
wdw = Tk()
frm = ttk.Frame(wdw, padding=10)
frm.grid()
#Variables input
r = int(input("Radius (cm) :"))
#Calculation
S = (Cm.pi * r ** 2)
P = (2 * Cm.pi * r)
#Display results
ttk.Label(frm, text=f"Radius of the disc : {r} cm").grid(column=0, row=0)
ttk.Label(frm, text=f"Surface of the disc : {S:.3f} cm").grid(column=0, row=1)
ttk.Label(frm, text=f"Perimeter of the disc : {P:.3f} cm").grid(column=0, row=2)
#Quit button
ttk.Button(frm, text="Quit", command=wdw.destroy).grid(column=0, row=3)
#Loop
wdw.mainloop()