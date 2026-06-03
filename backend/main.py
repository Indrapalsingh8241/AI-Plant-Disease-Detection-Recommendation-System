from fastapi import FastAPI, UploadFile, File
from PIL import Image

from backend.services.prediction import predict_image
from backend.services.llm import get_ai_recommendation

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Plant Disease Prediction API Running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(file.file).convert("RGB")

    result = predict_image(image)

    disease = result["disease"]

    recommendation = get_ai_recommendation(disease)

    return {
        "disease": disease,
        "confidence": result["confidence"],
        "recommendation": recommendation
    }