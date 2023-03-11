from fastapi import FastAPI
import numpy as np 
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class ModelInput(BaseModel):
    area_income: float
    house_age: float
    number_of_rooms: float
    number_of_bed_rooms: float
    area_population: float

@app.post('/house_price_prediction')
def price_pred(input_parameters: ModelInput):
    try:
        with open('linear_regression_model.pkl', 'rb') as f:
            house_price_model = pickle.load(f)
    except:
        return {"error": "Could not load model"}

    input_dict = input_parameters.dict()
    input_list = [input_dict[k] for k in input_dict.keys()]
    prediction = house_price_model.predict([input_list])
    prediction = json.dumps(prediction.tolist())
    return {"The predicted price of the house is: $": prediction}
    
@app.get('/')
def home():
    message = "Welcome to Dockerized ML Model Serving With FastApi"
    return message


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)