import json
import os
from datetime import datetime

HISTORY_FILE = "classification_history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_classification(bird_name, confidence, image_name, predictions, scientific_name="Unknown"):
    history = load_history()

    record = {
        "bird_name": bird_name,
        "scientific_name": scientific_name,
        "confidence": round(confidence * 100, 2),
        "image_name": image_name,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "predictions": [
            {
                "label": item["label"],
                "confidence": round(item["score"] * 100, 2)
            }
            for item in predictions
        ]
    }

    history.insert(0, record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def clear_history():
    with open(HISTORY_FILE, "w") as file:
        json.dump([], file, indent=4)