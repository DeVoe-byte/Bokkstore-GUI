from tkinter import *
window=Tk()
def km_to_miles():
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)
    pounds=float(e1_value.get())*2.20462
    t2.insert(END,pounds)
    ounces=float(e1_value.get())*35.274
    t3.insert(END,ounces)


b1=Button(window,text="CONVERT",command=km_to_miles)
b1.grid(row=4,column=325)
e1=Label(window,text="Kg")
e1.grid(row=0,column=3)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=3,column=3)
t1=Text(window,height=1,width=20)
t1.grid(row=5,column=2)
t2=Text(window,height=1,width=20)
t2.grid(row=5,column=3)
t3=Text(window,height=1,width=20)
t3.grid(row=5,column=4)
window.mainloop()