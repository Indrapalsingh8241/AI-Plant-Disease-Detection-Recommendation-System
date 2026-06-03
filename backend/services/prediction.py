import json
from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow.keras.layers import Dense as KerasDense
from backend.services.model_downloader import download_model

download_model()

from tensorflow.keras.models import load_model

MODEL_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_PATH = MODEL_DIR / "plant_disease_prediction_model.h5"
CLASS_PATH = MODEL_DIR / "class_indices.json"


class DenseNoQuantization(KerasDense):
    def __init__(self, *args, quantization_config=None, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_config(cls, config):
        config.pop("quantization_config", None)
        return super().from_config(config)


def load_prediction_model():
    return load_model(
        MODEL_PATH,
        custom_objects={"Dense": DenseNoQuantization},
        compile=False,
        safe_mode=False
    )


model = load_prediction_model()

with open(CLASS_PATH, "r") as f:
    class_indices = json.load(f)

idx_to_class = {
    v: k for k, v in class_indices.items()
}
def predict_image(image):

    image = image.resize((224, 224))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    predictions = model.predict(
        image,
        verbose=0
    )

    predicted_index = np.argmax(
        predictions
    )

    confidence = float(
        np.max(predictions)
    )

    disease = idx_to_class[
        predicted_index
    ]

    return {
        "disease": disease,
        "confidence": round(
            confidence * 100,
            2
        )
    }