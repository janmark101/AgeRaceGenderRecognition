import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
import os

model_path = '.'


gender_map = {
    0: "Male",
    1: "Female"
}

race_map = {
    0 : 'White',
    1: 'Black',
    2: 'Asian',
    3: 'Indian',
    4: 'Other',
}

age_map = {
    0 : '[0-9]', 
    1 : '[10-19]',
    2 : '[20-29]',
    3 : '[30-39]',
    4 : '[40-49]',
    5 : '[50-59]', 
    6 : '[60-69]',
    7 : '[70-79]',
    8 : '[80-89]', 
    9 : '[90-99]', 
}

model = load_model('model.h5')

def prepare_img(img_path):
    print(img_path)
    img = Image.open(img_path)
    img_array = img.resize((224,224))
    img_array = img_array.convert('RGB')
    img_array = np.array(img_array) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    set_x_label(img_array)
    
def predict(img):
    race_pred, gender_pred, age_pred = model.predict(img)
    return tf.nn.softmax(race_pred),tf.nn.sigmoid(gender_pred), tf.nn.softmax(age_pred)
    
def set_x_label(img):
    race_pred, gender_pred, age_pred = predict(img)
    label_pred.config(text=f"Predicted: {age_map[age_pred.numpy().argmax()]},{gender_map[gender_pred.numpy()[0,0] > 0.5]},{race_map[race_pred.numpy().argmax()]}")


def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
    if file_path:
        img = Image.open(file_path)
        img_path = file_path
        img = img.resize((400, 400))  
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
        prepare_img(img_path)
        



# Tworzenie głównego okna
root = tk.Tk()
root.title("AgeRaceGender Recognition")
root.geometry("600x550")

label = tk.Label(root)
label.pack(padx=10, pady=10)

label_pred = tk.Label(root, text="",font=("Arial",16))
label_pred.pack(pady=20)  

button = tk.Button(root, text="Choose an image", command=choose_image)
button.pack(padx=10, pady=10)



root.mainloop()
