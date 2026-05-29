from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id : int
    name : str
    description : str

todos = []

@app.get('/')
def show_todos():
    return todos

@app.post('/')
def hello():
    return {"message" : "hi world"}