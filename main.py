import os
from tkinter import *
import decode

window = Tk()
window.title("usage without a permit is illegal")
window.resizable(width=False, height=False)
window.iconbitmap("icon/image.ico")
window.geometry("400x350")
chars = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def session():
    global user_name
    login_window.destroy()
    session_window = Toplevel(window)
    session_window.resizable(width=False, height=False)
    session_window.iconbitmap("icon/image.ico")
    session_window.geometry("600x400")
    session_window.title("dashboard window __ilprofessore ")

    var = " and welcome to your Dashboard"
    db = Label(session_window, text="Hello " + user_name + var, bg="grey", padx=400, pady=15, font=12)
    db.pack()
    kar = " your most recent notification is displayed below:"
    lAbeL = Label(session_window, text=user_name + "," + kar, padx=5, pady=5, font=10, fg="red")
    lAbeL.pack(padx=5, pady=5)
    notification_file = open("files/" + user_name + "_notif" + ".ilprofessore", "r")
    notification_file_read = notification_file.read()

    notification_file_read = decode.decode_module(notification_file_read)

    Label(session_window, text="").pack()

    my_text_box = Entry(session_window, width=100)
    my_text_box.insert(0, notification_file_read)
    my_text_box.pack(padx=20, pady=20)

    Label(session_window, text="").pack()
    Label(session_window, text="ctrl+c", fg="red").pack()
    Label(session_window, text="to copy", fg="red").pack()
    Label(session_window, text="").pack()

    Button(session_window, text="exit", fg="red", padx=70, pady=10, command=session_window.destroy).pack(padx=10, pady=10)

    session_window.mainloop()


def pass_error():
    error_window = Toplevel(login_window)
    error_window.resizable(width=False, height=False)
    error_window.iconbitmap("icon/image.ico")
    error_window.geometry("200x150")
    error_window.title("failure window __ilprofessore ")

    Label(error_window, text="").pack()
    Label(error_window, text="wrong pin!", font=12).pack()
    Label(error_window, text="").pack()
    bUtT = Button(error_window, text="OK", fg="red", padx=30, pady=10, command=error_window.destroy)
    bUtT.pack(padx=10, pady=10)

    error_window.mainloop()


def login_error():
    login_error_window = Toplevel(login_window)
    login_error_window.resizable(width=False, height=False)
    login_error_window.iconbitmap("icon/image.ico")
    login_error_window.geometry("200x150")
    login_error_window.title("failure window __ilprofessore ")

    Label(login_error_window, text="").pack()
    Label(login_error_window, text="login failure!", font=12).pack()
    Label(login_error_window, text="").pack()
    xar = login_error_window.destroy
    butT = Button(login_error_window, text="OK", fg="red", padx=30, pady=10, command=xar)
    butT.pack(padx=10, pady=10)

    login_error_window.mainloop()


def login_success():
    session()


def login_user():
    global user_name
    user_name = user_login_info.get()
    pass_word = pass_login_info.get()
    user_name = user_name.lower()

    if user_name == "":
        user_name = "public"
    if pass_word == "":
        pass_word = "147"

    for i in chars:  # this piece of code will be fundamental in enabling encryption.
        for k in str(pass_word):
            if i == k:
                sys.exit()

    pass_word = decode.decode_module(pass_word)

    user_login_info.delete(0, END)
    pass_login_info.delete(0, END)

    dir_files_list = os.listdir("files")  # my innovation !
    if user_name + ".ilprofessore" in dir_files_list:
        login_file = open("files/" + user_name + ".ilprofessore", "r")
        login_file_read = login_file.read().splitlines()  # good one !
        if pass_word in login_file_read:
            login_success()
        else:
            pass_error()
    else:
        login_error()


def login():
    global login_window
    login_window = Toplevel(window)
    login_window.resizable(width=False, height=False)
    login_window.iconbitmap("icon/image.ico")
    login_window.geometry("400x350")
    login_window.title("login window __ilprofessore ")

    global user_login_info
    global pass_login_info
    Label(login_window, text="fill in the below login details", bg="grey", padx=400, font=12).pack()
    Label(login_window, text="").pack()
    Label(login_window, text="username *").pack()
    user_login_info = Entry(login_window)
    user_login_info.pack()
    Label(login_window, text="").pack()
    Label(login_window, text="pin (nums only) *").pack()
    pass_login_info = Entry(login_window, fg="white")
    pass_login_info.pack()
    Label(login_window, text="").pack()
    lbutt = Button(login_window, text="Submit", padx=400, pady=10, fg="blue", command=login_user)
    lbutt.pack(padx=100, pady=10)
    lbut = Button(login_window, text="Back", padx=400, pady=10, fg="red", command=login_window.destroy)
    lbut.pack(padx=100, pady=10)

    login_window.mainloop()


def register_user():
    username = user_info.get()
    password = pass_info.get()
    username = username.lower()

    for i in chars:  # this piece of code will be fundamental in enabling encryption.
        for k in str(password):
            if i == k:
                sys.exit()

    if username == "":
        username = "public"
    if password == "":
        password = "147"

    dir_files_list_reg = os.listdir("files")
    if username + ".ilprofessore" in dir_files_list_reg:
        sys.exit()  # program exits if a username is repeated for registration

    password = decode.decode_module(password)

    container = open("files/" + username + ".ilprofessore", "w")
    container.write(username + "\n")
    container.write(password)
    Label(register_window, text="Registration Successful", fg="green", font=12).pack()
    container.close()
    user_info.delete(0, END)
    pass_info.delete(0, END)


def register():
    global register_window
    register_window = Toplevel(window)
    register_window.resizable(width=False, height=False)
    register_window.iconbitmap("icon/image.ico")
    register_window.geometry("400x350")
    register_window.title("registration window __ilprofessore ")

    global user_info
    global pass_info
    Label(register_window, text="fill in the below details", bg="grey", padx=400, font=12).pack()
    Label(register_window, text="").pack()
    Label(register_window, text="username *").pack()
    user_info = Entry(register_window)
    user_info.pack()
    Label(register_window, text="").pack()
    Label(register_window, text="pin (nums only) *").pack()
    pass_info = Entry(register_window, fg="white")
    pass_info.pack()
    Label(register_window, text="").pack()
    bbutt = Button(register_window, text="Submit", padx=400, pady=10, fg="blue", command=register_user)
    bbutt.pack(padx=100, pady=10)
    zar = register_window.destroy
    bbut = Button(register_window, text="Back", padx=400, pady=10, fg="red", command=zar)
    bbut.pack(padx=100, pady=10)

    register_window.mainloop()


label1 = Label(window, text="__ilprofessore company ltd.", bg="grey", padx=400, pady=10, font=12)
label1.pack(padx=10, pady=10)
Label(window, text="").pack()
Button(window, text="Register", padx=400, pady=10, fg="blue", command=register).pack(padx=10, pady=10)
Label(window, text="").pack()
Button(window, text="Login", padx=400, pady=10, fg="blue", command=login).pack(padx=10, pady=10)
Label(window, text="").pack()
Button(window, text="Exit", padx=400, pady=10, fg="red", command=sys.exit).pack(padx=10, pady=10)

window.mainloop()
