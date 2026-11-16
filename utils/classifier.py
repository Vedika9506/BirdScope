import streamlit as st
from transformers import pipeline
from PIL import Image

MODEL_NAME = "chriamue/bird-species-classifier"


@st.cache_resource
def load_model():

    classifier = pipeline(
        "image-classification",
        model=MODEL_NAME,
        device=-1
    )

    return classifier


def classify_bird(image):

    model = load_model()

    image = image.convert("RGB")

    predictions = model(image, top_k=5)

    return predictions