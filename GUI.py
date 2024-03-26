from tkinter import *

root = Tk()

e = Entry(root, width=40, bg="blue",fg="white", borderwidth=3)
e.pack()
e.insert(0, "enter your name: ")
#Creating a label widget
    #myLabel1 = Label(root, text="Hello World!")
    #myLabel2 = Label(root, text="My name is")
#Shoving it onto the screen
    #myLabel.pack()

    #myLabel1.grid(row=0, column=0)
    #myLabel2.grid(row=1, column=0)


def calculate():
    myLabel = Label(root, text= e.get())
    myLabel.pack()

myButton = Button(root, text="calculate", padx=40, pady=15, command=calculate)
#state = DISABLED
#fg=, bg= 
myButton.pack()

#dropdown boxxes

def show():
    myLabel = Label(root, text=variable.get()).pack()

options = ["Mon", "Tue", "Wed", "Thu",]
variable = StringVar()
variable.set(options[0])
drop = OptionMenu(root, variable, *options )
drop.pack()
NewButton = Button(root, text="Show selection", command=show).pack()
root.mainloop()


