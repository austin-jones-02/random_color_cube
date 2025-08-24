"""
A Tkinter python script that changes the window color randomly based on the colors
available from Tkinter.

"""

from tkinter import *
from random import choice
from tkinter_colors import full_list_of_colors


color_changer_on = False

def random_color_chosen():
    """Randomly choses a color from the supported list for Tkinter utilizing random.choice"""
    selected_random_color = choice(full_list_of_colors)
    
    return selected_random_color


def color_changer():
    """Handles the toggle for running the color change or not"""
    global color_changer_on

    if color_changer_on:
        # Turn off
        color_changer_on = False
        button.config(background='gray98')

    else:
        # Turn on
        color_changer_on = True
        button.config(background='green')
        run_color_loop()


def run_color_loop():
    """Changes the color of the window background when called"""
    if color_changer_on:
        color = random_color_chosen()
        root.config(background=color)
        label.config(text=f'Current color: {color}')
        root.after(500, run_color_loop)

root = Tk()

root.title('Random color cube')
root.geometry('500x500')


button = Button(root,
                text='Toggle random color changer',
                cursor='hand2',
                command=color_changer
)
button.pack(padx=20, pady=20)

label = Label(root,
              fg='gray',
              font=('Helvetica', 20),
)
label.pack()


# Run the program
root.mainloop()