import tkinter as tk
from tkinter import messagebox
from login_page import auth
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_home():
    hide_sections()
    home_frame.place(x=0, y=130, width=1670, height=730)

def show_about():
    hide_sections()
    about_frame.place(x=0, y=130, width=1670, height=730)
    plot_pie_chart()
    plot_bar_graph()

def show_contact():
    hide_sections()
    contact_frame.place(x=0, y=130, width=1670, height=730)

def show_more():
    hide_sections()
    more_frame.place(x=0, y=130, width=1670, height=730)

def hide_sections():
    home_frame.place_forget()
    about_frame.place_forget()
    contact_frame.place_forget()
    more_frame.place_forget()

def route_pages():
    pass

def plot_pie_chart():
    if not hasattr(plot_pie_chart, 'canvas'):
        labels = ['Not Intrested In', 'Finacial Constraints', 'Engaged In domestic', 'School is so far']
        sizes = [25, 35, 20, 20]
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        explode = (0.1, 0, 0, 0)  

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')  
        plot_pie_chart.canvas = FigureCanvasTkAgg(fig, about_frame)
        plot_pie_chart.canvas.draw()
        plot_pie_chart.canvas.get_tk_widget().place(x=50, y=100, width=700, height=400)

def plot_bar_graph():
    if not hasattr(plot_bar_graph, 'canvas'):
        categories = ['Primary', 'Secondary', 'Graduation', 'Masters']
        values = [23, 17, 35, 29]

        fig, ax = plt.subplots()
        ax.bar(categories, values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
        ax.set_xlabel('Categories')
        ax.set_ylabel('Values')
        ax.set_title('Bar Graph Example')

        plot_bar_graph.canvas = FigureCanvasTkAgg(fig, about_frame)
        plot_bar_graph.canvas.draw()
        plot_bar_graph.canvas.get_tk_widget().place(x=800, y=100, width=700, height=400)

root = tk.Tk()
root.geometry("1360x730+0+0")
root.state("zoomed")
root.title("Student Dropout Analysis")
root.configure(bg='orange')
root.resizable(False, False)

header_label = tk.Label(root, text="Student Dropout Analysis", font=('Helvetica', 24, 'bold'), pady=20, bg='orange')
header_label.pack()

nav_frame = tk.Frame(root, bg='orange')
nav_frame.pack()

home_button = tk.Button(nav_frame, text="Home", padx=10, pady=5, command=show_home, bg='red', fg='white', bd=0)
home_button.grid(row=0, column=0, padx=10)

about_button = tk.Button(nav_frame, text="About", padx=10, pady=5, command=show_about, bg='red', fg='white', bd=0)
about_button.grid(row=0, column=1, padx=10)

contact_button = tk.Button(nav_frame, text="Contact", padx=10, pady=5, command=show_contact, bg='red', fg='white', bd=0)
contact_button.grid(row=0, column=2, padx=10)

login_button = tk.Button(nav_frame, text="Login", padx=10, pady=5, command=auth, bg='red', fg='white', bd=0)
login_button.grid(row=0, column=3, padx=10)

exit_button = tk.Button(nav_frame, text="Exit", padx=10, pady=5, command=lambda: (exit()), bg='red', fg='white', bd=0)
exit_button.grid(row=0, column=4, padx=10)

home_frame = tk.Frame(root, bg="orange")
about_frame = tk.Frame(root, bg='orange')
contact_frame = tk.Frame(root, bg='red')
more_frame = tk.Frame(root, bg='red')

te = "Welcome to Student Dropout-Portal"
home_label = tk.Label(home_frame, text=te, wraplength=800, font=('Helvetica', 20, 'bold'), bg='orange', fg='white')
home_label.place(x=80, y=30, width=1380, height=100)


left_image = tk.PhotoImage(file="pic/pic1.png")  
right_image = tk.PhotoImage(file="pic/pic_n.png")  


left_image_label = tk.Label(home_frame, image=left_image, bg="orange")
right_image_label = tk.Label(home_frame, image=right_image, bg="orange")


left_image_label.place(x=50, y=150,height=500, width=700)  # Adjust x, y as needed
right_image_label.place(x=800, y=150, height=500, width=700)  # Adjust x, y as needed


ab_te = (
    "A detailed View"
)
about_label = tk.Label(about_frame, text=ab_te, wraplength=800, justify="center", font=('Helvetica', 18, 'bold'), bg='orange', fg='white')
about_label.place(x=0, y=50, width=1670, height=50)


contact_label = tk.Label(contact_frame, wraplength=800, text="Contact Section: Email us at ASPERstudentportal@gmail.com", font=('Helvetica', 18, 'bold'), bg='red', fg='white')
contact_label.place(x=0, y=50, width=1380, height=580)

show_home()

root.mainloop()
