"""
We will need to use tkinter so that we don't have to download any weird or
new libraries... I just want to use base python

"""

from tkinter import *

root = Tk()

root.title("Random color cube")
root.geometry("500x500")

button = Button(root,
                text="Hey what's up guys?",
                cursor="hand2")

button.pack(padx=20, pady=20)



# Run the program
root.mainloop()