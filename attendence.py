from tkinter import *  # Fixed typo
from tkinter import ttk
from PIL import Image, ImageTk
import os
import cv2.face
import mysql.connector
from tkinter import messagebox
import numpy as np
import cv2
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


mydata=[]




class Attendence:
    
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1400x670+0+0")  # Correct format for geometry
        self.root.title("Face Recognition System")
        
        
        
        
        
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_Department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendence=StringVar()
        

        
        self.title_lbl = Label(self.root, text="STUDENT ATTENDENCE SYSTEM", 
        font=("Arial", 20, "bold"), bg="grey", fg="black")
        self.title_lbl.place(x=0, y=127, width=1380, height=40)
        
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()    

        # Load and display images (same as before)
        img_biometric = Image.open(r"c:\Users\darsh\OneDrive\Pictures\LTSSaddleback-Attendance.jpg")
        img_biometric = img_biometric.resize((1380, 128), Image.Resampling.LANCZOS) 
        self.photoimg_biometric = ImageTk.PhotoImage(img_biometric)
        First_label = Label(self.root, image=self.photoimg_biometric)
        First_label.place(x=0, y=0, width=1380, height=128)

        img_student = Image.open(r"c:\Users\darsh\OneDrive\Pictures\LTSSaddleback-Attendance.jpg")
        img_student = img_student.resize((1430, 600), Image.LANCZOS)  
        self.photoimg_student = ImageTk.PhotoImage(img_student)
        First_label = Label(self.root, image=self.photoimg_student)
        First_label.place(x=0, y=160, width=1430, height=600)
        
        
        Student_frame = ttk.LabelFrame(self.root, padding=3, relief="ridge",style="My.TLabelframe")
        Student_frame.place(x=10, y=170, width=1360, height=610)
        
        
        self.LEFT_frame = ttk.LabelFrame(Student_frame, padding=10, relief="ridge",text="Student Attendendence Detail")
        self.LEFT_frame.place(x=5, y=1, width=650, height=600)
        
        
        img_left = Image.open(r"d:\Images\Attendence system.jpg")
        img_left = img_left.resize((620, 60),Image.LANCZOS)  
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        First_label = Label(self.LEFT_frame, image=self.photoimg_left)
        First_label.place(x=0, y=0, width=620, height=60)
        
        
        
        
        #Class_Student_Information
        
        #Class student Frame 
        self.Class_Student_Frame = ttk.LabelFrame(self.LEFT_frame, padding=10, relief="ridge", text="Class Student Information")
        self.Class_Student_Frame.place(x=0, y=145, width=680, height=270)
        
        
        #Student ID

        Employee_Id = Label(self.Class_Student_Frame, text="ID", font=("times new roman", '8'))
        Employee_Id.grid(row=0, column=0, sticky="w")

        self.Employee_Id = Entry(self.Class_Student_Frame,textvariable=self.var_atten_id,font=("times new roman", '8'))
        self.Employee_Id.grid(row=0, column=1, sticky='w',padx=5,pady=2.5)
        
        #student Name

        
        Name = Label(self.Class_Student_Frame, text="Name",font=("times new roman", '8'))
        Name.grid(row=2, column=0, sticky="w")

        self.Name_Entry = Entry(self.Class_Student_Frame, textvariable=self.var_name,font=("times new roman", '8'))
        self.Name_Entry.grid(row=2, column=1, sticky='w', padx=5,pady=2.5)
        
        
        #Date of day
        
        Date = Label(self.Class_Student_Frame,text="Date", font=("times new roman", '8'))
        Date.grid(row=4, column=0, sticky="w")
        

        self.Date = Entry(self.Class_Student_Frame,textvariable=self.var_date, font=("times new roman", '8'))
        self.Date.grid(row=4, column=1, sticky='w',padx=5,pady=2.5)
        
        
        
        
        #Department
        
        
        Department = Label(self.Class_Student_Frame, text="Department", font=("times new roman", '8'))
        Department.grid(row=2, column=4, sticky="w")


        self.Department = Entry(self.Class_Student_Frame,textvariable=self.var_Department ,font=("times new roman", '8'))
        self.Department.grid(row=2, column=5, sticky='w',padx=5,pady=2.5)

        
        
        
        #student devision 

        
        Time = Label(self.Class_Student_Frame, text="Time", font=("times new roman", '8'))
        Time.grid(row=4, column=4, sticky="w")
        

        self.Time = Entry(self.Class_Student_Frame,textvariable=self.var_time  ,font=("times new roman", '8'))
        self.Time.grid(row=4, column=5, sticky='w',padx=5,pady=4)
        
        
        #Roll No
        

        Roll_No = Label(self.Class_Student_Frame, text="Roll No", font=("times new roman", '8'))
        Roll_No.grid(row=0, column=4, sticky="w")
        

        self.Roll_No = Entry(self.Class_Student_Frame,textvariable=self.var_roll,font=("times new roman", '8'))
        self.Roll_No.grid(row=0, column=5, sticky='w',padx=5,pady=4)
        
        
        
        Attendence_Status=Label(self.Class_Student_Frame, text='Attendence Status',font=("times new roman", '8'), background="white")
        Attendence_Status.grid(row=5,column=0)
        self.Attendence_Status=ttk.Combobox(self.Class_Student_Frame,font=("times new roman", '7'),state="readonly")
        self.Attendence_Status.grid(row=5,column=1,padx=5,pady=2,sticky='w')
        self.Attendence_Status["values"]=("Status","Present","Absent")
        self.Attendence_Status.current(0)
        
        
        
        
        Import_CSV=ttk.Button(self.Class_Student_Frame,text="Import CSV",width=15,command=self.importcsv)
        Import_CSV.place(x=125,y=160)
        
        
        
        Export_CSV=ttk.Button(self.Class_Student_Frame,text="Export CSV",width=15,command=self.exportcsv)
        Export_CSV.place(x=245,y=160)
        
        
        
        Update=ttk.Button(self.Class_Student_Frame,command=self.update_data,text="Update ",width=15)
        Update.place(x=365,y=160)
        
        
        Search=ttk.Button(self.Class_Student_Frame,text="Search",width=15,command=self.search_by_id)
        Search.place(x=5,y=160,)
        
