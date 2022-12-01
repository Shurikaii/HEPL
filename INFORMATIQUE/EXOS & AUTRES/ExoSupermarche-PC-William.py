# ---------- Lib & codecs --------- #

import cmath as cm 
from tkinter import *
from tkinter import ttk
import tkinter.font
from pyparsing import col
import json

# ---------- Functions ---------- #

'''EAN search'''
def search_name (ean):
  for keyval in data:
    if ean == keyval['DEAN']:
      return keyval['Name']
def search_price (ean):
  for keyval in data:
    if ean == keyval['DEAN']:
      return keyval['Price']
  
'''Quantity get'''
def qty_get(E_qty):
    
  global qty
  qty = E_qty.get('1.0','end')
    
  if qty == '\n' :
     return 1
  else:
     return float(qty)

'''Main function'''
def Main():
 global Total
 global Name
 global Price
 global qty
 global i

 if E_Name.get('1.0','end') == '\n' or E_Price.get('1.0','end') == '\n':
      
    ean = E_ean.get('1.0','end')
    if ean == '\n':
        print('error')
    else:
        ean = str(int(ean))
        if search_name (ean) != None:
         Name = search_name(ean)
         Price = float(search_price(ean))
         qty = qty_get(E_qty)
        else:
         Name = "Error"
         Price = 0
         qty = 0
 else:
    qty = qty_get(E_qty)   
    Name = E_Name.get('1.0','end')
    Price = float(E_Price.get('1.0','end'))
    
 E_Price.delete('1.0', 'end')
 E_Name.delete('1.0', 'end')
 E_qty.delete('1.0', 'end')
    
 Total = (Total + (Price*qty))
 i = i+qty
 label(i)     
              
def label(i):
 global r
 global result
 global qty
 if r == 0:
    result = Tk()
    result.grid 
    r = 1
 Label(result, text=Name, font=Cal2).grid(row=int(i), column=0)
 Label(result, text=(f'{Price:.2f}'), font=Cal2).grid(row=int(i), column=4)
 Label(result, text=(qty), font=Cal2).grid(row=int(i), column=2)
 Label(result, text=f" Total : {Total:.2f} €", font=CalB).grid(row=1001, column=2)
 Label(wdw, text=f" Total : {Total:.2f} €", font=CalB).grid(row=1001, column=2)
 Label(wdw, text=f"Articles : {i}", font=CalB).grid(row=1002, column=2)
 qty = 0
  
def clear():
 global r
 global Total
 global i
 result.destroy()
 Total = 0
 i = 0
 Label(wdw, text=f" Total : {Total:.2f} €", font=CalB).grid(row=1001, column=2)
 Label(wdw, text=f"Articles : {i}", font=CalB).grid(row=1002, column=2)
 r = 0
 
def destroy():
 wdw.destroy()
 result.destroy()
 
# ---------- Window ---------- #

wdw = Tk()
wdw.minsize(width=1000, height=500)
wdw.grid()
r = 1
result = Tk()
result.grid  
# ---------- Font ---------- #

Cal = tkinter.font.Font(family='calibri',size=20)
Cal2 = tkinter.font.Font(family='calibri',size=19)
CalB = tkinter.font.Font(family='calibri',size=25,weight='bold')

# ---------- Function Var  ----------- #
'''Initial variable'''
i = 0
Total = 0.00 
qty = 1
f = open('INFORMATIQUE\\data.json')
data = json.load(f)
Label(wdw, text=f" Price : {Total} €", font=CalB).grid(row=1001, column=2)
Label(wdw, text=f"Articles : {i}", font=CalB).grid(row=1002, column=2)
# ---------- Entry ---------- #

'''Article Name'''
ttk.Label(wdw, text=" Article Name : ", font=CalB).grid(row=1000, column=0)
E_Name = Text(wdw, height=1, width=40, font=Cal)
E_Name.grid(row=1000, column=1, columnspan=200)

'''Article Price'''
ttk.Label(wdw, text="Price : ", font=CalB).grid(row=1001, column=0)
E_Price = Text(wdw, height=1, width=8, font=Cal,)
E_Price.grid(row=1001, column=1)

'''Article Quantity'''
ttk.Label(wdw, text="Quantity : ", font=CalB).grid(row=1002, column=0)
E_qty = Text(wdw, height=1, width=8, font=Cal,)
E_qty.grid(row=1002, column=1)

'''EAN'''
ttk.Label(wdw, text="EAN : ", font=CalB).grid(row=1001, column=3)
E_ean = Text(wdw, height=1, width=18, font=Cal,)                                          #!!!! return entry + \n !!!!#
E_ean.grid(row=1002, column=3, columnspan=2)

'''ENTER BUTTON'''
button_enter=Button(wdw, height=2, width=30, text="ENTER", font=CalB, bg='green', activebackground='lightgreen', 
                    command=Main).grid(row=1003, column=0, columnspan=3, rowspan=2)
'''CLEAR BUTTON'''
button_enter=Button(wdw, height=1, width=20, text="Clear", font=Cal2, bg='lightgrey', activebackground='grey', 
                    command=clear).grid(row=1003, column=3, columnspan=2)
'''CLOSE BUTTON'''
button_destroy=Button(wdw, height=1, width=20, text="Close", font=Cal2, bg='red', activebackground='darkred', 
                    command=destroy).grid(row=1004, column=3, columnspan=2)
wdw.mainloop()
