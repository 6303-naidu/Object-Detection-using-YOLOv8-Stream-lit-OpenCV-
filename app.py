import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile

st.title("YOLOv8 Object Detection")

model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    img = cv2.imread(tfile.name)

    results = model(img)
    annotated_img = results[0].plot()

    st.image(annotated_img, caption="Detected Objects", channels="BGR")
