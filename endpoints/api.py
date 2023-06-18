from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from service import MyModel
from models import Input, Output


app = FastAPI(description="Web Applicatin for stroke prediction ML model",
              version= "0.0.1",)
# Configure CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model_path = 'D:/University/5th_year/فصل2/ML/project/stroke/models/best_estimator_logistic_regression.pkl'
model = MyModel(model_path= model_path)
 
@app.post("/predict_stroke", response_model= Output)
async def predict(input: Input):
    prediction = model.predict(input_data= input)
    output_data = Output(prediction=prediction)
    return output_data


    
    