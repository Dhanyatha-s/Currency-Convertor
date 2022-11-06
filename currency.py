
from tkinter import *
from currency_converter import CurrencyConverter
a=CurrencyConverter()
window=Tk()
window.title("Currency Convertor")
window.geometry("500x380")
window.config(bg="#FF8DC7")


def clicked():
    amount=int(e1.get())
    cur1=e2.get()
    cur2=e3.get()
    data=a.convert(amount,cur1,cur2)
    lab4=Label(window,text=data,font=("Ink Free",20,"bold"),fg="#FDFF00",bg="#FF8DC7").place(x=90,y=300)

lab=Label(window, text="💱Currency Convertor💱",font=("Ink Free",30,"bold"),fg="#8D72E1",bg="#FF8DC7").place(x=30,y=30)
lab1=Label(window,text="Enter the amount:",font=("Ink Free",20,"bold"),fg="#3F3B6C",bg="#FF8DC7").place(x=20,y=100)
e1=Entry(window,width=20,border=0)
lab2=Label(window,text="Enter currency:",font=("Ink Free",20,"bold"),fg="#3F3B6C",bg="#FF8DC7").place(x=20,y=140)
e2=Entry(window,width=20,border=0)
lab3=Label(window,text="Enter req Currency:",font=("Ink Free",20,"bold"),fg="#3F3B6C",bg="#FF8DC7").place(x=20,y=180)
e3=Entry(window,width=20,border=0)
btn=Button(window,text="convert",bg="#FF8DC7",command=clicked,font=("Ink Free",20,"bold"),fg="#3F3B6C").place(x=200,y=240)
e1.place(x=300,y=110)
e2.place(x=300,y=150)
e3.place(x=300,y=190)
window.mainloop()
#a=CurrencyConverter()
#print(a.convert(12,"USD","INR"))