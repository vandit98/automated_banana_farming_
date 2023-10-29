

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import json
import requests
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


latitude = np.random.uniform(-90, 90)

# Generate a random longitude (-180 to +180 degrees)
longitude = np.random.uniform(-180, 180)

# print("Random Latitude:", latitude)
# print("Random Longitude:", longitude)

origin = [
   "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



MODEL=tf.keras.models.load_model("./1")
CLASS_NAMES = ["Banana_G1", "Banana_G2", "Rotten"]

@app.get("/")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image=read_file_as_image(await file.read())
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

    obj =  {
                'class': predicted_class,
                'confidence': float(confidence),
                "lattitude":latitude,
                "longitude":longitude
            }
    payload = str(obj)
    url = "https://play.orkes.io/api/workflow/croptech"
    headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'X-Authorization': os.getenv('OREKUS_AUTH_KEY')
}
    response = requests.request("POST", url, headers=headers, data=payload)
    return {
        'predicted_class': predicted_class,
        'confidence': float(confidence),
        "lattitude":latitude,
        "longitude":longitude
    }






@app.post("/predict2")
async def predict2():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('camera', frame)
        k = cv2.waitKey(1)
        if k == 49:  # press 1 to quit camera
            return {"message": "camera closed"}
        elif k == 99:  # press c to capture image
            img_pil = Image.fromarray(frame)
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
            cv2.imshow('captured image', frame)
            k=cv2.waitKey(0)
            cap.release()
            cv2.destroyAllWindows()            

            return {
                'class': predicted_class,
                'confidence': float(confidence),
                "lattitude":latitude,
                "longitude":longitude
            }


                
from pydantic import BaseModel

# Define a request model to handle the inputs
class MongoInput(BaseModel):
    predicted_class: str
    confidence: float
    latitude: float
    longitude: float


@app.post("/mongo_feasible_input")
async def mongo(input_data: MongoInput):
    # Access the input data using input_data.image_id, input_data.predicted_class, etc.
    
    # Create a dictionary to store the data
    result_dict = {
        "class": input_data.predicted_class,
        "confidence": input_data.confidence,
        "latitude": input_data.latitude,
        "longitude": input_data.longitude
    }

    uri = os.getenv('MONGODB_URI')
    print(uri)
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['croptech']
    collection = db['croptech']
    collection.insert_one(result_dict)
    return result_dict
