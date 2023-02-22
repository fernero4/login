from tkinter import *
from tkinter import messagebox
import ast

IMAG_PATH="C:/Users/ferna/Downloads/python/login/Images/"

def Sing_Up():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()

    if (password==conform_password):
        try:
            file=open('datasheet.txt', 'r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt', 'w')
            file.write(str(r))
            file.close()
            messagebox.showinfo('Sing Up', 'Sucessfully sing up')

        except:

            file=open('datasheet.txt', 'w')
            pp=str({'username':'password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid','both password should match')


root=Tk()
root.title("Login Form")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img_login=PhotoImage(file=IMAG_PATH+"singUp.png")
Label(root, image=img_login, bg="white").place(x=0, y=0)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text="Sing up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

#User

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get()=="":
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
    if code.get()=="":
        code.insert(0, "Password")

code=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


#repeat password
def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e):
    if conform_code.get()=="":
        conform_code.insert(0, "Conform Password")

conform_code=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, "Conform Password")
conform_code.bind('<FocusIn>', on_enter)
conform_code.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)


#############################
Button(frame, width=39, padx=7, text="Sing up", bg="#57a1f8", fg="white", border=0, command=Sing_Up).place(x=28, y=290)
label=Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=98, y=320)
sing_up=Button(frame, width=6, text="Sing in", border=0, bg="white", cursor="hand2", fg="#57a1f8").place(x=198, y=320)


root.mainloop()