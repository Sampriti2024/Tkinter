# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Event Handler')
root.geometry('400x400')

def handle_keypress(event):
    print (event.char)
root.bind("<Key>",handle_keypress)
def handle_click(event):
    print ("Button was clicked")
button = Button(text = "click me!")
button.pack()
button.bind("<Button-1>", handle_click)
root.mainloop()
