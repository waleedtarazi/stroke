from pydantic import BaseModel, conint
from enum import Enum


class Gender(str,Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    
class Married(str,Enum):
    yes = 'yes' 
    no = 'no'
    
class Work_type(str, Enum):
    private = 'Private'
    self_employed = 'Self-employed'
    govt_job = 'Govt_job'
    never_worked = 'Never_worked'
    children = 'children'

class Residence(str, Enum):
    urban = 'Urban'
    rural = 'Rural'

class Smoking(str, Enum):
    formerly = 'formerly smoked'
    never = 'never smoked'
    smokes = 'smokes'
    unknown = 'Unknown'    
 


class Input(BaseModel):
    age: int
    hypertension: conint(ge=0, le=1)
    heart_disease: conint(ge=0, le=1)
    avg_glucose_level: float
    bmi: float
    
    gender: Gender
    ever_married: Married
    work_type: Work_type
    residence_type: Residence 
    smoking_status: Smoking
    
class Output(BaseModel):
    prediction: conint(ge=0, le=1)
