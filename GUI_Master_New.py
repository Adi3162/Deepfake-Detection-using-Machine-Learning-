import tkinter as tk
from PIL import Image, ImageTk
import csv
import time
import numpy as np
import cv2
from tkinter.filedialog import askopenfilename
import os
import shutil
from tensorflow import keras
import Train_FDD_cnn as TrainM


# Setup root window in fullscreen
root = tk.Tk()
root.state('zoomed')  # Fullscreen
root.title("DeepFake Video Detection")

# Set background image
bg_image_path = "f.jpg"  # Ensure this file exists
img = Image.open(bg_image_path)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
bg = img.resize((screen_width, screen_height))
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=0)

# Utility to create (or recreate) folders
def create_folder(FolderN):
    dst = os.path.join(os.getcwd(), FolderN)
    if os.path.exists(dst):
        shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(dst)

# Exit app
def CLOSE():
    root.destroy()

# Display result label
def update_label(str_T):
    result_label = tk.Label(root, text=str_T, width=70, font=("bold", 20), bg='cyan', fg='black')
    result_label.place(x=screen_width//2 - 400, y=screen_height - 100)

# Train model
def train_model():
    update_label("Model Training Started...")
    start = time.time()
    X = TrainM.main()
    end = time.time()
    elapsed = f"Execution Time: {end - start:.2f} seconds"
    msg = f"Model Training Completed\n{X}\n{elapsed}"
    update_label(msg)

# Play video inside the tkinter window
def run_video(VPathName, XV, YV, S1, S2):
    cap = cv2.VideoCapture(VPathName)

    def show_frame():
        ret, frame = cap.read()
        if not ret:
            return
        cap.set(cv2.CAP_PROP_FPS, 30)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image).resize((S1, S2))
        imgtk = ImageTk.PhotoImage(image=img)
        lmain = tk.Label(root)
        lmain.place(x=XV, y=YV)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    show_frame()

# Select and preview video
def VIDEO():
    global fn
    fileName = askopenfilename(title='Select Video', filetypes=[("MP4 files", "*.mp4")])
    fn = fileName
    if fn and fn.lower().endswith('.mp4'):
        run_video(fn, 560, 190, 753, 485)
    else:
        print("Select a valid .mp4 file")

# Fullscreen DeepFake detection video player
def show_FDD_video(video_path):
    from keras.models import load_model

    model_path = r"C:\Users\Admin\Desktop\Deepfake Detection Project 100% code\model2.h5"  # <-- FIXED path
    img_cols, img_rows = 64, 64
    FALLModel = load_model(model_path)

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"{video_path} cannot be opened")
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    green = (0, 255, 0)
    red = (0, 0, 255)
    i = 1

    cv2.namedWindow('FDD', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('FDD', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = video.read()
        if not ret:
            break

        img = cv2.resize(frame, (img_cols, img_rows), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        X_img = img.reshape(-1, img_cols, img_rows, 1).astype('float32') / 255

        predicted = FALLModel.predict(X_img)
        label = 1 if predicted[0][1] > 0.5 else 0
        label_text = "DeepFake Video Detected" if label == 1 else "Original Video Detected"
        color = red if label == 1 else green

        frame = cv2.putText(frame, f"Frame: {i}", (5, 30), font, 1, color, 2, lineType=cv2.LINE_AA)
        frame = cv2.putText(frame, f"Label: {label_text}", (5, 70), font, 1, color, 2, lineType=cv2.LINE_AA)

        cv2.imshow('FDD', frame)
        if cv2.waitKey(30) & 0xFF == 27:  # ESC to quit
            break
        i += 1

    video.release()
    cv2.destroyAllWindows()

# Choose video for verification
def Video_Verify():
    global fn
    fileName = askopenfilename(title='Select Video to Verify', filetypes=[("MP4 files", "*.mp4")])
    fn = fileName
    if fn and fn.lower().endswith('.mp4'):
        show_FDD_video(fn)
    else:
        print("Select a valid .mp4 file")

# UI Buttons
button5 = tk.Button(root, command=Video_Verify, text="Deepfake Video", width=20,
                    font=("Times", 20), bg="black", fg="white")
button5.place(x=100, y=200)

close = tk.Button(root, command=CLOSE, text="Exit", width=20,
                  font=("Times", 20), bg="red", fg="white")
close.place(x=100, y=270)

# Start the GUI loop
root.mainloop()





