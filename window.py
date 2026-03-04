import tkinter as tk
def login():
    if(entry_username.get()=="admin")&(emtry_password.get()=="admin"):
        print("login successfully")
        label_status.config(text="login successfully")

root=tk.Tk()

root.title("login window")
root.geometry("200x200")

label_userName=tk.Label(root,text="user name")
label_username.pack()

entry_password=tk.Entry(root,width=20)
entry_password.pack()



root.mainloop()