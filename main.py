from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {"message" : "hello world"}

@app.post('/')
def hello():
    return {"message" : "hi world"}