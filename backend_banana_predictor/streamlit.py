import streamlit as st
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
st.markdown(
        """
        <style>
        .reportview-container {
            background: url('./bg.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("# Bananas Maturity Classification ")
st.sidebar.markdown("# Main Page")
MODEL=tf.keras.models.load_model("./1")
CLASS_NAMES = ["Banana_G1", "Banana_G2", "Rotten"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

def predict(
    file: UploadFile = File(...)
):
    image=read_file_as_image(file.read())
    shape=image.shape
    img_batch=np.expand_dims(image, 0)
    # resize image to (256,256,3)
    img_batch=tf.image.resize(img_batch,(256,256))
    prediction=MODEL.predict(img_batch)
    predicted_class=CLASS_NAMES[np.argmax(prediction[0])]
    confidence=np.max(prediction[0])
    if predicted_class=="Banana_G2":
        predicted_class="Green Banana- not ripen"
    elif predicted_class=="Banana_G1":
        predicted_class="Mature Banana -ripen"
    else:
        predicted_class="Rotten Banana"
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

st.write("Upload an image or capture one with your camera")

option = st.selectbox("Choose an option", ["Upload Image", "Capture Image"])

if option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = read_file_as_image(uploaded_file.read())
        shape=image.shape
        img_batch=np.expand_dims(image, 0)
        # resize image to (256,256,3)
        img_batch=tf.image.resize(img_batch,(256,256))
        prediction=MODEL.predict(img_batch)
        predicted_class=CLASS_NAMES[np.argmax(prediction[0])]
        confidence=np.max(prediction[0])
        if predicted_class=="Banana_G2":
            predicted_class="Green Banana- not ripen"
        elif predicted_class=="Banana_G1":
            predicted_class="Mature Banana -ripen"
        else:
            predicted_class="Rotten Banana"
        # return {
        #     'class': predicted_class,
        #     'confidence': float(confidence)
        # }
        st.image(image, caption=f"Predicted class: {predicted_class}, Confidence: {confidence:.2f}")

elif option == "Capture Image":
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    captured = False
    capture_button = st.button("Capture Image")
    close_button = st.button("Close Camera")
    while True:
        ret, frame = cap.read()
        if close_button:
            break
        if not captured:
            stframe.image(frame, channels="BGR", caption="Camera")
        if capture_button and not captured:
            try:
                captured = True
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(frame_rgb)
                # img_pil = Image.fromarray(frame)
                img_byte_arr = BytesIO()
                img_pil.save(img_byte_arr, format='jpeg')
                img_byte_arr = img_byte_arr.getvalue()
                img = read_file_as_image(img_byte_arr)
                img_batch = np.expand_dims(img, 0)
                img_batch = tf.image.resize(img_batch, (256, 256))
                prediction = MODEL.predict(img_batch)
                predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
                confidence = np.max(prediction[0])
                if predicted_class == "Banana_G2":
                    predicted_class = "Green Banana - not ripe"
                elif predicted_class == "Banana_G1":
                    predicted_class = "Mature Banana - ripe"
                else:
                    predicted_class = "Rotten Banana"
                st.image(frame_rgb, caption=f"Predicted class: {predicted_class}, Confidence: {confidence:.2f}")
                capture_button = st.button("Capture Image", key="capture_btn")
            except:
                continue
    cap.release()
    cv2.destroyAllWindows()
        
    




