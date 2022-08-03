from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

def login():
    root = Toplevel()
    root.title('login')
    root.geometry("925x500+300+200")
    root.config(bg='#fff')
    root.resizable(False, False)


    def signin():
        username = user.get()
        code = password.get()

        if user.get() == '' and password.get() == '':
                messagebox.showerror('Error', 'Please Enter your username and password')
        elif user.get() == '':
            messagebox.showerror('Error', 'Please Enter your username')
        elif password.get() == '':
            messagebox.showerror('Error', 'Please Enter your password')
        else:
                conn = sqlite3.connect("users.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM `user_details`;")
                fetch = cursor.fetchall()
                for data in fetch:
                    if username == data[1] and code == data[2]:
                        screen = Toplevel(root)
                        screen.title('app')
                        screen.geometry("925x500+300+200")
                        screen.config(bg='white')

                        Label(screen, text=f"Hello {data[1]}",bg='#fff',font=('calibri(body)',50,'bold')).pack(expand=True)
                        
                        screen.mainloop()
                    elif username == data[1] and code != data[2]:
                        messagebox.showinfo('Wrong details', 'Wrong password')
                    elif username != data[1] and code == data[2]:
                        messagebox.showinfo('Wrong details', 'Wrong username')
                cursor.close()
                conn.close()

        
        
    frame1 = Frame(root,width=479, height=500,bg="white")    
    frame1.place(x=0,y=0)    
    img = ImageTk.PhotoImage(Image.open('./assets/signin.jpg'))
    Label(frame1, image=img, bg="white").place(x=50,y=50)

    frame = Frame(root, width=350, height=350,bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame,text="Sign in",fg="#fc8704",bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
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

    ##############################################################
    Button(frame,width=39,pady=7,text='Sign in', bg='#fc8704',fg='white',border=0,command=signin).place(x=35, y=204)
    label = Label(frame, text="Don't have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=270)

    sign_up = Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#fc8704')
    sign_up.place(x=215,y=270)




    mainloop()