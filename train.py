from tkinter import *  # Fixed typo
from tkinter import Tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import cv2
import numpy as np
from tkinter import Label
from time import strftime

class Train:
    


    def __init__(self,root):
        self.root = root                                                                    
        self.root.geometry("1400x670+0+0")

        self.root.title("Face Recognition System")
        
        
        
        self.title_lbl = Label(self.root, text="Train Data Set", 
        font=("Arial", 20, "bold"), bg="Red", fg="black")                           
        self.title_lbl.place(x=0, y=0, width=1380, height=40)
        
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()    
        
        
        
        # Load Image
        imgC = Image.open(r"c:\Users\darsh\OneDrive\Pictures\asian-women-using-face-detection-facial-recognition-technology-with-ai-brain.jpg")
        imgC = imgC.resize((467,160), Image.LANCZOS) 
        self.photoimgC = ImageTk.PhotoImage(imgC)

        # Display Image
        First_label = Label(self.root, image=self.photoimgC)
        First_label.place(x=0, y=40, width=467, height=160)
        
        
        
        
        
        
        # Load Image
        imgD = Image.open(r"c:\Users\darsh\OneDrive\Pictures\OIP.jpg")
        imgD = imgD.resize((467,160), Image.LANCZOS) 
        self.photoimgD = ImageTk.PhotoImage(imgD)
        
        # Display Image
        First_label = Label(self.root, image=self.photoimgD)
        First_label.place(x=467, y=40, width=467, height=160)
        
        
        
        
        
        
        
        
        #load image
        imgF = Image.open(r"c:\Users\darsh\OneDrive\Pictures\training-datasets-l.jpg")
        imgF = imgF.resize((1400,500), Image.LANCZOS) 
        self.photoimgF = ImageTk.PhotoImage(imgF)

        # Display Image
        First_label = Label(self.root, image=self.photoimgF)
        First_label.place(x=0, y=242, width=1400, height=500)
        
        
        
        
        # Load Image
        imgG = Image.open(r"c:\Users\darsh\OneDrive\Pictures\istockphoto-1139858627-612x612.jpg")
        imgG = imgG.resize((467,160), Image.LANCZOS) 
        self.photoimgG = ImageTk.PhotoImage(imgG)

        # Display Image
        First_label = Label(self.root, image=self.photoimgG)
        First_label.place(x=934, y=40, width=467, height=160)
        
        
        
        Train_button =Button(self.root,text="TRAINED DATASET", command=self.train_data_classifier,compound="center", font=("Arial", 10, "bold"),fg="black",background="gray",cursor="hand2")
        Train_button.place(x=458, y=205, width=480, height=40)
        
        
        
    def train_data_classifier(self):
        data_dir=("User")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        # we using numpy for 88% better performance in the array converting 
        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        #-------------------------------------Train The Classifier---------------------------------------------
        
        
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result",'Training dataset completed!!')
            
        

        

if __name__ == "__main__" :
    root = Tk()
    obj = Train(root) 
    root.mainloop()
        
        
        
        
        
        
        
        