# ================== Search Frame ================== #
        

        lbl_search = Label(self.Class_Student_Frame, text="Enter Employee ID:", font=("times new roman", 10), bg="white")
        lbl_search.grid(row=50, column=0, padx=5, pady=5)

        self.search_entry = Entry(self.Class_Student_Frame, font=("times new roman", 10))  # <== FIXED: self.search_entry
        self.search_entry.grid(row=50, column=1, padx=0, pady=5)
        
        
        Reset=ttk.Button(self.Class_Student_Frame,text="Reset ",width=15,command=self.reset_data)
        Reset.place(x=485,y=160)


        
    
        
        RIGHT_frame = ttk.LabelFrame(Student_frame, padding=10, relief="ridge",text="Student attendence Detail")
        RIGHT_frame.place(x=682, y=1, width=650, height=600)
        
        
        
        
        

        
        
        
        Table_frame = Frame(Student_frame,relief=RIDGE,bd=3)
        Table_frame.place(x=685, y=120, width=635, height=300)
        
        
#===================================================== Scroll Bar===================================================================# 
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.AttendenceReportTable=ttk.Treeview(Table_frame,columns=("Employeid","rollno" ,"Name" ,"Department" ,"time" ,"date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)
        
        
        self.AttendenceReportTable.heading("Employeid",text="Employen ID ")
        self.AttendenceReportTable.heading("rollno",text="Roll no")
        self.AttendenceReportTable.heading("Name",text="Name")
        self.AttendenceReportTable.heading("Department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date ")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
        
        
        
        self.AttendenceReportTable.column("Employeid",width=100)
        self.AttendenceReportTable.column("rollno",width=100)
        self.AttendenceReportTable.column("Name",width=100)
        self.AttendenceReportTable.column("Department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
        
        self.AttendenceReportTable["show"]="headings"
        self.AttendenceReportTable.pack(fill= BOTH, expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        #============================================================= FETCH DATA =====================================================================================#
        
    def fetchData(self, rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("", END, values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
            parent=self.root
        )

        if fln == "" or not fln:
            return  # Cancelled

        try:
            with open(fln, newline='') as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file:\n{e}", parent=self.root)

    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to export", parent=self.root)
                return

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
                parent=self.root
            )

            if fln == "" or not fln:
                return  # Cancelled

            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)

            messagebox.showinfo("Data Exported", f"Your data was exported successfully to:\n{os.path.basename(fln)}", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_Department.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendence.set(rows[6])
        
        
    def update_data(self):
        selected = self.AttendenceReportTable.focus()
        if not selected:
            messagebox.showerror("Error", "No record selected to update", parent=self.root)
            return
    
    # Gather updated data from entry fields
        updated_data = (
            self.var_atten_id.get(),
            self.var_roll.get(),
            self.var_name.get(),
            self.var_Department.get(),
            self.var_time.get(),
            self.var_date.get(),
            self.Attendence_Status.get()
        )
    
    # Update the selected item in Treeview
        self.AttendenceReportTable.item(selected, values=updated_data)
    
    # Optional: Update data in mydata list (if needed for export)
        selected_index = self.AttendenceReportTable.index(selected)
        mydata[selected_index] = updated_data
    
        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
        
        
        
    def search_by_id(self):
        search_id = self.search_entry.get().strip()

        if not search_id:
            messagebox.showwarning("Input Error", "Please enter an Employee ID to search.", parent=self.root)
            return

        found = False
        for item in self.AttendenceReportTable.get_children():
            values = self.AttendenceReportTable.item(item, "values")
            if values and values[0] == search_id:  # Assuming Employee ID is in column 0
                self.AttendenceReportTable.selection_set(item)  # Highlight the row
                self.AttendenceReportTable.focus(item)
                self.AttendenceReportTable.see(item)
                found = True
                break

        if not found:
            messagebox.showinfo("Not Found", f"No record found with Employee ID: {search_id}", parent=self.root)

        

        
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_Department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendence.set("")
        
        
        

if __name__ == "__main__":
    root = Tk()
    app = Attendence(root)
    root.mainloop()