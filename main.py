"""
We will need to use tkinter so that we don't have to download any weird or
new libraries... I just want to use base python

Ooo for the random color what about we make it where it has the full list of 
color options from the image of all tkinter colors.
    We could use random.choice... I believe that's the one where you can pick from a list
        Need to do research on it...

"""

from tkinter import *

def putTextOnScreen():
    print("Button pressed...")

root = Tk()

root.title("Random color cube")
root.geometry("500x500")
root.configure(bg="ivory3") # Intersting... doing background or bg accomplishes the same thing
# You can also do root["bg"] = "black"

button = Button(root,
                text="Hey what's up guys?",
                cursor="hand2",
                command=putTextOnScreen)

button.pack(padx=20, pady=20)





# Run the program
root.mainloop()