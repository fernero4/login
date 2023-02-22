from tkinter import *
from tkinter import messagebox

IMAG_PATH="C:/Users/ferna/Downloads/python/login/Images/"

# def Login():
#     username=entry1.get()
#     password=entry2.get()

#     if (username=="" and password==""):
#         messagebox.showinfo("","Blank not allowed")
#     elif (username=="ferna" and password=="1234"):
#         messagebox.showinfo("","login success")
#     else:
#         messagebox.showinfo("","Incorrect username and password")

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

user=Entry(frame, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

#Code
code=Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Password")

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

























root.mainloop()