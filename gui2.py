import tkinter as tk
def change_colour():
    background_colour=button.cget("bg")
    if background_colour=="red":
        button.config(bg="green")
    else:
        button.config(bg="red")

window=tk.Tk()
button=tk.Button(window,text="click me",command=change_colour)
button.pack()

window.mainloop()