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



class Face_Recognition:
    
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1400x670+0+0")  # Correct format for geometry
        self.root.title("Face Recognition System")
        
        
        self.title_lbl = Label(self.root, text="FACE RECOGNISE", 
        font=("Arial", 20, "bold"), bg="silver", fg="black")                           
        self.title_lbl.place(x=0, y=0, width=1380, height=40)
        
        
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()    
        
        
        # Load Image
        DETECTOR= Image.open(r"c:\Users\darsh\OneDrive\Pictures\Facedetec bg.jpg")
        DETECTOR =  DETECTOR .resize((1380, 750), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
        self.photoDETECTOR  = ImageTk.PhotoImage( DETECTOR )

        
        First_label = Label(self.root, image=self.photoDETECTOR)
        First_label.place(x=0, y=40, width=1380, height=750)
        
        
        
        DETECTOR1 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Detector1.jpg")
        DETECTOR1 = DETECTOR1.resize((500, 800), Image.LANCZOS) 
        self.photoDETECTOR1 = ImageTk.PhotoImage(DETECTOR1)

        # Display Image
        First_label = Label(self.root, image=self.photoDETECTOR1)
        First_label.place(x=10, y=60, width=500, height=640)
        
        
        
        
        DETECTOR2 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Detector1.jpg")
        DETECTOR2 = DETECTOR2.resize((500, 640), Image.LANCZOS) 
        self.photoDETECTOR2 = ImageTk.PhotoImage(DETECTOR2)

        # Display Image
        First_label = Label(self.root, image=self.photoDETECTOR2)
        First_label.place(x=857, y=60, width=500, height=640)
        
        
        
        
        DETECTOR2 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Detector1.jpg")
        DETECTOR2 = DETECTOR2.resize((500, 640), Image.LANCZOS) 
        self.photoDETECTOR2 = ImageTk.PhotoImage(DETECTOR2)

        # Display Image
        First_label = Label(self.root, image=self.photoDETECTOR2)
        First_label.place(x=857, y=60, width=500, height=640)
        
        
        
        DETECTOR3 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Detectoe button.png")
        DETECTOR3 = DETECTOR3.resize((150, 150),Image.LANCZOS) 
        self.photoDETECTOR3 = ImageTk.PhotoImage(DETECTOR3)

        # Display Image
        First_label = Label(self.root,image=self.photoDETECTOR3)
        First_label.place(x=610, y=350, width=150, height=150)
        
        
        
        B1 = ttk.Button(self.root, image=self.photoDETECTOR3,command=self.face_recog ,cursor= "hand2")
        B1.place(x=610, y=350, width=150, height=150)
        
        
        
        B2 =Button(self.root,text="Click Here",fg='black',background='green',font=("Arial",12,'bold'),command=self.face_recog ,cursor= "hand2")
        B2.place(x=610, y=502, width=150, height=30)
        
        
    #------------------------------------------------- Attendence------------------------------------------------------------------#
    
    def mark_attemndence(self,i,r,n,d):
        with open("Darshan.csv","r+",newline="\n")as f:
            myData_list=f.readlines()
            name_list=[]
            for line in myData_list:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},preset")
                
            
            
            
        
        
        
        
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)
            coord = []
            
                
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                messagebox.showinfo("Successfully","photo captured")

                conn = mysql.connector.connect(
                host='localhost',
                user="root",
                password="Dar@2004",
                database="biometric_software",
                port=3306
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name, Department, Roll_No FROM `student info` WHERE Class_Student=%s", (id,))
                result = my_cursor.fetchone()
                i="+".join(i)

                if result:
                    i,r,n,d= result
                    if confidence > 77:
                        cv2.putText(img, f"id:{i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll_No: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attemndence(i,r,n,d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]
            return coord

        def recognise(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(r"C:\Users\darsh\OneDrive\Documents\ATTENDENCE SYSTEM\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()

            
if __name__ == "__main__" :
        root = Tk()
        obj = Face_Recognition(root) 
        root.mainloop()
        
        