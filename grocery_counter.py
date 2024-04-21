from tkinter import *

from tkinter import messagebox

root = Tk()
v=IntVar()

count =0

d={}
def inc():
    global count
    count += 1
    v.set(count)
   
def dec():
    global count
    count -= 1
    v.set(count)
    print(v.get())

def add():
    global d
    
    d[e.get()]=v.get()
    print(d)
    messagebox.showinfo('Grocery Cat',d)
    
def finish():
    messagebox.showinfo('Grocery Cat',d)
    root.destroy()

e=Entry(root, width=40)
e.grid(row=0,column=1,columnspan=3)

label0 = Label (root, text='Please enter an item' )
label0.grid(row=0,column=0)

label1 = Label (root, text='Choose the quantity')
label1.grid(row=1,column=0)   
label = Label (root, textvariable =v, width=10 )
label.grid(row=1,column=2)
button1 = Button (root, text='-', fg='red', width=10, command=dec)

button1.grid(row=1,column=3)

button2 = Button (root, text='+', fg='green', width=10,command=inc)

button2.grid(row=1,column=1)

button3 = Button (root, text='ADD', fg='green',width=10,command=add)

button3.grid(row=2,column=1, columnspan=3)


button3 = Button (root, text='FINISH',fg='red', width=10,command=finish)

button3.grid(row=2,column=0)

root.mainloop()
