"""
We will need to use tkinter so that we don't have to download any weird or
new libraries... I just want to use base python

Ooo for the random color what about we make it where it has the full list of 
color options from the image of all tkinter colors.
    We could use random.choice... I believe that's the one where you can pick from a list
        Need to do research on it...

"""

from tkinter import *
from random import choice
from tkinter_colors import full_list_of_colors


def random_color_chosen():
    """Randomly choses a color from the supported list for Tkinter utilizing random.choice"""
    selected_random_color = choice(full_list_of_colors)
    print(selected_random_color)
    
    return selected_random_color


def color_changer():
    root.configure(background=random_color_chosen())
    root.after(1000, color_changer)

root = Tk()

root.title("Random color cube")
root.geometry("500x500")


button = Button(root,
                text="Change color of background",
                cursor="hand2",
                command=color_changer)

button.pack(padx=20, pady=20)


# Run the program
root.mainloop()