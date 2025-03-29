from pydantic import BaseModel

class PredictionResponse(BaseModel):
    status: str
    prediction: list
    processing_time: float = None