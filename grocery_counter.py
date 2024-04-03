from tkinter import*

root = Tk()

root.title("Set 1")

root.geometry('400x500')

def facebook():

    user.delete(0,END)

    user.insert(0,"idk@facebook.com")

def linkedin():

    user.delete(0,END)

    user.insert(0,"idk@linkedin.com")


def instagram():

    user.delete(0,END)

    user.insert(0,"idk@instagram.com")

def twitter():

    user.delete(0,END)

    user.insert(0,"idk@twitter.com")


f = Button(root, text="Facebook", width=10,height=10,bg="blue",command=facebook)

f.grid(row=0,column=0)

l = Button(root, text="Linkedin", bg="red",width=10,height=10,command=linkedin)

l.grid(row=0,column=1)

i = Button(root, text="Instagram", bg="green",width=10,height=10,command=instagram)

i.grid(row=1,column=0)

t = Button(root, text="Twitter", bg="sky blue",width=10,height=10,command=twitter)

t.grid(row=1,column=1)

user = Entry(root,width=50)

user.grid(row=2,column=0, columnspan=3)

root.mainloop()
