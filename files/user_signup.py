from tkinter import *
from tkinter import messagebox
import sqlite3
from files import user_login
from PIL import ImageTk, Image

def run():
    root = Tk()
    root.title('Sign up')
    root.geometry("925x500+300+200")
    root.config(bg='#fff')
    root.resizable(False, False)

    def start():
        user_login.login()
    def Database():
        signup_message = '''
                    You have successfully signed up
                    Go to the login page to login
                '''
        try:
            if user.get() == '' or password.get() == '' or con_pass.get() == '':
                messagebox.showerror('Error', 'Please fill in all details')
            
            else:
                if password.get() == con_pass.get() and user.get() != '':
                    conn = sqlite3.connect("users.db")
                    cursor = conn.cursor()
                    cursor.execute("CREATE TABLE `user_details` (user_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
                    cursor.execute("INSERT INTO `user_details` (username, password) VALUES(?, ?);", (str(user.get()), str(password.get())))
                    cursor.execute("SELECT * FROM `user_details`")
                    conn.commit()
                    fetch = cursor.fetchall()
                    messagebox.showinfo('Signup success', signup_message)
                    cursor.close()
                    conn.close()
                elif password.get() != con_pass.get():
                    messagebox.showerror('Auth failed', 'Passwords don\'t match')
        except:     
            if password.get() == con_pass.get() and user.get() != '':
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO `user_details` (username, password) VALUES(?, ?)", (str(user.get()), str(password.get())))
                cursor.execute("SELECT * FROM `user_details`")
                conn.commit()
                fetch = cursor.fetchall()
                messagebox.showinfo('Signup success', signup_message)
                cursor.close()
                conn.close()
    frame1 = Frame(root,width=479, height=500,bg="white")    
    frame1.place(x=0,y=0)
    img = ImageTk.PhotoImage(Image.open("assets/signup.jpeg"))
    Label(frame1, image=img, bg="white").place(x=50, y=50)

    frame = Frame(root, width=350, height=450,bg="white")
    frame.place(x=480, y=20)

    heading = Label(frame,text="Sign Up",fg="#fc8704",bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)
    #################### username ###################################
    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')




    user = Entry(frame,width=25,fg='#fc8704',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=107)

    ###################### Password   ####################################
    def on_enter(e):
        password.delete(0,'end')

    def on_leave(e):
        code = password.get()
        if code == '':
            password.insert(0, 'Password')


    password = Entry(frame,width=25,fg='#fc8704',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    password.place(x=30, y=150)
    password.insert(0, "Password")
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=177)

    ######################### confirm password ###################################
    def on_enter(e):
        con_pass.delete(0,'end')

    def on_leave(e):
        con_code = con_pass.get()
        if con_code == '':
            con_pass.insert(0, 'Confirm password')


    con_pass = Entry(frame,width=25,fg='#fc8704',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    con_pass.place(x=30, y=220)
    con_pass.insert(0, "Confirm Password")
    con_pass.bind('<FocusIn>', on_enter)
    con_pass.bind('<FocusOut>', on_leave)

    Frame(frame, width=295,height=2,bg='black').place(x=25,y=247)

    ##############################################################
    Button(frame,width=39,pady=7,text='Sign up', bg='#fc8704',fg='white',border=0, command=Database).place(x=35, y=284)
    label = Label(frame, text="Have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',10))
    label.place(x=80,y=350)

    sign_in = Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#fc8704',font=('',10,'bold'), command=start)
    sign_in.place(x=189,y=350)




    mainloop()