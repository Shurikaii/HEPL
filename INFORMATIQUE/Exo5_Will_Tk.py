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

    if var1 > 31 or var2 > 12:
        datet = ttk.Label(wdw, text="ERROR : TRY TO VERIFY DATE FORMAT").grid(
            column=0, row=4)
    else:
        var1t = var1
        var2t = var2
        var3t = var3
        if var1 == 31:
            if var2 == 12:
                var3t = var3t + 1
                var2t = 1
                var1t = 1
            else:
                var2t = var2t + 1
                var1t = 1
        else:
            var1t = var1t + 1
        datet = ttk.Label(
        wdw, text=f"Tomorow's date : {var1t:.0f}.{var2t:.0f}.{var3t:.0f}").grid(column=0, row=4)

    date = ttk.Label(wdw, text=f"Today's date is : {var1:.0f}.{var2:.0f}.{var3:.0f}").grid(
        column=0, row=0)


# Var input
evar1 = Text(wdw, height=2, width=20)
evar2 = Text(wdw, height=2, width=20)
evar3 = Text(wdw, height=2, width=20)
evar4 = Text(wdw, height=2, width=20)

evar1.grid(column=1, row=1, columnspan=2)
evar2.grid(column=1, row=2, columnspan=2)
evar3.grid(column=1, row=3, columnspan=2)

date = ttk.Label(wdw, text=f"Date :").grid(column=0, row=0)

ttk.Label(wdw, text="Day (1-31) :").grid(column=0, row=1)
ttk.Label(wdw, text="Month (1-12) :").grid(column=0, row=2)
ttk.Label(wdw, text="Year :").grid(column=0, row=3)


button_results = Button(wdw, height=1, width=10, text="Results",
                        command=lambda: entry_get()).grid(column=0, row=8, columnspan=2)

# Quit button
Button_exit = Button(wdw, text="Quit", command=wdw.destroy).grid(
    column=0, row=9, columnspan=2)
# Loop
wdw.mainloop()
