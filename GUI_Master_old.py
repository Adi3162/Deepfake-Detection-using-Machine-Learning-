import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import VITModel 
import sqlite3
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("DeepFake Detection")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('df1.jpg')
image2 =image2.resize((1550,800))

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)




#
lbl = tk.Label(root, text="DeepFake Detection using Machine Learning", font=('times', 25,' bold '), height=2, width=80,bg="#152238",fg="white")
lbl.place(x=0, y=3)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=250, height=900, bd=5, font=('times', 14, ' bold '),bg="#152238",fg="#FFFFFF")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=0)

    
def update_label1(str_T):
     #clear_img()
     result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
     result_label.place(x=300, y=450)
     
     
     
 ################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
     #clear_img()
     result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
     result_label.place(x=350, y=400)  
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= VITModel.main()
    print(X)
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from tensorflow.keras.models import load_model
    

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
       
       
        model = load_model('deepfake_model.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        deepfake=np.argmax(prediction)
        print(deepfake)
        
        
        
        if deepfake == 0:
            Cd="Real Face Detected"
        elif deepfake == 1:
            Cd="DeepFake Face Detected"
        
        
        A=Cd
        return A

############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=400)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        X1="Selected Image is {0}".format(X)
        
        end = time.time()
        
        
            
        ET = f"\nExecution Time: {end - start:.4f} seconds"
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir="C:/Users/Admin/Desktop/Deepfake Detection Project 100% code/dataset/testing", title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)



    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    


#################################################################################################################
def window():
    root.destroy()

def video():
    from subprocess import call
    call(["python","GUI_Master_New.py"])


button1 = tk.Button(frame_alpr, text="Upload_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=60)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=120)


button3 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button3.place(x=10, y=180)
#
#
button4 = tk.Button(frame_alpr, text="Video Prediction", command=video,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button4.place(x=10, y=240)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=290)



root.mainloop()