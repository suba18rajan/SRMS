from tkinter import *
from PIL import Image, ImageTk
from course import Courseclass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
from PIL import Image, ImageTk, ImageDraw
from datetime import *
from time import *
from math import *
import sqlite3
from tkinter import messagebox, ttk


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1520x800+0+0")
        self.root.config(bg="white")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        #Menu Frame
        M_Frame = LabelFrame(
            self.root, text="Menus", font=("times new roman", 15), bg="white"
        )
        M_Frame.place(x=10, y=70, width=1500, height=80)

        #Button
        btn_course = Button(
            M_Frame,
            text="Courses",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course,
        )
        btn_course.place(x=20, y=5, width=200, height=40)

        btn_student = Button(
            M_Frame,
            text="Students",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student,
        )
        btn_student.place(x=280, y=5, width=200, height=40)

        btn_result = Button(
            M_Frame,
            text="Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result,
        )
        btn_result.place(x=540, y=5, width=200, height=40)

        btn_view = Button(
            M_Frame,
            text="View Student Results",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report,
        )
        btn_view.place(x=800, y=5, width=200, height=40)

        btn_logout = Button(
            M_Frame,
            text="Logout",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.logout,
        )
        btn_logout.place(x=1040, y=5, width=200, height=40)

        btn_exit = Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.exit_,
        )
        btn_exit.place(x=1280, y=5, width=200, height=40)

        self.bg_img = Image.open("images/bg1.png")
        self.bg_img = self.bg_img.resize((980, 400), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        lbl_bg = Label(self.root, image=self.bg_img)
        lbl_bg.place(x=500, y=230, width=920, height=350)

        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white",
        )
        self.lbl_course.place(x=500, y=580, width=300, height=100)

        self.lbl_student = Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white",
        )
        self.lbl_student.place(x=810, y=580, width=300, height=100)

        self.lbl_result = Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white",
        )
        self.lbl_result.place(x=1120, y=580, width=300, height=100)

        self.lbl = Label(
            self.root,
            text="\n\nAnalog Clock",
            font=(
                "Book Antiqua",
                25,
                "bold",
            ),
            fg="white",
            compound=BOTTOM,
            bg="#081923",
            bd=0,
        )
        self.lbl.place(x=50, y=230, height=450, width=350)
        self.working()
        self.update_details()
    
        #footer
        lbl_footer=Label(self.root,text="SRMS-Student Result Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="#033054",fg="white").pack(side=BOTTOM,fill=X)


    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        draw.line(
            (origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))),
            fill="#DF005E",
            width=4,
        )
        draw.line(
            (origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))),
            fill="white",
            width=3,
        )
        draw.line(
            (origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))),
            fill="yellow",
            width=2,
        )
        draw.ellipse((195, 195, 210, 210), fill="black")
        clock.save("clock_new.png")
   


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Courseclass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to logout?", parent=self.root
        )
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to Exit?", parent=self.root
        )
        if op == True:
            self.root.destroy()



