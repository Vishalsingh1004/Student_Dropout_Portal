import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as msg

def submit_form():
    school_name = entry_school_name.get()
    affiliation_number = entry_affiliation_number.get()
    board_name = entry_board_name.get()
    school_address = entry_school_address.get("1.0", tk.END).strip()
    school_contact = entry_school_contact.get()
    number_of_students = entry_number_of_students.get()
    school_email = entry_school_email.get()
    principal_name = entry_principal_name.get()
    website_url = entry_website_url.get()

    if school_name == "" or affiliation_number == "":
        msg.showerror("Invalid", "All fields are required")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="V6392205398", database="school_record"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO school_submit (school_name, affiliation_number, board_name, school_address, school_contact, number_of_students, school_email, principal_name, website_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (school_name, affiliation_number, board_name, school_address, school_contact, number_of_students, school_email, principal_name, website_url)
            )
            conn.commit()
            conn.close()
            msg.showinfo("Success", f"Your data has been saved: {affiliation_number}")
        except Exception as es:
            msg.showerror("Error", f"Due to: {str(es)}")

def school_form():
    root = tk.Toplevel()
    root.title("School Registration Form")
    root.state('zoomed')
    root.configure(bg="#95D2B3")

    style = ttk.Style()
    style.configure("TLabel", font=("Times New Roman", 14))
    style.configure("TEntry", font=("Times New Roman", 14))
    style.configure("TRadiobutton", font=("Times New Roman", 14))
    style.configure("TButton", font=("Times New Roman", 14))
    style.configure("EntryStyle.TEntry", font=("Times New Roman", 14), borderwidth=0, relief="solid")  # Custom style for entries

   
    title_label = ttk.Label(root, text="School Registration Form", font=("Helvetica", 24, "bold"), background="#95D2B3",foreground="white")
    title_label.place(x=650, y=20)

    
    label_school_name = ttk.Label(root, text="School Name:", background="#95D2B3", foreground="white")
    label_school_name.place(x=400, y=100)

    global entry_school_name
    entry_school_name = tk.Entry(root, width=50, bd=0)
    entry_school_name.place(x=550, y=100, height=30)

    label_affiliation_number = ttk.Label(root, text="Affiliation Number:", background="#95D2B3", foreground="white")
    label_affiliation_number.place(x=400, y=160)

    global entry_affiliation_number
    entry_affiliation_number = tk.Entry(root, width=50, bd=0)
    entry_affiliation_number.place(x=550, y=160, height=30)

    label_board_name = ttk.Label(root, text="Board Name:", background="#95D2B3", foreground="white")
    label_board_name.place(x=400, y=220)

    global entry_board_name
    entry_board_name = tk.Entry(root, width=50, bd=0)
    entry_board_name.place(x=550, y=220, height=30)

    label_school_address = ttk.Label(root, text="School Address:", background="#95D2B3", foreground="white")
    label_school_address.place(x=400, y=280)

    global entry_school_address
    entry_school_address = tk.Text(root, width=50, height=6, font=("Times New Roman", 14), bd=0, relief="solid")
    entry_school_address.place(x=550, y=280)

    label_school_contact = ttk.Label(root, text="School Contact:", background="#95D2B3", foreground="white")
    label_school_contact.place(x=400, y=430)

    global entry_school_contact
    entry_school_contact = tk.Entry(root, width=50, bd=0)
    entry_school_contact.place(x=550, y=430, height=30)

    label_number_of_students = ttk.Label(root, text="Number of Students:", background="#95D2B3", foreground="white")
    label_number_of_students.place(x=400, y=490)

    global entry_number_of_students
    entry_number_of_students = tk.Entry(root, width=50, bd=0)
    entry_number_of_students.place(x=570, y=490, height=30)

    label_school_email = ttk.Label(root, text="School Email:", background="#95D2B3", foreground="white")
    label_school_email.place(x=400, y=540)

    global entry_school_email
    entry_school_email = tk.Entry(root, width=50, bd=0)
    entry_school_email.place(x=550, y=540, height=30)

    label_principal_name = ttk.Label(root, text="Principal Name:", background="#95D2B3", foreground="white")
    label_principal_name.place(x=400, y=590)

    global entry_principal_name
    entry_principal_name = tk.Entry(root, width=50, bd=0)
    entry_principal_name.place(x=550, y=590, height=30)

    label_website_url = ttk.Label(root, text="Website URL:", background="#95D2B3", foreground="white")
    label_website_url.place(x=400, y=640)

    global entry_website_url
    entry_website_url = tk.Entry(root, width=50, bd=0)
    entry_website_url.place(x=550, y=640, height=30)

   
    btn_img = tk.PhotoImage(file='pic/button_submit.png')
    submit_button = tk.Button(root, image=btn_img, command=submit_form, background="#95D2B3", bd=0)
    submit_button.place(x=675, y=700)

    root.mainloop()


