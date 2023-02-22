from tkinter import *
from tkinter import messagebox
import ast

IMAG_PATH="C:/Users/ferna/Downloads/python/login/Images/"
SAVE_TXT_PATH="C:/Users/ferna/Downloads/python/login/example1/"

def Destroy_app():
    root.destroy()

######################################################  SING UP  #########################################################################
def Sing_up_command():
    root.withdraw()
    window=Toplevel(root)
    window.protocol("WM_DELETE_WINDOW", Destroy_app)
    window.title("Login Form")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    def Sing_Up():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if (password==conform_password):
            try:
                file=open(SAVE_TXT_PATH+'datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open(SAVE_TXT_PATH+'datasheet.txt', 'w')
                file.write(str(r))
                file.close()
                messagebox.showinfo('Sing Up', 'Sucessfully sing up')
                window.destroy()
                root.wm_deiconify()
            except:

                file=open(SAVE_TXT_PATH+'datasheet.txt', 'w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()

                file=open(SAVE_TXT_PATH+'datasheet.txt', 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open(SAVE_TXT_PATH+'datasheet.txt', 'w')
                file.write(str(r))
                file.close()
                messagebox.showinfo('Sing Up', 'Sucessfully sing up')
                window.destroy()
                root.wm_deiconify()
                
        else:
            messagebox.showerror('Invalid','both password should match')



    img_login=PhotoImage(file=IMAG_PATH+"singUp.png")
    Label(window, image=img_login, bg="white").place(x=0, y=0)

    frame=Frame(window, width=350, height=350, bg="white")
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


    Button(frame, width=39, padx=7, text="Sing up", bg="#57a1f8", fg="white", border=0, command=Sing_Up).place(x=28, y=290)
    Label(frame, text="I have an account", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=98, y=320)
    Button(frame, width=6, text="Sing in", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=Destroy_app).place(x=198, y=320)

    window.mainloop()


######################################################  SING IN  #########################################################################


def Sing_in():
    username=user.get()
    password=code.get()

    file=open(SAVE_TXT_PATH+'datasheet.txt', 'r+')
    d=file.read()
    r=ast.literal_eval(d)
    file.close

    if (username in r.keys() and password==r[username]):
        root.withdraw()
        screen=Toplevel(root)
        screen.protocol("WM_DELETE_WINDOW", Destroy_app)
        screen.title("Example App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")
        Label(screen, text="Sample message", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)
        screen.mainloop()

    else:
        messagebox.showerror("Invalid","invalid username or password")


root=Tk()
root.title("Login Form")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

img_login=PhotoImage(file=IMAG_PATH+"login.png")
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


Button(frame, width=39, padx=7, text="Sing in", bg="#57a1f8", fg="white", border=0, command=Sing_in).place(x=35, y=204)
label=Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)
sing_up=Button(frame, width=6, text="Sing up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=Sing_up_command).place(x=215, y=270)


root.mainloop()