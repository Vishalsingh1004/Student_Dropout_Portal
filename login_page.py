import tkinter as tk
from tkinter import messagebox as msg
import mysql.connector
from submit_form import school_form
from stu_reg_page import student_form
 


def validate_student_login():
    username = student_username_entry.get()
    password = student_password_entry.get()
    print(username)
    print(password)

    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="V6392205398",
        database="stud_log"
    )
    cursor = conn.cursor()

    
    query = "SELECT * FROM student_record WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        
        msg.showinfo("Success", "Login successful!")
        student_form()

        

    else:
        
        msg.showerror("Error", "Invalid Username or Password")

    
    cursor.close()
    conn.close()


def validate_school_login():
    username = school_username_entry.get()
    password = school_password_entry.get()
    print(username)
    print(password)

    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="V6392205398",
        database="school_record"
    )
    cursor = conn.cursor()

    
    query = "SELECT * FROM school_log  WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        
        msg.showinfo("Success", "Login successful!")
        school_form()

    else:
        
        msg.showerror("Error", "Invalid Username or Password")

    
    cursor.close()
    conn.close()

def auth():
    login_window = tk.Toplevel()
    login_window.title("Login Page")
    login_window.configure(bg='orange')
    login_window.state("zoomed")
    login_window.resizable(False, False)

    global school_username
    global school_pass

    school_username = tk.StringVar()
    school_pass = tk.StringVar()

    global student_username
    global student_pass

    student_username = tk.StringVar()
    student_pass = tk.StringVar()

    school_label = tk.Label(login_window, text="School Login", font=("Times New Roman", 55, "bold"), fg='blue', bg='orange')
    school_label.place(x=490, y=10)

    school_username_label = tk.Label(login_window, text="Username:", fg='white', bg='orange', font=("Verdana", 15, "bold"))
    school_username_label.place(x=450, y=120)

    global school_username_entry
    school_username_entry = tk.Entry(login_window, font="Verdana 15", bd=0, textvariable=school_username)
    school_username_entry.place(x=600, y=120, height=30, width=400)

    school_password_label = tk.Label(login_window, text="Password:", fg='white', bg='orange', font=("Verdana", 15, "bold"))
    school_password_label.place(x=450, y=190)

    global school_password_entry
    school_password_entry = tk.Entry(login_window, font="Verdana 15", bd=0, show="*", textvariable=school_pass)
    school_password_entry.place(x=600, y=190, height=30, width=400)

    btn_img = tk.PhotoImage(file='pic/button_login.png')

    school_submit_button = tk.Button(login_window, image=btn_img, bg="orange", bd=0, fg="orange", command=validate_school_login)
    school_submit_button.place(x=670, y=250)


    student_label = tk.Label(login_window, text="Student Login", font=("Times New Roman", 55, "bold"), fg='white', bg='orange')
    student_label.place(x = 490, y = 320)

    student_username_label = tk.Label(login_window, text="Username:", fg='white', bg='orange', font=("Verdana", 15, "bold"))
    student_username_label.place(x = 450, y = 450)

    global student_username_entry
    student_username_entry = tk.Entry(login_window, font="Verdana 15", bd=0, textvariable=student_username)
    student_username_entry.place(x = 600, y = 450, height=30, width=400)

    student_password_label = tk.Label(login_window, text="Password:", fg='white', bg='orange', font=("Verdana", 15, "bold"))
    student_password_label.place(x = 450, y = 520)

    global student_password_entry
    student_password_entry = tk.Entry(login_window, font="Verdana 15", bd=0, show="*", textvariable=student_pass)
    student_password_entry.place(x = 600, y = 520, height=30, width=400)

    student_submit_button = tk.Button(login_window, image=btn_img, bg="orange", bd=0, fg="orange",command=validate_student_login)
    student_submit_button.place(x = 670, y = 600)

    login_window.mainloop()
