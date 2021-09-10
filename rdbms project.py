from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("COLLEGE STUDENT MANAGEMENT SYSTEM")


        # variable

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        #1 image

        img = Image.open(r"project image\1.jpg")
        img = img.resize((540, 160), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        self.btn_1 = Button(self.root, image=self.photoimg, cursor= "hand2")
        self.btn_1.place(x=0, y=0, width=540, height=160)

        #2
        img_2 = Image.open(r"project image\4.jpg")
        img_2 = img_2.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_2 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=540, y=0, width=540, height=160)

        #3
        img_3 = Image.open(r"project image\3.jpg")
        img_3 = img_3.resize((540, 160), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        self.btn_3 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=1000, y=0, width=540, height=160)

        #back groud image
        img_4 = Image.open(r"project image\8.jpg")
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=160, width=1530, height=710)

        lbl_title = Label(bg_lbl, text="COLLEGE STUDENT MANAGEMENT SYSTEM", font=("times new roman", 37, "bold"), fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=1530, height=50)

        #manage frame

        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=15, y=55, width=1500, height=560)

        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=("times new roman", 12, "bold"), fg="red", bg="white")
        DataLeftFrame.place(x=10, y=10, width=660, height=540)

        # img
        img_5 = Image.open(r"project image\9.jpg")
        img_5 = img_5.resize((650, 120), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        my_img = Label(DataLeftFrame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=650, height=120)


        # course label frame information

        std_lbl_info_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Current Course Information",
                                   font=("times new roman", 12, "bold"), fg="red", bg="white")
        std_lbl_info_frame.place(x=0, y=120, width=650, height=115)

        #labels
        # department
        lbl_dep = Label(std_lbl_info_frame, text="Department:", font=("arial", 12, "bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("arial", 12, "bold"), width=17, state="readonly")
        combo_dep["value"] = ("Select Department", "BSCS", "BSSE", "MCS")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_std = Label(std_lbl_info_frame, text="Courses:", font=("arial", 12, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        com_txtcourse_std = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_course, font=("arial", 12, "bold"), width=17, state="readonly")
        com_txtcourse_std["value"] = ("Select Course", "First-Year", "Second-year", "Third-year", "Fourth-year")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        current_year = Label(std_lbl_info_frame, text="Year:", font=("arial", 12, "bold"), bg="white")
        current_year.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        com_txt_current_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year, font=("arial", 12, "bold"), width=17, state="readonly")
        com_txt_current_year["value"] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1, column=1, padx=2, sticky=W)

        # semester
        lbl_semester = Label(std_lbl_info_frame, text="Semester:", font=("arial", 12, "bold"), bg="white")
        lbl_semester.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        comsemester = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_semester, font=("arial", 12, "bold"), width=17, state="readonly")
        comsemester["value"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        comsemester.current(0)
        comsemester.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student  class label information

        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Class Course Information",
                                        font=("times new roman", 11, "bold"), fg="red", bg="white")
        std_lbl_class_frame.place(x=0, y=235, width=650, height=235)

        # student id
        lbl_id = Label(std_lbl_class_frame, text="Student_ID:", font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame, textvariable=self.va_std_id, font=("arial", 11, "bold"), width=22)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # name

        lbl_name = Label(std_lbl_class_frame, text="Student Name:", font=("arial", 11, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_name = ttk.Entry(std_lbl_class_frame, textvariable=self.var_std_name, font=("arial", 11, "bold"), width=22)
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        # division
        lbl_div = Label(std_lbl_class_frame, text="Class Section:", font=("arial", 11, "bold"), bg="white")
        lbl_div.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        com_txt_div = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_div, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_div["value"] = ("Select Section", "A", "B", "C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # roll
        lbl_roll = Label(std_lbl_class_frame, text="Roll No:", font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable=self.var_roll, font=("arial", 11, "bold"), width=22)
        txt_roll.grid(row=1, column=3, padx=2, pady=7)

        # gender

        lbl_gender = Label(std_lbl_class_frame, text="Gender:", font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame, textvariable=self.var_gender, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_gender["value"] = ("Select Gender", "Male", "Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # dob
        lbl_dob = Label(std_lbl_class_frame, text="DOB:", font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_dob = ttk.Entry(std_lbl_class_frame, textvariable=self.var_dob, font=("arial", 11, "bold"), width=22)
        txt_dob.grid(row=2, column=3, padx=2, pady=7)

        # email
        lbl_email = Label(std_lbl_class_frame, text="Email:", font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_email = ttk.Entry(std_lbl_class_frame, textvariable=self.var_email, font=("arial", 11, "bold"), width=22)
        txt_email.grid(row=3, column=1, padx=2, pady=7)

        # phone number
        lbl_phone = Label(std_lbl_class_frame, text="Phone No:", font=("arial", 11, "bold"), bg="white")
        lbl_phone.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_phone = ttk.Entry(std_lbl_class_frame, textvariable=self.var_phone, font=("arial", 11, "bold"), width=22)
        txt_phone.grid(row=3, column=3, padx=2, pady=7)

        # address

        lbl_address = Label(std_lbl_class_frame, text="Address:", font=("arial", 11, "bold"), bg="white")
        lbl_address.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_address = ttk.Entry(std_lbl_class_frame, textvariable=self.var_address, font=("arial", 11, "bold"), width=22)
        txt_address.grid(row=4, column=1, padx=2, pady=7)

        # teacher
        lbl_teacher = Label(std_lbl_class_frame, text="Teacher Name:", font=("arial", 11, "bold"), bg="white")
        lbl_teacher.grid(row=4, column=2, padx=2, pady=7, sticky=W)

        txt_teacher = ttk.Entry(std_lbl_class_frame, textvariable=self.var_teacher, font=("arial", 11, "bold"), width=22)
        txt_teacher.grid(row=4, column=3, padx=2, pady=7)

        # button frame
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=470, width=650, height=38)

        btn_Add = Button(btn_frame, text="Save", command=self.add_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_Add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), width=17, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=1)


        # right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information",
                                   font=("times new roman", 12, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=680, y=10, width=800, height=540)

        #img 2
        img_6 = Image.open(r"project image\10.jpg")
        img_6 = img_6.resize((780, 200), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)
        my_img = Label(DataRightFrame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=790, height=200)
        # search frame

        search_Frame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Information:",
                                    font=("times new roman", 12, "bold"), fg="red", bg="white")
        search_Frame.place(x=0, y=200, width=790, height=60)
        # search label

        search_by = Label(search_Frame, text="Search By:", font=("arial", 11, "bold"), fg="red", bg="yellow")
        search_by.grid(row=0, column=0, padx=5, sticky=W)
        self.var_com_search = StringVar()

        com_txt_search = ttk.Combobox(search_Frame, textvariable=self.var_com_search, font=("arial", 12, "bold"), width=18, state="readonly")
        com_txt_search["value"] = ("Select Option", "Student_ID", "Roll", "Phone")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=5, sticky=W)
        self.var_search = StringVar()

        txt_search = ttk.Entry(search_Frame, textvariable=self.var_search, font=("arial", 11, "bold"), width=22)
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_Frame, command=self.search_data, text="Search", font=("arial", 11, "bold"), width=14, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        btn_showAll = Button(search_Frame, command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), width=14, bg="blue", fg="white")
        btn_showAll.grid(row=0, column=4, padx=5)

        # ---------Student Table and scroll bar--------

        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=260, width=790, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher",),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Div")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")


        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # functions
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("ERROR", "ALL FIELD ARE REQUIRED")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mir111mir", database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get()

                                             ))
                conn.commit()

                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS", "STUDENT HAS BEEN ADDED", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("ERROR", f"Due to :{str(es)}", parent=self.root)
    # fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mir111mir", database="my_data")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    # get cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.va_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
    # update data
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("ERROR", "ALL FIELD ARE REQUIRED")
        else:
            try:
                update = messagebox.askyesno("UPDATE", "ARE YOU SURE UPDATE THIS STUDENT DATA", parent=self.root)
                if update>0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="mir111mir", database="my_data")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Division = %s, Roll = %s, Gender = %s, Dob = %s, Email = %s, Phone = %s, Address = %s, Teacher = %s where student_id = %s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),

                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.va_std_id.get()
                          ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS", "STUDENT SUCCESSFULLY UPDATE", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("ERROR", f"Due to :{str(es)}", parent=self.root)
    # delete
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("DELETE","ARE YOU SURE DELETE THIS STUDENT")
                if Delete>0:

                    conn = mysql.connector.connect(host="localhost", username="root", password="mir111mir", database="my_data")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    value = (self.va_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("DELETE","YOUR  STUDENT DATA HAS BEEN DELETED",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("ERROR", f"Due to :{str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
    # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("ERROR", "PLEASE SELECT OPTION")
        else:
            try:

                conn = mysql.connector.connect(host="localhost", username="root", password="mir111mir",
                                               database="my_data")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END, values=i)
                    conn.commit()
                conn.close()
            except EXCEPTION as es:
                messagebox.showerror("ERROR", f"Due to :{str(es)}", parent=self.root)
























if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()