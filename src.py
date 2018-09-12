from tkinter import *
import os

creds = 'tempfile.temp'

def Signup():
    global pwE
    global nameE
    global rootS

    rootS = Tk()
    rootS.title("Sign Up")

    instructions = Label(rootS , text = "Please Enter New Credintials \n")
    instructions.grid(row = 0 , column = 0 , sticky = E)

    nameL = Label(rootS , text = "New Usermame: ")
    nameL.grid(row = 1 , column = 0 , sticky = W)

    pwL = Label(rootS , text = "New Password")
    pwL.grid(row = 2 , column = 0 , sticky = W)

    nameE = Entry(rootS)
    nameE.grid(row = 1 , column = 1)
    pwE = Entry(rootS , show = '*')
    pwE.grid(row = 2  , column = 1)

    signupButton = Button(rootS , text = "Signup" , command= FSSignup )
    signupButton.grid(columnspan = 2 , sticky = W)
    rootS.mainloop()

def FSSignup():
    with open(creds , 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwE.get())
        f.close()
    rootS.destroy()
    Login()

def Login():
    global nameEL
    global pwEL
    global rootA

    rootA = Tk()
    rootA.title("Login")
    insttructions = Label (rootA , text = "Please Login")
    insttructions.grid(sticky = E)

    nameL = Label(rootA , text = "Username")
    nameL.grid(row = 1 , column = 0 , sticky = W)
    pwordL = Label(rootA , text = "Password")
    pwordL.grid(row = 2 , column = 0 , sticky = W)

    nameEL = Entry(rootA)
    nameEL.grid(row = 1 , column = 1)
    pwEL = Entry(rootA , show = '*')
    pwEL.grid(row = 2 , column = 1)

    loginB = Button(rootA , text = "Login" , command = Checklogin)
    loginB.grid(columnspan = 2 , sticky = W)
    rmuser = Button(rootA , text = "Delete User" , fg = 'red' ,command = Del)
    rmuser.grid(columnspan = 2 , sticky = W)
    rootA.mainloop()

def Checklogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
    if nameEL.get() == uname and pwEL.get() == pword:
        r = Tk()
        r.title("Hello :D ")
        r.geometry("150x150")
        rlbl = Label(r , text = "\n[+] Logged In")
        rlbl.pack()
        r.mainloop()
    else:
        r = Tk()
        r.title(" Failed ")
        r.geometry("150x150")
        rlbl = Label(r , text = "\n [+] Invalid Login")
        rlbl.pack()
        r.mainloop()

def Del():
    os.remove(creds)
    rootA.destroy()
    Signup()

if os.path.isfile(creds):
    Login()
else:
    Signup()


