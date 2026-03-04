import tkinter as tk

window = tk.Tk()
window.title("My Tkinter App")

label = tk.Label(
    window,
    text="Hello, Tkinter!",
    fg="blue",
    bg="yellow",
    padx=10,
    pady=5
)
label.pack()

button = tk.Button(
    window,
    text="Click Me",
    width=15,
    command=lambda: print("Button clicked!")
)
button.pack()

window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Tkinter Example")

label = tk.Label(window, text="Initial Text")
label.pack()

# Using cget()
current_text = label.cget("text")
print(f"Current text: {current_text}")

# Using config() and dictionary access
current_bg = label.config()["bg"][-1]
print(f"Current background: {current_bg}")

window.mainloop()