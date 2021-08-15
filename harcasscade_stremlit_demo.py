import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import cv2

#inittalise haarcascade CascadeClassifier and read in model xml file for face detction 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#takes in image from streamlit fileuploader as PIL image and outputs image with bounding boxes of detected faces 
def detect_faces(image):
    #convert PIL image from rgb to cv2 BGR image
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #convert cv2 BGR image into grayscale for haarcascade CascadeClassifier
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(len(faces))
    #draw bounding boxes on original image using coordianates provided from prediction 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display image in rgb formatn and show number of detected faces  
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    st.markdown("Number of faces detected **{}**".format(len(faces)))


st.header('Basic Face Detection Using Haarcascade')
st.subheader("A simple face detection demo using haarcascade classifier from open cv")
st.caption("instructions to use: upload a png ,jpg or jpeg file and it will automatically detect faces")
uploaded_file = st.file_uploader('File uploader',type=["jpg","png","jpeg"])
if uploaded_file is not None:
    print(type(uploaded_file))
    image = Image.open(uploaded_file)
    detect_faces(image)
st.caption("Built by NYP AI team")



