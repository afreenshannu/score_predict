from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

df = joblib.load("model/score_train_model.pkl")


class stu_data(BaseModel):
    study_time: float
    attendance: float
    gender_male: int


app = FastAPI()


@app.get("/")
def root_data():
    return {"message": "This is good"}


@app.post("/shannu")
def scr_prd(data: stu_data):
    inp_data = np.array([[data.study_time, data.attendance, data.gender_male]])
    prd = df.predict(inp_data)
    return {"Predicted_score": int(prd[0])}
