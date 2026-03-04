import tkinter as tk

def button_click():
    print("button click")
    label.config(bg='purple')
    button.config(bg='sky blue')
    print("you typed",entry.get())

window=tk.Tk()

window.title("my first gui app with fa24-b")
window.geometry("400x200")


label=tk.Label(window,text="hello,Tkinter!",bg="green",fg="yellow",font=("arial",16))
label.pack()

label=tk.Label(window,text="my name is minal",bg="green",fg="yellow",font=("arial",18))
label.pack()

label=tk.Label(window,text="hope you all are doing well",bg="green",fg="yellow",font=("arial",14))
label.pack()

button=tk.Button(window,text="click me",command=button_click,bg="red",fg="yellow")
button.pack()

entry=tk.Entry(window,width=30)
entry.pack()
window.mainloop()