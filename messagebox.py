# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Create Window
root = Tk()
root.title('Event Handler')
root.geometry('400x400')

def msg():
    messagebox.showwarning("Alert!" , "Stop. Virus found!!")
button = Button(root,text = "scan for virus" , command = msg)
button.place(x = 80 , y = 80)

root.mainloop()
