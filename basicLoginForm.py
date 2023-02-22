from tkinter import *
from tkinter import messagebox

IMAG_PATH="C:/Users/ferna/Downloads/python/login/Images/"

def Singin():
    username=user.get()
    password=code.get()

    if (username=="admin" and password=="1234"):
        screen=Toplevel(root)
        screen.title("Example App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen, text="Sample message", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
        screen.mainloop()

    elif (username!="admin" and password!="1234"):
        messagebox.showerror("Invalid","Invalid username and password")
    elif (username!="admin"):
        messagebox.showerror("Invalid","Invalid username")
    elif (password!="1234"):
        messagebox.showerror("Invalid","Invalid password")


root=Tk()
root.title("Login Form")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img_login=PhotoImage(file=IMAG_PATH+"login3.png")
Label(root, image=img_login, bg="white").place(x=0, y=0)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text="Sing in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

#User

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0, "Username")


user=Entry(frame, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

#Code
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0, "Password")

code=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


Button(frame, width=39, padx=7, text="Sing in", bg="#57a1f8", fg="white", border=0, command=Singin).place(x=35, y=204)
label=Label(frame, text="Don't hace an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)
sing_up=Button(frame, width=6, text="Sing up", border=0, bg="white", cursor="hand2", fg="#57a1f8").place(x=215, y=270)



















root.mainloop()