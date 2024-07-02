import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import mysql.connector

def submit_form():
    name = entry_name.get()
    father_name = entry_father_name.get()
    occupation = entry_occupation.get()
    address = entry_address.get("1.0", tk.END).strip()
    contact = entry_contact.get()
    family_income = entry_family_income.get()
    gender = gender_var.get()

    if name == "" or gender == "":
        msg.showerror("Invalid", "All fields are required")
    else:
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="V6392205398", database="stud_log"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO student_submit (name, father_name, occupation, address, contact, family_income, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, father_name, occupation, address, contact, family_income, gender)
            )
            conn.commit()
            conn.close()
            msg.showinfo("Success", f"Your data has been saved: {name}")
        except Exception as es:
            msg.showerror("Error", f"Due to: {str(es)}")

def student_form():
    root = tk.Toplevel()
    root.title("Student Registration Form")
    root.state('zoomed')
    root.configure(bg="#A0937D")

    style = ttk.Style()
    style.configure("TLabel", font=("Times New Roman", 14))
    style.configure("TEntry", font=("Times New Roman", 14))
    style.configure("TRadiobutton", font=("Times New Roman", 14))
    style.configure("TButton", font=("Times New Roman", 14))
    style.configure("EntryStyle.TEntry", font=("Times New Roman", 14), borderwidth=0, relief="solid")  # Custom style for entries

    
    title_label = ttk.Label(root, text="Student Registration Form", font=("Helvetica", 24, "bold"),background="#A0937D")
    title_label.place(x=650, y=20)

    
    label_name = ttk.Label(root, text="Name:", background="#A0937D", foreground="white")
    label_name.place(x=400, y=100)

    global entry_name
    entry_name = tk.Entry(root, width=50,bd = 0)
    entry_name.place(x=550, y=100,height=30)

    label_father_name = ttk.Label(root, text="Father's Name:",background="#A0937D", foreground="white")
    label_father_name.place(x=400, y=160,height=30)

    global entry_father_name
    entry_father_name = tk.Entry(root, width=50,bd = 0)
    entry_father_name.place(x=550, y=160, height=30)

    label_occupation = ttk.Label(root, text="Occupation:",background="#A0937D", foreground="white")
    label_occupation.place(x=400, y=220)

    global entry_occupation
    entry_occupation = tk.Entry(root, width=50,bd = 0)
    entry_occupation.place(x=550, y=220,height=30)

    label_address = ttk.Label(root, text="Address:",background="#A0937D", foreground="white")
    label_address.place(x=400, y=280)

    global entry_address
    entry_address = tk.Text(root, width=50, height=6, font=("Helvetica", 14), bd=0, relief="solid")
    entry_address.place(x=550, y=280)

    label_contact = ttk.Label(root, text="Contact:",background="#A0937D", foreground="white")
    label_contact.place(x=400, y=450)

    global entry_contact
    entry_contact = tk.Entry(root, width=50,bd=0)
    entry_contact.place(x=550, y=450,height=30)

    label_family_income = ttk.Label(root, text="Family Income:",background="#A0937D", foreground="white")
    label_family_income.place(x=400, y=500)

    global entry_family_income
    entry_family_income = tk.Entry(root, width=50,bd = 0)
    entry_family_income.place(x=550, y=500,height=30)

    label_gender = ttk.Label(root, text="Gender:",background="#A0937D", foreground="white")
    label_gender.place(x=400, y=590)

    global gender_var
    gender_var = tk.StringVar()
    male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male",background="#A0937D", )
    male_radio.place(x=550, y=590)

    female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female",background="#A0937D")
    female_radio.place(x=650, y=590)

    btn_img = tk.PhotoImage(file='pic/button_submit.png')
    submit_button = tk.Button(root,image=btn_img , command=submit_form,background="#A0937D",bd=0)
    submit_button.place(x=675, y=650)

    root.mainloop()


