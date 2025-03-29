from fastapi import FastAPI, UploadFile, File
from .schemas import PredictionResponse
from steel_defect.inference import Predictor

app = FastAPI()
predictor = Predictor("models/best_model.pth")

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    # Add image processing logic
    prediction = predictor.predict(contents)
    return {
        "status": "success",
        "prediction": prediction.tolist()
    }

def create_app():
    return app