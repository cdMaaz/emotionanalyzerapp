from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
model = joblib.load('pipeline.pickle')
app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict/")
def predict_emotion(data: TextRequest):
    
    prediction = model.predict([data.text])[0]
    
    return {"emotion": prediction}
# To start 'uvicorn api:app --reload'