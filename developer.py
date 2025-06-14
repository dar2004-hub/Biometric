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




class Developer:
    
    def __init__(self,root):
        
        self.root = root
        self.root.geometry("1400x670+0+0")  # Correct format for geometry
        self.root.title("Face Recognition System")
        
        
        
        
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
        
        
        
        

        img_student = Image.open(r"c:\Users\darsh\OneDrive\Pictures\R.jpg")
        img_student = img_student.resize((1430, 600), Image.LANCZOS)  
        self.photoimg_student = ImageTk.PhotoImage(img_student)
        First_label = Label(self.root, image=self.photoimg_student)
        First_label.place(x=0, y=160, width=1430, height=600)
        
        Student_frame = ttk.LabelFrame(First_label, padding=3, relief="ridge", text="",style="My.TLabelframe")
        Student_frame.place(x=960, y=0, width=520, height=600)
        
        
        Darshan_img = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Darshan.Picture.jpg")
        Darshan_img = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Darshan.Picture.jpg")
        Darshan_img = Darshan_img.resize((120, 130), Image.LANCZOS)  
        self.photoDarshan_img = ImageTk.PhotoImage(Darshan_img)
        First_label2 = Label(Student_frame, image=self.photoDarshan_img)
        First_label2.place(x=270, y=0, width=120, height=130)
        
        Dev_Labe=Label(Student_frame,text="Hello My Name Darshan Chaubey",font=("times new roman",13,"bold"),bg='white')
        Dev_Labe.place(x=0,y=0)
        
        
        vandana_img = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Vandana.jpg")
        vandana_img = vandana_img.resize((120, 130), Image.LANCZOS)  
        self.photovandana_img = ImageTk.PhotoImage(vandana_img)
        First_label3 = Label(Student_frame, image=self.photovandana_img)
        First_label3.place(x=270, y=145, width=120, height=130)
        
        Dev_Labe=Label(Student_frame,text="Hello My Name Vandana Yadav",font=("times new roman",13,"bold"),bg='white')
        Dev_Labe.place(x=0,y=155)
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
        