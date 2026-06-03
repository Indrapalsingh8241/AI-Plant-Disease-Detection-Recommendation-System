import os
import gdown

MODEL_PATH = "backend/models/plant_disease_prediction_model.h5"

FILE_ID = "1SLauGsRKvfzpfe0SXH6VWHn73vKOMz-_"

URL = f"https://drive.google.com/uc?id={FILE_ID}"


def download_model():

    if not os.path.exists(MODEL_PATH):

        print("Downloading model from Google Drive...")

        gdown.download(
            URL,
            MODEL_PATH,
            quiet=False
        )

        print("Model downloaded successfully.")