# Lib & codecs
import cmath as Cm 
from tkinter import *
from tkinter import ttk
# Frame 
wdw = Tk()
wdw.minsize(height=200, width=400)
wdw.grid()
# Function
def entry_get():
    var1 = float(evar1.get("1.0", "end"))
    var2 = float(evar2.get("1.0", "end"))
    var3 = float(evar3.get("1.0", "end"))
    
    varX = float(evarX.get("1.0", "end"))
    varY = float(evarY.get("1.0", "end"))
    
    eq = ttk.Label(wdw, text=f"Straight line équation = {var1}x + {var2}y + {var3} = 0").grid(column=0, row=0)
    peq = ttk.Label(wdw, text=f"Point coordonate = ({varX} ; {varY})").grid(column=0, row=4)
    
    if (var1*varX + var2*varY + var3) == 0 :
        ttk.Label(wdw, text="The point is on the straight line" ).grid(column=0, row=7)
    else :
        ttk.Label(wdw, text="The point is NOT on the straight line").grid(column=0, row=7)
    
    
# Var input

evar1 = Text(wdw, height=2, width=20)
evar2 = Text(wdw, height=2, width=20)
evar3 = Text(wdw, height=2, width=20)
evar4 = Text(wdw, height=2, width=20)

evarX = Text(height=2, width=20 )
evarY = Text(height=2, width=20)

evar1.grid(column=1, row=1, columnspan=2)
evar2.grid(column=1, row=2, columnspan=2)
evar3.grid(column=1, row=3, columnspan=2)


evarX.grid(column=1, row=5, columnspan=2)
evarY.grid(column=1, row=6, columnspan=2)

eq = ttk.Label(wdw, text=f"Straight line équation = ax + by + c = 0").grid(column=0, row=0)
ttk.Label(wdw, text="a =").grid(column=0, row=1)
ttk.Label(wdw, text="b =").grid(column=0, row=2)
ttk.Label(wdw, text="c =").grid(column=0, row=3)

peq = ttk.Label(wdw, text=f"Point coordonate = (x ; y)").grid(column=0, row=4)
ttk.Label(wdw, text="x =").grid(column=0, row=5)
ttk.Label(wdw, text="y =").grid(column=0, row=6)

button_results=Button(wdw, height=1, width=10, text="Results", 
                    command=lambda: entry_get()).grid(column=0, row=8, columnspan=2)

#Quit button
Button_exit=Button(wdw, text="Quit", command=wdw.destroy).grid(column=0, row=9, columnspan=2)
#Loop
wdw.mainloop()