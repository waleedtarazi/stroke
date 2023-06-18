import joblib
import pandas as pd
from models import Input

columns = ['gender', 
           'age', 
           'hypertension', 
           'heart_disease', 
           'ever_married', 
           'work_type', 
           'Residence_type', 
           'avg_glucose_level', 
           'bmi', 
           'smoking_status']


class MyModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, input_data: Input):
        
        feature_vector = [input_data.gender.value, input_data.age, 
                          input_data.hypertension, input_data.heart_disease, 
                          input_data.ever_married.value, input_data.work_type.value, 
                          input_data.residence_type.value, input_data.avg_glucose_level, 
                          input_data.bmi, input_data.smoking_status.value]
        
        instance = pd.DataFrame(data= [feature_vector], columns= columns)

        prediction = self.model.predict(instance)[0]
        return prediction