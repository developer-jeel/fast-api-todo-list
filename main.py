from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id : int
    name : str
    description : str

todos = []

@app.get('/')
def home():
    return {"message" : "hello world"}

@app.post('/')
def hello():
    return {"message" : "hi world"}